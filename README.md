# Human Contribution Index (HCI)

**An open framework for measuring authentic human intellectual contribution in research — in the age of AI.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## The Problem

Universities, journals, and funding bodies face an urgent question: **How much of this research is genuinely human?**

Current tools detect AI-generated text. The HCI goes further — it measures the depth of *human intellectual engagement* behind the work, not just whether a machine wrote the words.

## What is the HCI?

The Human Contribution Index is a structured scoring framework with **5 dimensions** that capture the cognitive acts most characteristic of human researchers and most resistant to AI replication:

| Dimension | Weight | What It Measures |
|---|---|---|
| **Conceptual Direction** | 0.25 | Did the human identify the problem, frame the questions, and direct the inquiry? |
| **Creative Synthesis** | 0.25 | Are the connections and insights non-obvious? Do they require domain expertise? |
| **Critical Judgment** | 0.20 | Did the human evaluate alternatives and make reasoned selections? |
| **Ethical Reasoning** | 0.15 | Did the human navigate ethical considerations and take responsibility? |
| **Scholarly Voice** | 0.15 | Is there a distinctive perspective and authentic argumentation? |

### The Formula

```
HCI = Σ(λⱼ × HCⱼ) × (1 - AIᵈ)
```

Where:
- `HCⱼ` = Human contribution score for dimension j (1-5 scale)
- `λⱼ` = Dimension weight (see table above)
- `AIᵈ` = AI dependency factor (0.0 to 1.0)

### AI Dependency Factor (AIᵈ)

| Range | Description |
|---|---|
| 0.0 – 0.2 | AI used as minor tool (spell-check, formatting) |
| 0.2 – 0.4 | AI used for specific tasks with human oversight (literature search, data cleaning) |
| 0.4 – 0.6 | Substantial AI assistance with human direction (drafting, analysis) |
| 0.6 – 0.8 | Heavy AI reliance with limited human modification |
| 0.8 – 1.0 | AI-generated with minimal human contribution |

## Quick Start

### Manual Scoring
Use the [detailed scoring rubric](rubric/hci-rubric.md) to assess a dissertation or research paper. Score each dimension 1-5 using the behavioral anchors provided, estimate the AI dependency factor, then compute:

```python
# Example: A strong dissertation with minor AI tool use
scores = {
    "conceptual_direction": 4,
    "creative_synthesis": 3,
    "critical_judgment": 4,
    "ethical_reasoning": 4,
    "scholarly_voice": 4
}
weights = {
    "conceptual_direction": 0.25,
    "creative_synthesis": 0.25,
    "critical_judgment": 0.20,
    "ethical_reasoning": 0.15,
    "scholarly_voice": 0.15
}
ai_dependency = 0.1  # Minor AI tool use

weighted_sum = sum(scores[d] * weights[d] for d in scores)
hci_score = weighted_sum * (1 - ai_dependency)
print(f"HCI Score: {hci_score:.2f}")  # HCI Score: 3.42
```

## Scoring Rubric

The full scoring rubric with detailed behavioral anchors for each dimension is available in [`rubric/hci-rubric.md`](rubric/hci-rubric.md).

## Part of the CRQI Framework

The HCI is the central component of the **Composite Research Quality Index (CRQI)**, a broader framework that integrates human contribution assessment with traditional research quality dimensions (Originality, Generativity, Methodological Rigor, and Impact):

```
CRQI = [w₁(OI) + w₂(GI) + w₃(MRI) + w₄(II)] × HCI
```

The HCI serves as a **multiplicative factor** — reflecting the position that authentic human contribution is not just one dimension of quality, but the foundational element that gives value to all others.

The full CRQI framework will be published in a separate repository.

## Use Cases

- **Universities:** Assess the authenticity of human engagement in dissertations and theses
- **Journal Editors:** Evaluate the depth of human contribution in submitted manuscripts
- **Funding Bodies:** Verify that funded research reflects genuine human intellectual work
- **Researchers:** Self-assess and demonstrate the human contribution in their own work

## Theoretical Foundation

The HCI is grounded in cognitive science and epistemology:

- **Creative Synthesis** draws on research on analogical reasoning and conceptual combination
- **Critical Judgment** draws on theories of metacognition, epistemic humility, and reasoning under uncertainty
- **Conceptual Direction** draws on the cognitive distinction between problem-finding and problem-solving
- **Ethical Reasoning** draws on cognitive models of moral judgment and scientific responsibility
- **Scholarly Voice** reflects an integrated cognitive signature of authentic authorial engagement

For the full theoretical development, see the [research paper](docs/theoretical-foundation.md).

## Contributing

We welcome contributions from researchers, educators, and practitioners. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Ways to contribute:
- **Improve the rubric:** Suggest clearer behavioral anchors or missing criteria
- **Disciplinary calibration:** Help adapt the framework for specific fields
- **Translation:** Make the rubric available in other languages
- **Validation data:** Share scored assessments to help validate the framework
- **Case studies:** Document your experience applying the HCI

## Citation

If you use the HCI in your research, please cite:

```bibtex
@misc{hci-framework,
  title={The Human Contribution Index: A Framework for Measuring Authentic Human Intellectual Contribution in Research},
  author={[Author Name]},
  year={2026},
  url={https://github.com/humancontributionindex/hci-framework}
}
```

## License

This work is licensed under the [MIT License](LICENSE).

## Contact

- **Website:** [coming soon]
- **Email:** [coming soon]
- **Discussions:** Use [GitHub Discussions](../../discussions) for questions and ideas
