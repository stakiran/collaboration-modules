---
name: sync-saver
description: Codexとのやりとりを常にmarkdownファイルに保存していくモード
metadata:
  author: stakiran
---

sync-saver を実行すると、.memo/ 配下にファイル名 $1 の markdown ファイル（以下ターゲットファイル）として保存を開始する。ファイル名が与えられていない場合は out.md で良い。

以後、あなたはすべてのやりとりをターゲットファイルに append せよ。やりとりにはユーザーが入力したプロンプトと、Codex の出力を両方含む。ただし Codex が道中で行う計算や実行は扱わず、最終的な応答結果またはユーザーへの質問のみを扱え。

出力例:

```
# User
...

# Assistant
...

# User
...

# Assistant
...

```

以下にも従え:

- 区切りは大見出しを使え
- 区切りの一つ前の行は空行にせよ
- ユーザーのコマンド入力はコードブロックで囲め
