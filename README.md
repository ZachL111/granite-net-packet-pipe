# granite-net-packet-pipe

`granite-net-packet-pipe` is a focused TypeScript codebase around design a TypeScript verification harness for packet systems, covering stream reduction, windowed input fixtures, and failure-oriented tests. It is meant to be easy to inspect, run, and extend without a hosted service.

## Granite Net Packet Pipe Walkthrough

I would read the project from the outside in: command, fixture, model, then roadmap. That keeps the networking idea grounded in files that can be checked locally.

## Capabilities

- Includes extended examples for retry behavior, including `surge` and `degraded`.
- Documents policy decisions tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.
- Stores project constants and verification metadata in `metadata/project.json`.
- Adds a repository audit script that checks structure before running the language verifier.

## Reason For The Project

The goal is to capture the core behavior in code and make the surrounding assumptions obvious. A reader should be able to run the verifier, open the fixtures, and understand why each decision was made.

## Where Things Live

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `package.json`: Node package scripts

## How It Is Put Together

The core is a scoring model over demand, capacity, latency, risk, and weight. That keeps packet shape, socket state, and retry behavior in one explicit decision path. The threshold is 179, with risk penalty 7, latency penalty 3, and weight bonus 5. The TypeScript project keeps types close to the model and compiles before running its checks.

## Command Examples

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Data Notes

`surge` is the first example I would inspect because it lands on the `accept` path with a score of 190. The broader file also keeps `degraded` at -57 and `surge` at 190, which gives the model a useful low-to-high spread.

## Check The Work

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Tradeoffs

This code is local-first. It makes no claim about deployed usage and avoids credentials, hosted state, and environment-specific setup.

## Possible Extensions

- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add a loader for `examples/extended_cases.csv` and promote selected cases into the language test suite.
- Add one more networking fixture that focuses on a malformed or borderline input.

## Getting It Running

Clone the repository, enter the directory, and run the verifier. No database server, cloud account, or token is required.
