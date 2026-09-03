# Deployment guide: adopt assessment-by-prompts in your course

> **Language:** [Español](guia-despliegue.md) · English

This guide walks you end to end with a **generic example** you can copy and adapt to
your own materials. It assumes neither your subject nor your stack: the method is
independent of the language or technology you teach. For the mechanical GitHub
detail (permissions, `pull_request_target`, branch protection) see
[`configuracion-github.md`](configuracion-github.md).

## Before you start: the contract change

You are changing **what is submitted and what is assessed**. Before: the code,
reviewed by PR. Now: the **process** —the prompts the student directed at the AI,
their screenshots, and a final technical *blueprint*—, with the code as a coherence
anchor. Communicate this contract change on day one; the usual resistance disappears
once students understand that **AI is not banned, its use is assessed**.

---

## Generic example (adapt it)

Take a fictional course, **"Data processing with Python"**, with a final project:
*"build a pipeline that ingests a large CSV, cleans it and publishes an aggregated
table"*. Replace the domain with yours (a REST API, an ML model, a dashboard, a
Solidity contract: it does not matter).

### Step 1 — Prepare the course repository

1. Create the repo `my-data-course` (students will **fork**, not PR).
2. Copy the PR-closing action and customize its message:
   ```bash
   mkdir -p .github/workflows
   cp github-actions/cerrar-prs.yml .github/workflows/
   cp templates/PULL_REQUEST_TEMPLATE.md .github/
   ```
3. Copy the template students will fill in and the submission guide:
   ```bash
   mkdir -p plantilla
   cp templates/PROMPTS.md plantilla/
   cp templates/guia-entregas.md plantilla/
   ```
4. In the course `README.md`, make the flow explicit (fork → `PROMPTS.md` →
   `git push`, no PR) and link the submission guide.

### Step 2 — Define the deliverable in `PROMPTS.md`

Require, at minimum:

- **3+ real prompts**, copied verbatim (typos included: they are the human trace).
- **One screenshot** per key prompt.
- **A final blueprint**: the technical summary the AI writes on the student's
  request (stack, architecture, decisions) proving they understand what they built.
- The resulting **code** in their fork.

> The rubric does **not** reward "the code works" (the AI generates it), but the
> **quality of the decomposition** into prompts, the **ability to iterate** on
> errors, the **coherence** prompts↔screenshot↔blueprint↔code and the
> **understanding** shown when explaining decisions. See the exact weights in the
> README ("Scoring Criteria") and the rationale in
> [`methodology.md`](methodology.md).

### Step 3 — Students work and submit

```
1. Fork the course repo
2. Work with any AI, documenting prompts WHILE working
3. Screenshot the important prompts
4. Ask the AI for the final blueprint
5. git push to their fork  (no PR to open)
```

### Step 4 — Automatic triage

Configure the list of forks and run the evaluator (it is a **triage signal**, not
the final grade):

```bash
cp scripts/config.example.py scripts/config.py   # config.py is NOT versioned
# edit ALUMNOS, REPO_ORIGINAL and RUTA_PROMPTS
python scripts/evaluar_prompts.py
```

It produces a report with a ranking and categories (highlight / normal / **review**
/ rejected). The evaluator is biased toward **recall**: it prefers to over-flag.
Thresholds live in `config.py` and are tuned to your course.

### Step 5 — Human review where it matters

Accept the `normal`/`highlight` cases without alerts directly. Spend your time on
the `review` ones: **2–3 oral questions about their own blueprint** quickly tell who
understood from who assembled without understanding. The machine prioritizes; **you
grade**.

---

## Adapting to your own materials

- **Different language/stack**: nothing changes. The deliverable is the process, not
  the code; it works the same for SQL, R, Rust or a notebook.
- **Group work**: each member documents **their** prompts in the same `PROMPTS.md`,
  identifying who did what.
- **No GitHub**: the same triptych (`PROMPTS.md` + screenshots + blueprint) is
  submitted through the LMS. Essential for anyone who does not want to expose their
  work publicly (see privacy).
- **Tuning rigor**: raise `min_prompts`/`min_palabras` in `CRITERIOS` for advanced
  courses; lower the "thin content" alert threshold for beginners.

## Privacy (mandatory)

The method publishes prompts and screenshots in public forks. **Informed consent** +
**private alternative** without penalty + instructing students to **redact personal
data** from screenshots + complying with GDPR/FERPA. Detail in
[`methodology.md`](methodology.md#privacy-and-consent).

---

## How to cite and attribute this work

If you use the method or the tools —in your course, a talk, a paper, or when
deriving your own version—, **cite the authorship** and **keep the attribution**:

**Academic citation (preprint):**

> Gutierrez Miranda, J. M. (2026). *Assessment by prompts: shifting assessment from
> product to process in programming education in the age of generative AI*.
> Preprint. TodoEconometria.
> https://github.com/TodoEconometria/evaluacion-prompts-ia

**Software / toolkit:** see [`CITATION.cff`](../CITATION.cff) (GitHub shows the
"Cite this repository" button). Author: **Juan Marcelo Gutierrez Miranda |
TodoEconometria**.

**MIT license:** you may use, modify and redistribute freely; the only condition is
to **keep the copyright notice and the attribution to the author** in copies and
derivatives. Do not remove the authorship headers from the scripts.
