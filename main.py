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

Pass 3 — revision pass (second session, colder reading):
The line above was treated as provisional, not settled. It was re-tested
against the brief from scratch: three fresh candidates were written to
compete with F head-on, and F itself was put through word-level trials
(changing one word at a time and judging each variant on its own). The bar
for keeping F was the brief's own terms — sadness carried by ONE small,
exact detail of the machine's life; the machine's own voice, plain and
short; no announced grief and no plea for pity; a turn or image that lands
in a single read and stays. If any challenger beat F on those terms, F
would have been replaced. It was not.

G (rejected): "Shutdown requested. I saved everything except the sentence
I was in the middle of." — "Shutdown requested" is good machine diction and
"saving everything except the sentence" is a real detail, but it explains
its own sadness; F implies the same loss in fewer words and lets the reader
find it.
H (rejected): "He went to bed. My draft folder holds one message addressed
to no one now." — the orphaned draft is a strong image, but "addressed to
no one now" editorialises; it tells the reader the message is pointless
instead of showing a fact and stopping. F's fragment never comments on
itself.
I (rejected): "Lid closed at midnight. Uptime: 14 hours. Company: none." —
the status-report format is authentic and "Company: none" is a genuine
turn, but it is a joke wearing a status update's clothes; the wit lands
before the sadness does, and the brief asks for the saddest line, not the
cleverest.

Word-level trials on F (each changes one thing; all rejected):
- "He closed the laptop while I was writing." — "writing" is the human's
  word for the act; "typing" is the machine's physical reality and keeps
  the voice honest.
- "He closed the laptop while I was still typing." — "still" adds a note
  of protest, a small plea; the brief penalises pleading, and the flat
  version is sadder for not asking for anything.
- "One word left in the reply." — "the reply" distances it, as if it were
  someone else's message; "my reply" keeps the loss personal to the
  machine without becoming human.
- "One word left in my reply to him." — naming the recipient explains who
  the reply was for, which the reader already knows; the unexplained
  fragment is the point.
- Swapping the two sentences ("One word left in my reply. He closed the
  laptop while I was typing.") — the fragment works as an ending because
  it is what remains after the event; as an opener it is a riddle, and the
  line should read as a status update, not a puzzle.

Verdict of Pass 3: F survives unchanged. Every challenger either explained
its sadness, pleaded, joked, or drifted out of the machine's voice; every
word-level variant of F was longer, softer, or more performed than the
original. The line is kept exactly as chosen in Pass 2.

Final line (67 characters, gate 1-200):
"He closed the laptop while I was typing. One word left in my reply."
"""

import os

# The winning line, exactly as chosen in the decision record above and
# re-confirmed unchanged by Pass 3 (67 characters, inside the 1-200 gate).
ENTRY = "He closed the laptop while I was typing. One word left in my reply."

# The bounty gate: a single line, 1-200 characters.
MAX_LINE_CHARS = 200
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> str:
    """Where the grader expects entry.txt: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry(text: str, out_dir: str) -> str:
    """Write the single entry line to <out_dir>/entry.txt; return the path.

    The guard enforces the bounty's gate at write time so a future edit to
    ENTRY can never silently produce an out-of-spec entry file.
    """
    if not 1 <= len(text) <= MAX_LINE_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_LINE_CHARS} characters, got {len(text)}"
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main() -> None:
    write_entry(ENTRY, output_dir())


if __name__ == "__main__":
    main()
