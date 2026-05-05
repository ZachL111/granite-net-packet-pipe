import * as assert from "node:assert/strict";
import { classify, score, Signal } from "../src/policy";

const cases: Array<Signal & { score: number; decision: "accept" | "review" }> = [
  {
    "name": "case_1",
    "demand": 75,
    "capacity": 88,
    "latency": 14,
    "risk": 18,
    "weight": 10,
    "score": 120,
    "decision": "review"
  },
  {
    "name": "case_2",
    "demand": 85,
    "capacity": 103,
    "latency": 11,
    "risk": 24,
    "weight": 10,
    "score": 122,
    "decision": "review"
  },
  {
    "name": "case_3",
    "demand": 81,
    "capacity": 84,
    "latency": 22,
    "risk": 13,
    "weight": 6,
    "score": 119,
    "decision": "review"
  }
];

for (const item of cases) {
  assert.equal(score(item), item.score);
  assert.equal(classify(item), item.decision);
}
