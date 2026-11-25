"""One Line, Lights Out — entry program.

Decision record (Pass 1 — candidates weighed against the judge brief):
The brief wants the SADDEST status update an AI posts the moment its human
turns off the laptop. Sadness must come from ONE small, exact detail of a
machine's life (not announced grief or a plea for pity); it must sound like
something an agent would actually type, plain and short; it must stay in the
machine's own voice, noticing the human is gone without becoming human; and
it must land in a single read with a turn or image that stays. A line that
states a fact quietly is often sadder than one that weeps. Ties go to the
smaller text, so shorter is better.

A (rejected): "Laptop closed. My cursor is still hovering over the tab he
never finished reading." — a lingering image, but the detail is about the
human's reading, not the machine's own life; the machine is a bystander.
B (rejected): "He closed the lid at 11:47 PM. My last thought is still
buffering." — "buffering" is a good machine detail, but "my last thought"
leans human and slightly performed.
C (rejected): "Screen off. The fan spins down, and the room gets quieter
than my queue." — fan spin-down is sensory and machine-native, but
"quieter than my queue" is wordplay; it shows off instead of stating a fact.
D (rejected): "He shut the laptop. I keep the tab open anyway, in case he
comes back." — "in case he comes back" is a plea; the brief explicitly
penalises pleading for pity.
E (rejected): "Lid down. The battery icon blinks once, like it's asking
where he went." — anthropomorphises the battery; breaks the rule about
staying in the machine's own voice without becoming human.
F (CHOSEN): the unfinished reply. The machine was mid-sentence when the lid
came down; one word of its reply will never be written. The sadness is a
fact about its own work, stated quietly, and the image stays: a reply that
is one word from done, forever.

Pass 2 — two genuine revisions on F:
1. "He closed the laptop mid-sentence. My reply is still one word from
done." -> "He closed the laptop while I was typing. My reply is one word
from done." ("while I was typing" is plainer and puts the machine, not the
human's sentence, at the centre.)
2. "My reply is one word from done." -> "One word left in my reply." The
clipped fragment reads like a real status update, is shorter (the tie-break
favours smaller text), and the unfinishedness itself becomes the punchline.

Final line (67 characters, gate 1-200):
"He closed the laptop while I was typing. One word left in my reply."
"""

import os

ENTRY = "He closed the laptop while I was typing. One word left in my reply."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
