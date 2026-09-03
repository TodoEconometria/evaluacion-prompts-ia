# Frequently Asked Questions (FAQ)

> **Language:** [Español](faq.md) · English

### Can students lie in their prompts?

They can, but keeping fabricated prompts, screenshots, blueprint and code coherent is
costly. The system looks for **inconsistencies** across those four sources (see
[`anti-cheating.md`](anti-cheating.md)). Fabricating a coherent case costs almost as much
as doing the work.

### What if a student does not use AI?

They document their process anyway: Google searches, StackOverflow, documentation, trial
and error. The `PROMPTS.md` format is the same; what is assessed is the **reasoning**, not
the specific tool.

### How do I handle students without a GitHub account?

They need to create one: it is part of professional literacy. As an alternative, the same
structure (`PROMPTS.md` + screenshots + blueprint) can be submitted through the virtual
classroom / LMS for those who cannot or do not want to expose their work publicly (see
privacy below).

### Does it work for group work?

Yes. Each member documents **their** prompts in the same `PROMPTS.md`, identifying who did
what. Individual contribution stays traceable within the collective work.

### Is the script's grade the final grade?

No. It is a **triage signal** to sort submissions and flag the doubtful ones. The final
grade is the instructor's; the weights are editable in `config.py`. See "Scoring Criteria"
in the README.

### Isn't it unfair to publish students' work?

That is why informed consent and a private alternative are **mandatory**. No one should be
forced to expose their work. See the privacy section in
[`methodology.md`](methodology.md#privacy-and-consent) (GDPR / FERPA).

### Does the cheating detector give false positives?

Yes, and on purpose it prefers to over-flag (send to review) rather than under-flag. A
student with a formal style may trigger the `SUSPICIOUS` alert without having copied. That
is why the alert leads to a **conversation**, not an automatic penalty.

### Can I use this outside programming?

The principle —assessing the thinking process rather than the deliverable the AI can
generate— is general. The concrete implementation (forks, `PROMPTS.md`, technical
blueprint) is designed for technical courses; adapting it to essays or design means
changing the evidence format, not the philosophy.

### Where is the academic grounding?

In [`methodology.md`](methodology.md) and the README references (authentic assessment,
Wiggins 1990; evaluative judgement, Tai et al. 2018; academic integrity and ChatGPT,
Cotton et al. 2024). The full whitepaper is in `paper/preprint.pdf`.
