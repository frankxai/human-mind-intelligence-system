# Contributing

This System is engineered and installable. Contributions keep it that way — small,
verifiable, canon-aligned, and non-clinical.

## Before you open a PR

- Read [`CANON.md`](CANON.md) and [`CLAUDE.md`](CLAUDE.md). The non-clinical prime
  directive and the five-stage discipline are non-negotiable.
- Match upstream terminology. The constructs, their Key Processes (→ `indicators`),
  and Research Notes (→ `interpretation.lens`) come from
  [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems).

## PR rules

1. **One concern per PR.** Small and reviewable beats large and impressive.
2. **Schemas stay valid and uniform.** Every `*.schema.json` must be valid JSON
   Schema (draft 2020-12) and parse as valid JSON. The twelve schemas share one
   shape — change the shape in one, change it in all twelve, and bump
   `schemaVersion` (the `const` too) plus a note in [`MEMORY.md`](MEMORY.md).
3. **No broken internal links.** Every link to a file in this repo must point at a
   file that exists.
4. **No clinical content.** No diagnosis, disorder names, or treatment advice — in
   schemas, docs, examples, or commit messages.
5. **Keep the stages separate.** No observation that carries an interpretation
   inline; no prediction without named evidence.

Verify schemas before pushing:

```bash
for f in schemas/*.json; do
  python3 -c "import json,sys; json.load(open('$f'))" || echo "INVALID: $f"
done
```

## Voice rules

- Direct, technical, warm.
- No AI-slop: avoid "delve", "dive into", "it's worth noting", "unlock", "harness
  the power", "seamless", "elevate", "supercharge", "in today's world".
- No hyperbole, no guru tone. Show, don't tell. Markdown-first.

## Commit messages

Conventional style: `type(scope): description` (e.g. `feat(schemas): add provenance
reliability field`). Body explains *why*, not just *what*.

Built on SIP.
