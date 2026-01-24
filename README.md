# collaboration-modules
概要や使い方は AGENTS.md を読んでください。

Please read **AGENTS.md** for an overview and usage instructions.

## Note: Windows + VSCode を使っていて、VSCode 内ターミナルから Codex を使っている場合
- 1: Windows 側の Powershell を 7 にしておく(pswhコマンドで実行する方のpowershell)
- 2: VSCode の default profile を Powershell 7 にしておく
- 3: `%userprofile%\.codex\config.toml` に以下を追記
    - これにより InvalidOperation: Cannot set property. Property setting is supported only on core types in this language mode. エラーを防げた
 
```toml
[features]
powershell_utf8 = false
```

ここまでやるとCodex処理中のエラーメッセージが減って無駄な試行が減ると思う。
