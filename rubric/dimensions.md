# HCI Scoring Rubric

## How to Use This Rubric

For each of the five dimensions below, read the dissertation or research work and assign a score from 1 (Poor) to 5 (Excellent) using the behavioral anchors as guidance. Then estimate the AI Dependency Factor. Finally, compute the HCI score using the formula.

---

## Dimension 1: Creative Synthesis (λ = 0.25)

*Measures the ability to forge a new, meaningful whole from disparate, previously unrelated parts.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | The dissertation shows no evidence of synthesis across different ideas or fields. The work remains entirely within a single, narrow framework with no attempt to connect ideas from different sources. |
| **2 (Fair)** | The dissertation makes some simple connections between ideas, but these are obvious and do not generate new insights. The synthesis is superficial. |
| **3 (Average)** | The dissertation makes some connections to other fields, but these are superficial or commonplace. The integration does not lead to new insights. |
| **4 (Good)** | The dissertation demonstrates strong evidence of creative synthesis, connecting ideas from different fields in ways that generate new and valuable insights. |
| **5 (Excellent)** | The dissertation masterfully integrates concepts and methods from disparate fields to create a novel and powerful synthesis. The integration generates emergent insights that would not have been possible from a single disciplinary perspective. |

**What to look for:** Non-obvious cross-domain connections, integration of ideas from different intellectual domains, emergent insights from combining frameworks, novel analogies that illuminate the research problem.

---

## Dimension 2: Critical Judgment (λ = 0.20)

*Measures the ability to evaluate claims, weigh evidence, and make reasoned decisions while maintaining awareness of cognitive limitations and biases.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | The author accepts claims and evidence uncritically. There is no evidence of evaluating the strengths and weaknesses of different positions or methodological choices. |
| **2 (Fair)** | The author shows some evidence of critical thinking but it is inconsistent. Alternative viewpoints are occasionally acknowledged but not seriously engaged with. |
| **3 (Average)** | The author demonstrates a reasonable level of critical thinking. Key claims are supported with evidence, and some alternative perspectives are considered. However, the analysis lacks depth or nuance. |
| **4 (Good)** | The author demonstrates strong critical judgment. Claims are rigorously evaluated, alternative explanations are seriously considered, and methodological choices are well-justified. The author shows awareness of the limits of their own work. |
| **5 (Excellent)** | The author demonstrates exceptional critical judgment throughout. There is evidence of deep metacognitive awareness, epistemic humility, and sophisticated engagement with competing perspectives. The author anticipates and addresses potential criticisms proactively. |

**What to look for:** Metacognitive awareness, epistemic humility, nuanced engagement with alternative perspectives, evidence-based reasoning, acknowledgment of limitations, proactive addressing of counter-arguments.

---

## Dimension 3: Conceptual Direction (λ = 0.25)

*Measures the intellectual leadership involved in framing a problem and setting a research agenda.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | The research questions are derivative and show no evidence of independent thought. The problem framing follows a template with no original perspective on why this research matters. |
| **2 (Fair)** | The research questions are a minor variation on existing questions. There is some evidence of independent problem framing, but the overall direction is heavily guided by prior work. |
| **3 (Average)** | The research questions are reasonable and show some evidence of independent thought in their framing. The rationale for the research direction is adequate but not compelling. |
| **4 (Good)** | The research questions demonstrate clear intellectual leadership. The problem is framed in a way that reveals a deep understanding of the field and a clear vision for where it needs to go. |
| **5 (Excellent)** | The research questions are exceptionally original and demonstrate visionary intellectual leadership. The problem framing itself is a significant contribution, revealing connections and gaps that others have missed. |

**What to look for:** Originality of research questions, quality of problem framing, evidence of independent intellectual agenda-setting, clarity of vision, ability to identify gaps others have missed.

---

## Dimension 4: Ethical Reasoning (λ = 0.15)

*Measures engagement with the moral and societal implications of the research.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | The dissertation ignores or dismisses the ethical implications of the research. There is no evidence of ethical consideration beyond minimal compliance. |
| **2 (Fair)** | The dissertation includes a standard, pro-forma ethics statement but no deeper engagement with the ethical dimensions of the work. Ethics is treated as a box-ticking exercise. |
| **3 (Average)** | The dissertation demonstrates an awareness of the key ethical issues and addresses them adequately. There is evidence of genuine consideration, but the analysis does not go beyond the obvious. |
| **4 (Good)** | The dissertation demonstrates a strong and nuanced engagement with the ethical dimensions of the research. The author considers the impact on multiple stakeholders and navigates ethical tensions thoughtfully. |
| **5 (Excellent)** | The dissertation demonstrates an exceptional and sophisticated engagement with ethics. The author proactively identifies non-obvious ethical considerations, engages with them in depth, and demonstrates a strong sense of moral responsibility for the research and its consequences. |

**What to look for:** Depth of ethical engagement beyond compliance, consideration of multiple stakeholders, navigation of ethical tensions, proactive identification of ethical implications, moral responsibility.

---

## Dimension 5: Scholarly Voice (λ = 0.15)

*Measures the holistic expression of an integrated mind that has deeply engaged with the material and synthesized it into a unique, authentic perspective.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | The writing is generic, lacking a distinct authorial presence. The text reads as if it could have been written by anyone (or by AI). There is no sense of a unique intellectual perspective. |
| **2 (Fair)** | The writing is clear but lacks a strong authorial voice. The author reports findings and ideas competently but without conveying a sense of personal intellectual investment or ownership. |
| **3 (Average)** | The writing shows some evidence of an emerging authorial voice. There are moments of distinctive perspective, but they are inconsistent. The overall tone is competent but not compelling. |
| **4 (Good)** | The writing demonstrates a clear and confident authorial voice. The author takes ownership of their arguments, writes with conviction, and engages the reader in a compelling intellectual narrative. |
| **5 (Excellent)** | The writing demonstrates an exceptional scholarly voice. There is a powerful sense of intellectual ownership, a nuanced and sophisticated use of language, and a palpable sense of genuine curiosity and commitment. The text could only have been written by this specific researcher. |

**What to look for:** Distinctive authorial presence, intellectual ownership, nuanced language use, effective reader engagement, sense of genuine curiosity, confidence in argumentation, authentic perspective.

---

## AI Dependency Factor (AIᵈ)

After scoring the five dimensions, estimate the AI Dependency Factor based on the level of AI involvement in the research:

| AIᵈ Range | Description | Examples |
|---|---|---|
| 0.0 – 0.2 | AI as minor tool | Spell-check, formatting, grammar tools |
| 0.2 – 0.4 | AI for specific tasks with human oversight | Literature search assistance, data cleaning, reference management |
| 0.4 – 0.6 | Substantial AI assistance with human direction | AI-assisted drafting with significant revision, AI-supported analysis with human interpretation |
| 0.6 – 0.8 | Heavy AI reliance with limited human modification | AI-generated sections with minor editing, AI-driven analysis with minimal human oversight |
| 0.8 – 1.0 | AI-generated with minimal human contribution | Predominantly AI-written with cosmetic human edits |

---

## Computing the HCI Score

```
HCI = Σ(λⱼ × HCⱼ) × (1 - AIᵈ)
```

### Step-by-step:

1. Multiply each dimension score by its weight
2. Sum the weighted scores
3. Multiply by (1 - AI Dependency Factor)

### Example Calculation

| Dimension | Score | Weight | Weighted |
|---|---|---|---|
| Creative Synthesis | 4 | 0.25 | 1.00 |
| Critical Judgment | 4 | 0.20 | 0.80 |
| Conceptual Direction | 3 | 0.25 | 0.75 |
| Ethical Reasoning | 4 | 0.15 | 0.60 |
| Scholarly Voice | 4 | 0.15 | 0.60 |
| **Weighted Sum** | | | **3.75** |

With AIᵈ = 0.15 (minor AI tool use):

```
HCI = 3.75 × (1 - 0.15) = 3.75 × 0.85 = 3.19
```

### Interpretation

| HCI Score | Interpretation |
|---|---|
| 4.0 – 5.0 | Exceptional human contribution — strong evidence of authentic intellectual engagement across all dimensions |
| 3.0 – 4.0 | Strong human contribution — clear evidence of genuine human intellectual work |
| 2.0 – 3.0 | Moderate human contribution — some dimensions show authentic engagement, others are weak |
| 1.0 – 2.0 | Limited human contribution — significant concerns about the authenticity of intellectual engagement |
| Below 1.0 | Minimal human contribution — heavy AI dependency has substantially diminished the human intellectual contribution |
