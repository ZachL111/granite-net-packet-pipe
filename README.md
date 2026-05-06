# granite-net-packet-pipe

`granite-net-packet-pipe` explores networking with a small TypeScript codebase and local fixtures. The technical goal is to design a TypeScript verification harness for packet systems, covering stream reduction, windowed input fixtures, and failure-oriented tests.

## Reason For The Project

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Granite Net Packet Pipe Review Notes

The first comparison I would make is `socket risk` against `retry pressure` because it shows where the rule is most opinionated.

## What It Does

- `fixtures/domain_review.csv` adds cases for packet span and retry pressure.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/granite-net-packet-walkthrough.md` walks through the case spread.
- The TypeScript code includes a review path for `socket risk` and `retry pressure`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `packet span`, `retry pressure`, `route drift`, and `socket risk`.

The TypeScript implementation avoids hidden state so fixture changes are easy to reason about.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The verifier is intentionally local. It should fail if the fixture score math, lane assignment, or language-specific test drifts.

## Boundaries

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
