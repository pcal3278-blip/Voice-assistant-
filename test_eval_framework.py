import unittest

from eval_framework import EvalMetrics, PromotionEvaluator


class TestPromotionEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = PromotionEvaluator()

    def test_composite_score(self):
        metrics = EvalMetrics(
            success=95,
            reliability=96,
            latency=90,
            cost=85,
            satisfaction=92,
            core_regression_pass_rate=100,
        )
        self.assertEqual(self.evaluator.composite_score(metrics), 93.0)

    def test_promotion_approved(self):
        baseline = EvalMetrics(90, 94, 88, 80, 89, 100)
        candidate = EvalMetrics(95, 95, 92, 85, 93, 100)
        decision = self.evaluator.promotion_decision(baseline, candidate)
        self.assertTrue(decision["approved"])

    def test_promotion_rejected_when_regression_fails(self):
        baseline = EvalMetrics(90, 95, 88, 80, 89, 100)
        candidate = EvalMetrics(96, 94, 92, 85, 93, 95)
        decision = self.evaluator.promotion_decision(baseline, candidate)
        self.assertFalse(decision["approved"])
        self.assertFalse(decision["checks"]["core_regression_100"])
        self.assertFalse(decision["checks"]["reliability_non_regression"])


if __name__ == "__main__":
    unittest.main()
