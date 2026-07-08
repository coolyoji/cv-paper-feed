var IMPORT_ENDPOINT = "/cv-paper-feed/import";

function install(data, reason) {}

async function startup({ id, version, resourceURI, rootURI }, reason) {
  await Zotero.initializationPromise;
  registerEndpoint();
  Zotero.debug("CV Paper Feed Importer started");
}

function shutdown({ id, version, resourceURI, rootURI }, reason) {
  if (reason === APP_SHUTDOWN) {
    return;
  }
  delete Zotero.Server.Endpoints[IMPORT_ENDPOINT];
  Zotero.debug("CV Paper Feed Importer stopped");
}

function uninstall(data, reason) {}

function registerEndpoint() {
  Zotero.Server.Endpoints[IMPORT_ENDPOINT] = CVPaperFeedImportEndpoint;
}

function response(status, body) {
  return [status, "application/json", JSON.stringify(body || {})];
}

function normalizeTitle(title) {
  return (title || "").toLowerCase().replace(/\W+/g, "");
}

function splitCreatorName(name) {
  name = (name || "").trim();
  if (!name) {
    return null;
  }
  if (name.includes(",")) {
    let [lastName, ...first] = name.split(",");
    return {
      creatorType: "author",
      firstName: first.join(",").trim(),
      lastName: lastName.trim()
    };
  }
  let parts = name.split(/\s+/);
  if (parts.length === 1) {
    return { creatorType: "author", name };
  }
  return {
    creatorType: "author",
    firstName: parts.slice(0, -1).join(" "),
    lastName: parts[parts.length - 1]
  };
}

function sourceToItemType(source) {
  source = (source || "").toLowerCase();
  if (source.includes("cvpr") || source.includes("iccv") || source.includes("eccv") || source.includes("wacv")) {
    return "conferencePaper";
  }
  return "journalArticle";
}

async function getOrCreateCollection(libraryID, name, parentID) {
  parentID = parentID || null;
  let collections = Zotero.Collections.getByLibrary(libraryID);
  let existing = collections.find((collection) => {
    return !collection.deleted
      && collection.name === name
      && (collection.parentID || null) === parentID;
  });
  if (existing) {
    return existing;
  }
  let collection = new Zotero.Collection();
  collection.libraryID = libraryID;
  collection.name = name;
  collection.parentID = parentID;
  await collection.saveTx({ skipSelect: true });
  return collection;
}

async function getDailyCollection(dateText, rootName) {
  let libraryID = Zotero.Libraries.userLibraryID;
  let parts = dateText.split("-");
  if (parts.length !== 3) {
    throw new Error("date must be YYYY-MM-DD");
  }
  let root = await getOrCreateCollection(libraryID, rootName || "每日精读论文", null);
  let year = await getOrCreateCollection(libraryID, parts[0], root.id);
  let month = await getOrCreateCollection(libraryID, parts[1], year.id);
  return getOrCreateCollection(libraryID, parts[2], month.id);
}

async function findExistingTopLevelItem(libraryID, title) {
  let normalized = normalizeTitle(title);
  if (!normalized) {
    return null;
  }
  let search = new Zotero.Search();
  search.libraryID = libraryID;
  search.addCondition("libraryID", "is", libraryID);
  search.addCondition("title", "contains", title);
  search.addCondition("itemType", "isNot", "attachment");
  let ids = await search.search();
  let items = await Zotero.Items.getAsync(ids);
  return items.find((item) => normalizeTitle(item.getField("title")) === normalized) || null;
}

async function createParentItem(paper, collectionID) {
  let item = new Zotero.Item(sourceToItemType(paper.source));
  item.libraryID = Zotero.Libraries.userLibraryID;
  item.setField("title", paper.title || "Untitled");
  if (paper.url) {
    item.setField("url", paper.url);
  }
  if (paper.summary) {
    item.setField("abstractNote", paper.summary);
  }
  if (paper.published) {
    item.setField("date", paper.published);
  }
  if (paper.source) {
    if (item.itemType === "conferencePaper") {
      item.setField("proceedingsTitle", paper.source);
    }
    else {
      item.setField("publicationTitle", paper.source);
    }
  }
  let creators = (paper.authors || []).map(splitCreatorName).filter(Boolean);
  if (creators.length) {
    item.setCreators(creators);
  }
  let tags = ["daily-deep-read", "cv-paper-feed"].concat(paper.tags || []);
  item.setTags(tags.map((tag) => ({ tag: String(tag), type: 1 })));
  item.setCollections([collectionID]);
  await item.saveTx({ skipSelect: true });
  return item;
}

async function ensureItemInCollection(item, collectionID) {
  let collections = new Set(item.getCollections());
  if (!collections.has(collectionID)) {
    collections.add(collectionID);
    item.setCollections([...collections]);
    await item.saveTx({ skipSelect: true });
  }
}

async function itemHasFileAttachment(item) {
  let childIDs = item.getAttachments();
  if (!childIDs.length) {
    return false;
  }
  let children = await Zotero.Items.getAsync(childIDs);
  return children.some((child) => child.isFileAttachment());
}

async function importPaper(paper, collectionID) {
  let libraryID = Zotero.Libraries.userLibraryID;
  let item = await findExistingTopLevelItem(libraryID, paper.title);
  let created = false;
  if (item) {
    await ensureItemInCollection(item, collectionID);
  }
  else {
    item = await createParentItem(paper, collectionID);
    created = true;
  }

  let attached = false;
  let moved = false;
  if (paper.localPath && !(await itemHasFileAttachment(item))) {
    let attachment = await Zotero.Attachments.importFromFile({
      file: paper.localPath,
      parentItemID: item.id,
      title: "Full Text PDF",
      contentType: "application/pdf",
      moveFile: true,
      saveOptions: { skipSelect: true }
    });
    attached = !!attachment;
    moved = true;
  }

  return {
    title: paper.title,
    itemID: item.id,
    itemKey: item.key,
    created,
    attached,
    moved
  };
}

function CVPaperFeedImportEndpoint() {}

CVPaperFeedImportEndpoint.prototype = {
  supportedMethods: ["POST"],
  supportedDataTypes: ["application/json"],
  permitBookmarklet: false,

  init: async function (requestData) {
    try {
      let data = requestData.data || {};
      let dateText = data.date;
      let papers = data.papers || [];
      if (!dateText || !Array.isArray(papers)) {
        return response(400, { error: "Expected JSON with date and papers[]" });
      }
      let collection = await getDailyCollection(dateText, data.rootCollection || "每日精读论文");
      let results = [];
      for (let paper of papers) {
        results.push(await importPaper(paper, collection.id));
      }
      let pane = Zotero.getActiveZoteroPane();
      if (pane && pane.collectionsView) {
        await pane.collectionsView.selectByID(collection.treeViewID);
      }
      return response(201, {
        date: dateText,
        collectionID: collection.id,
        collectionKey: collection.key,
        collectionPath: `${data.rootCollection || "每日精读论文"}/${dateText.replaceAll("-", "/")}`,
        imported: results
      });
    }
    catch (error) {
      Zotero.logError(error);
      return response(500, { error: String(error) });
    }
  }
};
