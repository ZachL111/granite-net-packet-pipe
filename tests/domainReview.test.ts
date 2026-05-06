import * as assert from "node:assert/strict";
import { domainReviewLane, domainReviewScore } from "../src/domainReview";

const item = { signal: 67, slack: 28, drag: 18, confidence: 51 };
assert.equal(domainReviewScore(item), 159);
assert.equal(domainReviewLane(item), "ship");
