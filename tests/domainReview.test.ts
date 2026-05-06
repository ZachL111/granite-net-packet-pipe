function equal<T>(actual: T, expected: T): void {
  if (actual !== expected) {
    throw new Error(`expected ${expected}, got ${actual}`);
  }
}

import { domainReviewLane, domainReviewScore } from "../src/domainReview";

const item = { signal: 67, slack: 28, drag: 18, confidence: 51 };
equal(domainReviewScore(item), 159);
equal(domainReviewLane(item), "ship");
