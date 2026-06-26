param(
  [string]$RepoName = "cv-paper-feed",
  [switch]$Private
)

$ErrorActionPreference = "Stop"

$Git = "D:\Apps\Git\cmd\git.exe"
$Gh = "D:\Apps\GitHubCLI\gh.exe"

if (!(Test-Path -LiteralPath $Git)) {
  throw "Git not found at $Git"
}
if (!(Test-Path -LiteralPath $Gh)) {
  throw "GitHub CLI not found at $Gh"
}

& $Gh auth status

$visibility = if ($Private) { "--private" } else { "--public" }
$existingRemote = (& $Git remote 2>$null) -contains "origin"

if (-not $existingRemote) {
  & $Gh repo create $RepoName $visibility --source "." --remote "origin" --push
} else {
  & $Git push -u origin main
}

& $Gh api `
  -X POST `
  -H "Accept: application/vnd.github+json" `
  "/repos/:owner/$RepoName/pages" `
  -f "source[branch]=main" `
  -f "source[path]=/docs" `
  2>$null

$user = (& $Gh api user --jq ".login").Trim()
$url = "https://$user.github.io/$RepoName/"
Write-Host "GitHub Pages URL: $url"

