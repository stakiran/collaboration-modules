param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]] $Args
)

$root = $PSScriptRoot
$logDir = Join-Path $root ".log"
New-Item -ItemType Directory -Force $logDir | Out-Null

$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$logTranscript = Join-Path $logDir "codex_$ts.transcript.log"  # 元(UTF-16LE)
$logUtf8       = Join-Path $logDir "codex_$ts.log"             # 見やすい版(UTF-8)

Start-Transcript -Path $logTranscript | Out-Null
try {
  codex @Args
  $code = $LASTEXITCODE
}
finally {
  Stop-Transcript | Out-Null
}

# UTF-16LE → UTF-8 に変換（NULっぽく見える問題を回避）
Get-Content -LiteralPath $logTranscript |
  Set-Content -LiteralPath $logUtf8 -Encoding utf8

exit $code
