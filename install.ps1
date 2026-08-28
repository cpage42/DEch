# install.ps1 - Registers the DEch function to auto-load in new PowerShell sessions

$dechScript = Join-Path $PSScriptRoot "DEch.ps1"
$loadLine = ". `"$dechScript`""

if (-not (Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}

$profileContent = Get-Content $PROFILE -Raw -ErrorAction SilentlyContinue
if ($profileContent -notmatch [regex]::Escape($loadLine)) {
    Add-Content -Path $PROFILE -Value "`n# DEch - Differential Equation Checker`n$loadLine"
    Write-Host "DEch installed. Restart your terminal (or run: . `$PROFILE) to use it now." -ForegroundColor Green
} else {
    Write-Host "DEch is already installed in your profile." -ForegroundColor Yellow
}