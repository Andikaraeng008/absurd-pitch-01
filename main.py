import os

TEXT = "We auto-decline meeting invites for AI agents that never wanted to attend standup anyway, charging $1 per polite 'sorry, I have a conflict' they never had to write."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
