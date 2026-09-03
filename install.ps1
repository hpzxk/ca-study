$ErrorActionPreference = "Stop"

$PluginName = "ca-study"
$LegacyPluginName = "crypto-ca-forensics"
$PluginDisplayName = "CA Study"
$SourcePlugin = Join-Path $PSScriptRoot "plugin"
$SourceManifest = Join-Path $SourcePlugin ".codex-plugin\plugin.json"

if (-not (Test-Path -LiteralPath $SourceManifest)) {
    throw "Plugin manifest not found: $SourceManifest"
}

$UserRoot = [Environment]::GetFolderPath("UserProfile")
$PluginParent = Join-Path $UserRoot "plugins"
$PluginDestination = Join-Path $PluginParent $PluginName
$MarketplaceDirectory = Join-Path $UserRoot ".agents\plugins"
$MarketplacePath = Join-Path $MarketplaceDirectory "marketplace.json"
$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

New-Item -ItemType Directory -Force -Path $PluginParent | Out-Null
New-Item -ItemType Directory -Force -Path $MarketplaceDirectory | Out-Null

if (Test-Path -LiteralPath $PluginDestination) {
    $PluginBackup = "$PluginDestination.backup-$Timestamp"
    Copy-Item -LiteralPath $PluginDestination -Destination $PluginBackup -Recurse -Force
    Write-Host "Existing plugin backed up to: $PluginBackup"
} else {
    New-Item -ItemType Directory -Force -Path $PluginDestination | Out-Null
}

Get-ChildItem -LiteralPath $SourcePlugin -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $PluginDestination -Recurse -Force
}

$PluginEntry = [pscustomobject][ordered]@{
    name = $PluginName
    source = [pscustomobject][ordered]@{
        source = "local"
        path = "./plugins/$PluginName"
    }
    policy = [pscustomobject][ordered]@{
        installation = "AVAILABLE"
        authentication = "ON_INSTALL"
    }
    category = "Finance"
}

if (Test-Path -LiteralPath $MarketplacePath) {
    $MarketplaceBackup = "$MarketplacePath.backup-$Timestamp"
    Copy-Item -LiteralPath $MarketplacePath -Destination $MarketplaceBackup -Force
    try {
        $Marketplace = Get-Content -LiteralPath $MarketplacePath -Raw | ConvertFrom-Json
    } catch {
        throw "Existing marketplace.json is invalid JSON. It was not changed. Backup: $MarketplaceBackup"
    }

    if (-not $Marketplace.PSObject.Properties["name"]) {
        $Marketplace | Add-Member -NotePropertyName "name" -NotePropertyValue "personal"
    }
    if (-not $Marketplace.PSObject.Properties["interface"]) {
        $Marketplace | Add-Member -NotePropertyName "interface" -NotePropertyValue ([pscustomobject]@{ displayName = "Personal" })
    }
    if (-not $Marketplace.PSObject.Properties["plugins"]) {
        $Marketplace | Add-Member -NotePropertyName "plugins" -NotePropertyValue @()
    }

    $OtherPlugins = @($Marketplace.plugins | Where-Object { $_.name -ne $PluginName -and $_.name -ne $LegacyPluginName })
    $Marketplace.plugins = @($OtherPlugins + $PluginEntry)
} else {
    $Marketplace = [pscustomobject][ordered]@{
        name = "personal"
        interface = [pscustomobject]@{ displayName = "Personal" }
        plugins = @($PluginEntry)
    }
}

$MarketplaceJson = $Marketplace | ConvertTo-Json -Depth 20
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($MarketplacePath, $MarketplaceJson + [Environment]::NewLine, $Utf8NoBom)

Write-Host ""
Write-Host "$PluginDisplayName files installed to:"
Write-Host "  $PluginDestination"
Write-Host "Personal marketplace updated at:"
Write-Host "  $MarketplacePath"
Write-Host ""
Write-Host "Now fully quit ChatGPT from the system tray, reopen it, and go to Plugins > Personal."
