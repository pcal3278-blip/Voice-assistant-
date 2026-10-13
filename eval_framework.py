from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class EvalMetrics:
    success: float
    reliability: float
    latency: float
    cost: float
    satisfaction: float
    core_regression_pass_rate: float


class PromotionEvaluator:
    """Deterministic evaluator for model promotion decisions.

    Metric values are expected on a 0-100 scale.
    """

    WEIGHTS: Dict[str, float] = {
        "success": 0.40,
        "reliability": 0.20,
        "latency": 0.15,
        "cost": 0.10,
        "satisfaction": 0.15,
    }

    def composite_score(self, metrics: EvalMetrics) -> float:
        return round(
            (metrics.success * self.WEIGHTS["success"])
            + (metrics.reliability * self.WEIGHTS["reliability"])
            + (metrics.latency * self.WEIGHTS["latency"])
            + (metrics.cost * self.WEIGHTS["cost"])
            + (metrics.satisfaction * self.WEIGHTS["satisfaction"]),
            2,
        )

    def promotion_decision(self, baseline: EvalMetrics, candidate: EvalMetrics) -> Dict[str, object]:
        baseline_score = self.composite_score(baseline)
        candidate_score = self.composite_score(candidate)
        delta = round(candidate_score - baseline_score, 2)

        checks = {
            "core_regression_100": candidate.core_regression_pass_rate == 100.0,
            "composite_delta_at_least_3": delta >= 3.0,
            "reliability_non_regression": candidate.reliability >= baseline.reliability,
            "rollback_path_available": True,
        }

        approved = all(checks.values())
        return {
            "approved": approved,
            "baseline_score": baseline_score,
            "candidate_score": candidate_score,
            "delta": delta,
            "checks": checks,
        }
