# Cheating Detection (anti-cheating)

> **Language:** [Español](anti-trampa.md) · English

This document details the signals `evaluar_prompts.py` uses to flag submissions that
deserve a **human review**. None of these signals is a verdict: they are cheap heuristics
to decide *where* to look, not *what grade* to assign.

## Philosophy: signal, not sentence

The premise of the system is that assessing the process (the prompts) is more robust than
assessing the product (the code) when AI can generate the product. But a determined
student can also fabricate a plausible process. So the goal is not an infallible detector
—there is none— but to **raise the cost of cheating** and **focus the instructor's
attention** on the handful of doubtful cases.

## Implemented signals

### 1. "Too clean" prompts

Real prompts from someone learning carry human traces: typos (*"how do i geT..."*),
informal language (*"help me with..."*), basic questions (*"what is spark"*). A student who
copies the code first and writes the prompts afterwards tends to produce neat, very
technical, error-free prompts.

**How it is measured.** The script counts occurrences of a small formal lexicon against an
informal one. If formal exceeds informal by more than double and there are ≥3 prompts, it
raises the `SUSPICIOUS` alert.

**Limit.** It is trivial to evade (just ask the AI to add typos). Treat it as an invitation
to ask in person, not as proof.

### 2. Copy of the instructor's example

If the assignment gives an example with a concrete domain (countries X, Y, Z; a specific
dataset), a submission that reuses exactly that domain suggests shallow copying rather than
original work. The submission's topic/entities are compared with the example's.

### 3. Incoherent blueprint

The *blueprint* is the technical summary the AI generates at the end. If it describes
technologies, architecture, or decisions that **do not appear** in the submitted code, the
submission is internally inconsistent — a good sign the pieces were assembled without being
understood.

### 4. Thin content

Fewer than ~300 words in `PROMPTS.md` (or very few prompts) indicates insufficient effort
to document a real process. It raises the `REVIEW` alert.

## Cross-coherence: the real defense

No single signal is strong. Real detection lives in the **coherence across the four
sources**:

```
prompts  ⇄  screenshots  ⇄  blueprint  ⇄  code
```

Fabricating a case that is coherent across all four at once —the prompts explain the code,
the screenshots match the prompts, the blueprint describes what the code actually does—
costs almost as much as having done the work. That is the point.

## What it does NOT detect

- A student who genuinely uses the AI skillfully yet understands little: the system rewards
  the documented process, and that is deliberate (the goal is to teach good AI use).
- Collusion between students with different domains and rewritten prompts.
- False positives from style: a naturally formal student may trigger `SUSPICIOUS`. That is
  why the alert leads to **review**, not to **failure**.

## Recommended use

1. Run the script and sort by category.
2. Accept the `NORMAL`/`HIGHLIGHT` cases without alerts directly.
3. Spend manual review on the `REVIEW` and `SUSPICIOUS` cases: 2–3 oral questions about
   their own blueprint usually suffice to tell who understood from who copied.

See also: [`methodology.md`](methodology.md) · [`faq.en.md`](faq.en.md).
