"""
Human Contribution Index (HCI) Calculator

A simple tool to compute HCI scores from manual dimension ratings.
"""

# Dimension weights
WEIGHTS = {
    "conceptual_direction": 0.25,
    "creative_synthesis": 0.25,
    "critical_judgment": 0.20,
    "ethical_reasoning": 0.15,
    "scholarly_voice": 0.15,
}


def calculate_hci(scores: dict, ai_dependency: float = 0.0) -> dict:
    """
    Calculate the Human Contribution Index score.

    Args:
        scores: Dictionary with dimension names as keys and scores (1-5) as values.
                Keys: conceptual_direction, creative_synthesis, critical_judgment,
                      ethical_reasoning, scholarly_voice
        ai_dependency: AI dependency factor (0.0 to 1.0).
                       0.0 = no AI use, 1.0 = fully AI-generated.

    Returns:
        Dictionary with weighted scores, weighted sum, and final HCI score.
    """
    # Validate inputs
    for dim, score in scores.items():
        if dim not in WEIGHTS:
            raise ValueError(f"Unknown dimension: {dim}")
        if not 1 <= score <= 5:
            raise ValueError(f"Score for {dim} must be between 1 and 5, got {score}")

    if not 0.0 <= ai_dependency <= 1.0:
        raise ValueError(f"AI dependency must be between 0.0 and 1.0, got {ai_dependency}")

    if len(scores) != 5:
        missing = set(WEIGHTS.keys()) - set(scores.keys())
        raise ValueError(f"Missing dimensions: {missing}")

    # Calculate weighted scores
    weighted = {dim: scores[dim] * WEIGHTS[dim] for dim in scores}
    weighted_sum = sum(weighted.values())
    hci_score = weighted_sum * (1 - ai_dependency)

    return {
        "weighted_scores": weighted,
        "weighted_sum": round(weighted_sum, 2),
        "ai_dependency": ai_dependency,
        "hci_score": round(hci_score, 2),
    }


def interpret_hci(score: float) -> str:
    """Return a human-readable interpretation of the HCI score."""
    if score >= 4.0:
        return "Exceptional human contribution"
    elif score >= 3.0:
        return "Strong human contribution"
    elif score >= 2.0:
        return "Moderate human contribution"
    elif score >= 1.0:
        return "Limited human contribution"
    else:
        return "Minimal human contribution"


# --- Example usage ---
if __name__ == "__main__":
    example_scores = {
        "conceptual_direction": 4,
        "creative_synthesis": 3,
        "critical_judgment": 4,
        "ethical_reasoning": 4,
        "scholarly_voice": 4,
    }

    result = calculate_hci(example_scores, ai_dependency=0.15)

    print("=== Human Contribution Index (HCI) ===\n")
    print("Dimension Scores:")
    for dim, score in example_scores.items():
        label = dim.replace("_", " ").title()
        print(f"  {label}: {score}/5 (weighted: {result['weighted_scores'][dim]:.2f})")
    print(f"\nWeighted Sum: {result['weighted_sum']}")
    print(f"AI Dependency: {result['ai_dependency']}")
    print(f"HCI Score: {result['hci_score']}")
    print(f"Interpretation: {interpret_hci(result['hci_score'])}")
