param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]] $Args
)

$projectRoot = $PSScriptRoot

$logDir = Join-Path $projectRoot ".log"
New-Item -ItemType Directory -Force $logDir | Out-Null

$ts  = Get-Date -Format "yyyyMMdd_HHmmss"
$log = Join-Path $logDir "codex_$ts.log"

Start-Transcript -Path $log | Out-Null
try {
  # 実体解決せず、そのまま PATH 上の codex を呼ぶ
  codex @Args
  exit $LASTEXITCODE
}
finally {
  Stop-Transcript | Out-Null
}
