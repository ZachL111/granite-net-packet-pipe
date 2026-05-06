# Granite Net Packet Pipe Walkthrough

I use this file as a small checklist before changing the TypeScript implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | packet span | 159 | ship |
| stress | retry pressure | 151 | ship |
| edge | route drift | 168 | ship |
| recovery | socket risk | 225 | ship |
| stale | packet span | 152 | ship |

Start with `recovery` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The useful comparison is `socket risk` against `retry pressure`, not the raw score alone.
