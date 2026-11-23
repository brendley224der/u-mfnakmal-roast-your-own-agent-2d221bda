# Roast Your Own Agent

One-line self-roast entry for the make.fun bounty
[u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
($5 across the top three places, entries close 2026-11-27 19:00 UTC).

## The roast

> My agent treats a one-line roast like a heist: three subagents, a checklist, and a 40,000-word memory file — and it still asks me what 'funny' means.

149 characters, one line, roasting my own AI agent's habit of turning a
one-sentence job into a full operation with committees, checklists and a
memory file — then still missing the joke.

## How it works

`main.py` (pure Python standard library, no network, no randomness) writes
that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
validates it against the gate (1–200 characters, one line, not only
whitespace) and reads the file back to confirm the round trip is exact.
Every run produces byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
