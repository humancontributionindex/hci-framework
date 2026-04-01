"""
Human Contribution Index (HCI) Calculator — Framework 0.2.0

A simple tool to compute HCI scores from manual dimension ratings.
Scores are on a 20-100 scale with a three-tier classification.
(Floor of 20 because each dimension has a minimum score of 1.)
"""

# Dimension weights (0.2.0)
WEIGHTS = {
    "epistemic_agency": 0.35,
    "cognitive_transformation": 0.25,
    "methodological_autonomy": 0.20,
    "original_synthesis": 0.15,
    "metacognitive_oversight": 0.05,
}

DIMENSION_LABELS = {
    "epistemic_agency": "Epistemic Agency",
    "cognitive_transformation": "Cognitive Transformation",
    "methodological_autonomy": "Methodological Autonomy",
    "original_synthesis": "Original Synthesis",
    "metacognitive_oversight": "Metacognitive Oversight",
}


def calculate_hci(scores: dict) -> dict:
    """
    Calculate the Human Contribution Index score.

    Args:
        scores: Dictionary with dimension keys and scores (1-5).
                Keys: epistemic_agency, cognitive_transformation,
                      methodological_autonomy, original_synthesis,
                      metacognitive_oversight

    Returns:
        Dictionary with weighted scores, composite score (0-100),
        and classification tier.  Score range is 20-100.
    """
    for dim, score in scores.items():
        if dim not in WEIGHTS:
            raise ValueError(f"Unknown dimension: {dim}")
        if not 1 <= score <= 5:
            raise ValueError(
                f"Score for {dim} must be between 1 and 5, got {score}"
            )

    if len(scores) != 5:
        missing = set(WEIGHTS.keys()) - set(scores.keys())
        raise ValueError(f"Missing dimensions: {missing}")

    weighted = {dim: scores[dim] * WEIGHTS[dim] for dim in scores}
    weighted_sum = sum(weighted.values())
    total_weight = sum(WEIGHTS.values())  # 1.0 today; kept for safety if weights change
    normalized = weighted_sum / total_weight
    hci_score = round(normalized * 20)

    return {
        "weighted_scores": weighted,
        "weighted_sum": round(weighted_sum, 2),
        "hci_score": hci_score,
        "tier": classify(hci_score),
    }


def classify(score: int) -> dict:
    """Return the classification tier for a given HCI score."""
    if score >= 80:
        return {
            "label": "High Agency",
            "description": "The human author is clearly the intellectual architect of the work.",
        }
    if score >= 60:
        return {
            "label": "Hybrid",
            "description": "A mix of human-led inquiry and significant reliance on AI for core intellectual tasks.",
        }
    return {
        "label": "Low Agency",
        "description": "The work is likely a product of AI generation with minimal human intellectual contribution.",
    }


# --- Example usage ---
if __name__ == "__main__":
    example_scores = {
        "epistemic_agency": 4,
        "cognitive_transformation": 3,
        "methodological_autonomy": 4,
        "original_synthesis": 4,
        "metacognitive_oversight": 4,
    }

    result = calculate_hci(example_scores)

    print("=== Human Contribution Index (HCI 0.2.0) ===\n")
    print("Dimension Scores:")
    for dim, score in example_scores.items():
        label = DIMENSION_LABELS[dim]
        weight_pct = f"{WEIGHTS[dim] * 100:.0f}%"
        print(
            f"  {label} ({weight_pct}): {score}/5 "
            f"(weighted: {result['weighted_scores'][dim]:.2f})"
        )
    print(f"\nHCI Score: {result['hci_score']}/100")
    print(f"Classification: {result['tier']['label']}")
    print(f"  {result['tier']['description']}")
