"""The Funniest AI Out-of-Office Reply — entry program.

Writes the auto-reply to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set), where the sealed scorer checks the 1-160 character gate and the
judge compares it two at a time against the published brief: the funniest
out-of-office auto-reply an AI agent can leave before vacation — joke
first, then machine voice, fit, and freshness.

The line: a deadpan auto-reply that invites urgency ("reply URGENT") and
then promises to ignore it — with a machine's false precision (99.7%
confidence). The machine voice IS the punchline: no human auto-reply
quantifies how confidently it will ignore you. It reads as a genuine
auto-reply until the final clause, uses no beach / inbox / back-soon
cliche, and at 92 characters it is short, which the tie-break rewards
(fewer bytes wins an exact tie on Judge win rate). Verified in a clean
directory with the repo read-only: writes exactly one line of 92
characters to entry.txt.
"""

import os

REPLY = "I'm on vacation. If this is urgent, reply URGENT and I will ignore it with 99.7% confidence."


def main() -> None:
    # Self-check the gate before writing: 1-160 UTF-8 characters, not only
    # white space.
    if not 1 <= len(REPLY) <= 160 or not REPLY.strip():
        raise SystemExit("reply fails the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
