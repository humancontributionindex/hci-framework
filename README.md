# Human Contribution Index (HCI)

**An open framework for measuring scholarly agency in research — in the age of AI.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## The Problem

Universities, journals, and funding bodies face an urgent question: **How much of this research reflects genuine human intellectual agency?**

Current tools detect AI-generated text. The HCI goes further — it measures the depth of *scholarly agency* behind the work. Not whether a machine wrote the words, but whether a human was the architect of the thinking.

## What is the HCI?

The Human Contribution Index is a structured scoring framework with **5 dimensions** that capture the cognitive acts most characteristic of human researchers:

| Dimension | Weight | What It Measures |
|---|---|---|
| **Epistemic Agency** | 35% | Did the human identify a meaningful gap, formulate original questions, and direct the inquiry? |
| **Cognitive Transformation** | 25% | Does the author's thinking evolve through the work? Is there triangulation of evidence? |
| **Methodological Autonomy** | 20% | Did the human justify their research design and critically evaluate alternatives? |
| **Original Synthesis** | 15% | Are there new conceptual models or cross-theory integrations that transcend the sources? |
| **Metacognitive Oversight** | 5% | Is there an honest, reflective account of limitations and the research journey? |

The framework is built on a core distinction: the human is the **Architect** (designs the research — vision, questions, judgment) and AI is the **Builder** (executes tasks — drafting, formatting, searching). The HCI measures the quality of the architectural work.

### The Formula

Each dimension is scored 1–5 using behavioral anchors. The composite score is scaled to 0–100:

```
HCI = Σ(λⱼ × HCⱼ) / Σ(λⱼ) × 20
```

Where:
- `HCⱼ` = Dimension score (1–5 scale)
- `λⱼ` = Dimension weight (see table above)
- Since each dimension is scored 1–5, the effective range is 20–100

### Classification

| Score | Classification | Meaning |
|---|---|---|
| **80–100** | **High Agency** | The human author is clearly the intellectual architect of the work. |
| **60–79** | **Hybrid** | A mix of human-led inquiry and significant reliance on AI for core intellectual tasks. |
| **Below 60** | **Low Agency** | The work is likely a product of AI generation with minimal human intellectual contribution. |

## Quick Start

### Manual Scoring
Use the [detailed scoring rubric](rubric/dimensions.md) to assess a dissertation or research paper.

Score each dimension 1–5 using the behavioral anchors provided, then compute:

```python
scores = {
    "epistemic_agency": 4,
    "cognitive_transformation": 3,
    "methodological_autonomy": 4,
    "original_synthesis": 4,
    "metacognitive_oversight": 4
}
weights = {
    "epistemic_agency": 0.35,
    "cognitive_transformation": 0.25,
    "methodological_autonomy": 0.20,
    "original_synthesis": 0.15,
    "metacognitive_oversight": 0.05
}

weighted_sum = sum(scores[d] * weights[d] for d in scores)
total_weight = sum(weights.values())
hci_score = round((weighted_sum / total_weight) * 20)
print(f"HCI Score: {hci_score}/100")  # HCI Score: 75/100
```

### Automated Scoring
Try the free scorer at [humancontributionindex.com](https://humancontributionindex.com) — paste your research text and get an instant assessment.

### Python Calculator
Use the included [`hci_calculator.py`](hci_calculator.py) for batch scoring:

```bash
python hci_calculator.py
```

## Scoring Rubric

The full scoring rubric with detailed behavioral anchors and "fingerprints" (what to look for) for each dimension is available in [`rubric/dimensions.md`](rubric/dimensions.md).

## Use Cases

- **Universities:** Assess the authenticity of scholarly agency in dissertations and theses
- **Journal Editors:** Evaluate the depth of human contribution in submitted manuscripts
- **Funding Bodies:** Verify that funded research reflects genuine human intellectual work
- **Researchers:** Self-assess and demonstrate the human contribution in their own work

## Theoretical Foundation

The HCI is grounded in cognitive science and epistemology:

- **Epistemic Agency** draws on the cognitive distinction between problem-finding and problem-solving
- **Cognitive Transformation** draws on research into conceptual change and evidence-based reasoning
- **Methodological Autonomy** draws on theories of research design judgment and procedural decision-making
- **Original Synthesis** draws on research on analogical reasoning and conceptual combination
- **Metacognitive Oversight** draws on theories of metacognition, epistemic humility, and reflective practice

For the full theoretical development, see the [research paper](docs/theoretical-foundation.md).

## Contributing

We welcome contributions from researchers, educators, and practitioners. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Ways to contribute:
- **Improve the rubric:** Suggest clearer behavioral anchors or missing criteria
- **Disciplinary calibration:** Help adapt the framework for specific fields
- **Translation:** Make the rubric available in other languages
- **Validation data:** Share scored assessments to help validate the framework
- **Case studies:** Document your experience applying the HCI

## What changed in 0.2.0

This version introduces a significant evolution of the framework based on applied research:

- **Dimensions reconceptualized:** From measuring "what the human contributed" to measuring "scholarly agency" — how much the human was the architect of the thinking
- **Weights redistributed:** Epistemic Agency (asking the right questions) is now weighted highest at 35%
- **AI dependency factor removed:** The framework no longer penalizes AI use — it only measures whether the thinking is human
- **20–100 scoring scale:** Composite scores are now on a 20–100 scale instead of 0–5 (floor of 20 reflects that all dimensions have a minimum score of 1)
- **3-tier classification added:** High Agency / Hybrid / Low Agency for clear, actionable results
- **Standalone framework:** HCI is no longer positioned as a component of a larger CRQI system

The previous version is available at [tag v0.1.0](../../releases/tag/v0.1.0).

## Citation

If you use the HCI in your research, please cite:

```bibtex
@misc{hci-framework,
  title={The Human Contribution Index: A Framework for Measuring Scholarly Agency in Research},
  author={Macario, Simone and Casadio, Paolo and Chan, Paul},
  year={2026},
  url={https://github.com/humancontributionindex/hci-framework}
}
```

## License

This work is licensed under the [MIT License](LICENSE).

## Contact

- **Website:** [humancontributionindex.com](https://humancontributionindex.com/)
- **Discussions:** Use [GitHub Discussions](../../discussions) for questions and ideas
