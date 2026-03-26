# HCI Scoring Rubric (0.2.0)

## How to Use This Rubric

For each of the five dimensions below, read the research work and assign a score from 1 (Poor) to 5 (Excellent) using the behavioral anchors as guidance. Then compute the HCI score using the formula at the bottom.

The HCI assesses **scholarly agency** — the researcher's demonstrated capacity to be the intellectual architect of their work. For each dimension, we describe "fingerprints" to look for: the moments where human judgment, creativity, and critical thinking are most visible.

---

## Dimension 1: Epistemic Agency (λ = 0.35)

*The foundational act of scholarship — identifying a meaningful gap and formulating original research questions. This is weighted highest because asking the right questions is more important than having polished answers.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | No original research gap identified. Research questions are generic, template-driven, or directly copied from existing studies with no independent framing. |
| **2 (Fair)** | A minor gap is identified, but questions closely follow existing work with little independence. The problem framing adds minimal novelty. |
| **3 (Average)** | A reasonable gap is identified with some independent formulation of research questions. The rationale is adequate but not compelling. |
| **4 (Good)** | A clear and novel research gap is articulated. Research questions are precise, insightful, and demonstrate deep understanding of the field. |
| **5 (Excellent)** | Exceptional identification of a critical juncture or overlooked gap that reframes the field. Visionary question formulation that reveals connections and problems others have missed. |

**Fingerprints to look for:** Articulation of a "critical juncture" in the field, novel research gap that goes beyond obvious next-steps, precise and insightful research questions, courage to tackle a difficult or unconventional problem, a clear "why now?" rationale.

---

## Dimension 2: Cognitive Transformation (λ = 0.25)

*Evidence that the author's thinking evolved through engagement with the research process — not just reporting findings, but being changed by them.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | No evidence of thinking evolving. Findings are accepted at face value without integration. The literature review reads as a list, not a conversation. |
| **2 (Fair)** | Some engagement with multiple sources, but no meaningful transformation of understanding. Ideas are juxtaposed rather than integrated. |
| **3 (Average)** | Reasonable triangulation of evidence with some grappling with conflicting findings. The author engages with complexity but doesn't fully resolve it. |
| **4 (Good)** | Strong evidence of thinking evolving through the work. Multiple evidence sources are integrated with nuance. Conflicting findings are addressed directly. |
| **5 (Excellent)** | Exceptional cognitive transformation visible throughout. The author's understanding demonstrably deepens and shifts as they engage with evidence. The reader can trace the intellectual journey. |

**Fingerprints to look for:** Thinking that visibly evolves over the course of the document, triangulation of multiple and diverse evidence sources, genuine grappling with conflicting or surprising findings, moments where the author revises their position based on evidence.

---

## Dimension 3: Methodological Autonomy (λ = 0.20)

*The researcher's ownership of and justification for their research design — evidence that methodological choices were made deliberately, not by default.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | No rationale for research design. Methodology appears chosen by default, convenience, or supervisor directive with no evidence of independent design thinking. |
| **2 (Fair)** | A basic rationale is given, but no critical evaluation of alternatives or limitations. The "why this method?" question is not convincingly answered. |
| **3 (Average)** | Adequate justification with some awareness of methodological trade-offs. Alternatives are mentioned but not deeply evaluated. |
| **4 (Good)** | Well-justified methodology with critical discussion of strengths, weaknesses, and alternatives considered. The researcher demonstrates ownership of the design. |
| **5 (Excellent)** | Exceptional methodological autonomy. Novel analytical tools or frameworks are developed. Every design choice is rigorously justified. The methodology itself is a contribution. |

**Fingerprints to look for:** Clear and explicit rationale for every design choice, development of novel analytical tools or frameworks, critical discussion of the methodology's strengths and weaknesses, evidence that alternatives were genuinely considered and rejected for specific reasons.

---

## Dimension 4: Original Synthesis (λ = 0.15)

*The creation of new wholes from existing parts — arguments, models, or frameworks that transcend the individual sources they draw upon.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | No synthesis. The work is a collection of summaries arranged sequentially with no integrative argument or framework. |
| **2 (Fair)** | Simple juxtaposition of ideas with no emergent insight from the combination. Sources are placed side by side but not woven together. |
| **3 (Average)** | Some integration across sources, but the synthesis is predictable and does not generate new understanding. The whole equals the sum of its parts. |
| **4 (Good)** | Strong original synthesis. New conceptual models are created, or theories from different fields are integrated in ways that produce valuable new understanding. |
| **5 (Excellent)** | Masterful synthesis producing a holistic argument that is genuinely more than the sum of its parts. Creates new conceptual territory that did not exist before the integration. |

**Fingerprints to look for:** Creation of new conceptual models or frameworks, integration of theories from different fields, development of a holistic argument that transcends its sources, novel analogies that illuminate the research problem, emergent insights that no single source provides.

---

## Dimension 5: Metacognitive Oversight (λ = 0.05)

*Honest self-awareness about the research process, its limitations, and the researcher's own learning journey.*

| Score | Anchor |
|---|---|
| **1 (Poor)** | No discussion of limitations or reflection on the research process. The work presents conclusions as if they are beyond question. |
| **2 (Fair)** | A perfunctory limitations section exists, but it reads as an afterthought with no genuine self-awareness or honesty about the research journey. |
| **3 (Average)** | An adequate limitations discussion is present, but it lacks depth or genuine honesty about the challenges, surprises, and pivots in the research process. |
| **4 (Good)** | A thoughtful and honest discussion of limitations, combined with a transparent account of research decisions and their rationale. |
| **5 (Excellent)** | Exceptional metacognitive awareness. A candid, reflective account of the learning journey — including what surprised the researcher, what they would do differently, and what they still don't know. Genuine intellectual humility. |

**Fingerprints to look for:** Honest and thoughtful discussion of limitations, transparent account of the research process including dead ends, reflective summary of what the researcher learned, acknowledgment of what remains unknown, evidence of intellectual humility.

---

## Computing the HCI Score

Each dimension is scored 1–5. The composite is scaled to 0–100:

```
HCI = (Σ(λⱼ × HCⱼ) / Σ(λⱼ)) × 20
```

### Step-by-step:

1. Multiply each dimension score by its weight
2. Sum the weighted scores
3. Divide by the sum of all weights (normalizes for any unscored dimensions)
4. Multiply by 20 to scale to 0–100

### Example Calculation

| Dimension | Score | Weight | Weighted |
|---|---|---|---|
| Epistemic Agency | 4 | 0.35 | 1.40 |
| Cognitive Transformation | 3 | 0.25 | 0.75 |
| Methodological Autonomy | 4 | 0.20 | 0.80 |
| Original Synthesis | 4 | 0.15 | 0.60 |
| Metacognitive Oversight | 3 | 0.05 | 0.15 |
| **Weighted Sum** | | **1.00** | **3.70** |

```
HCI = (3.70 / 1.00) × 20 = 74 / 100 → Hybrid
```

### Classification

| HCI Score | Classification | Description |
|---|---|---|
| **80–100** | **High Agency** | The human author is clearly the intellectual architect of the work. |
| **60–79** | **Hybrid** | A mix of human-led inquiry and significant reliance on AI for core intellectual tasks. |
| **Below 60** | **Low Agency** | The work is likely a product of AI generation with minimal human intellectual contribution. |
