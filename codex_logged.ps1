param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]] $Args
)

# このスクリプトがある場所 = プロジェクト直下想定
$projectRoot = $PSScriptRoot

# ログ出力先（プロジェクト直下の .log）
$logDir = Join-Path $projectRoot ".log"
New-Item -ItemType Directory -Force $logDir | Out-Null

$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$log = Join-Path $logDir "codex_$ts.log"

# 本物の codex 実体（exe/cmd）を取得
$real = (Get-Command codex -CommandType Application -ErrorAction Stop).Source

Start-Transcript -Path $log | Out-Null
try {
  & $real @Args
  exit $LASTEXITCODE
}
finally {
  Stop-Transcript | Out-Null
}
