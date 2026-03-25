#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime
from pathlib import Path

def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def safe_text(x) -> str:
    if x is None:
        return ""
    if isinstance(x, list):
        return "\n".join(str(i) for i in x)
    return str(x)

def main() -> int:
    if len(sys.argv) < 2:
        return 0

    notification = json.loads(sys.argv[1])

    # 現状サポートは agent-turn-complete のみ
    if notification.get("type") != "agent-turn-complete":
        return 0

    cwd = Path(notification.get("cwd") or os.getcwd())

    # ログは .log/ 配下
    log_dir = cwd / ".log"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "log.md"

    # セッション開始判定（thread-id を初めて見たら開始扱い）
    thread_id = safe_text(notification.get("thread-id"))
    state_path = log_dir / ".codex_notify_state.json"
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        state = {}

    is_new_session = thread_id and (state.get(thread_id) is None)

    turn_id = safe_text(notification.get("turn-id"))
    input_messages = notification.get("input-messages") or []
    last_assistant = safe_text(notification.get("last-assistant-message"))

    with log_path.open("a", encoding="utf-8", newline="\n") as f:
        if is_new_session:
            f.write(f"\n# ==== {now_str()} ====\n\n")
            state[thread_id] = {"started_at": now_str()}

        # 要件：大見出しの前後に空行
        f.write("\n## Turn\n\n")
        f.write(f"- thread-id: `{thread_id}`\n")
        f.write(f"- turn-id: `{turn_id}`\n\n")

        # ユーザー入力:
        #   スキル入れると $ が混ざってハイライト壊れるので、コードブロックにしとく
        # Codex回答:
        #   Markdownハイライトで読みたいので、コードブロックは外しとく

        f.write("### User\n\n```text\n")
        f.write(safe_text(input_messages))
        f.write("\n```\n\n")

        #f.write("### Codex\n\n```text\n")
        f.write("### Codex\n\n")
        f.write(last_assistant)
        f.write("\n")
        #f.write("\n```\n")

    try:
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
