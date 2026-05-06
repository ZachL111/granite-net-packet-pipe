function equal<T>(actual: T, expected: T): void {
  if (actual !== expected) {
    throw new Error(`expected ${expected}, got ${actual}`);
  }
}

import { classify, score, Signal } from "../src/policy";

type FixtureCase = Signal & { name: string; score: number; decision: "accept" | "review" };

const cases: FixtureCase[] = [
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
  equal(score(item), item.score);
  equal(classify(item), item.decision);
}
