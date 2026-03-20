# AlignLab - Open-Source RLHF Toolkit for Underserved Domains

**Building affordable, domain-specific RLHF datasets using multi-agent systems.**
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## The Problem

Reinforcement Learning from Human Feedback (RLHF) is essential for aligning AI models to human preferences. However, current RLHF services focus on large, general-purpose models and English-only tasks. This leaves critical gaps:

- **Small models** (7B-13B) lack affordable alignment pipelines
- **Secure code generation** is neglected - security-focused preference data is scarce
- **Educational AI** needs pedagogical alignment, not just chat
- **Low-resource languages** (e.g., Yoruba, Swahili, Pidgin) are almost unsupported
- **Agentic behavior** (tool use, planning) requires trajectory-level feedback

Startups, researchers, and EdTech companies struggle to find RLHF providers that understand their niche. Existing solutions are either too expensive or too generic.

---

## Our Solution

**AlignLab** is an open-source framework that demonstrates how to bootstrap high-quality preference datasets for these underserved areas using a multi-agent hive (XANDER). It combines:

- **Automated candidate generation** via specialist agents (security scanner, teacher, trader)
- **Structured preference pair creation** (chosen vs rejected) in JSONL format
- **Extensible pipeline** for adding human review later
- **Integration with existing tools** (web3-security-scout, xander-hive-framework)

Our goal: show that domain-specific RLHF can be done cost-effectively, and invite collaborators to scale this into a full service.

---

## How It Works (High Level)

1. **Define the domain** - e.g., secure Python code, Socratic tutoring, Yoruba QA.
2. **Generate candidate responses** - XANDER agents produce multiple outputs per prompt.
3. **Automatic labeling** - Use rule-based or specialist agents to pre-label preferences (e.g., security score, pedagogical rubric).
4. **Human review (optional)** - Export for expert validation.
5. **Dataset output** - Clean JSONL ready for RLHF fine-tuning (PPO/DPO).

See `src/generate_preferences.py` for a working example.

---

## Current Focus Areas

- ✅ **SecureCode RLHF** – Preference pairs for secure vs vulnerable code (tie to `web3-security-scout`)
- ✅ **EduTutor RLHF** – Tutor responses that scaffold vs give direct answers (tie to `prof` agent)
- 🔜 **SmallModel Starter** – General chat for 7B–13B models
- 🔜 **LangAlign** – Low-resource language QA pairs
- 🔜 **Agentic RLHF** – Multi-step tool use trajectories

## Dataset Quality Metrics

AlignLab includes a quality scorer (`alignlab.quality`) that evaluates:

- Lexical diversity of chosen/rejected responses
- Prompt/reponse length distributions
- Domain balance
- Warnings for potential issues (too short prompts, low diversity, imbalance)

Generate a dataset and receive a `.quality.json` report automatically.

---

## Repository Structure

```
alignlab/
├── README.md
├── LICENSE (MIT)
├── requirements.txt
├── setup.py
├── src/
│   └── alignlab/
│       ├── __init__.py
│       ├── cli.py                 # unified CLI: generate & score
│       ├── generate_preferences.py
│       └── quality.py            # dataset quality metrics
├── data/
│   └── samples/
│       ├── secure_code_preferences.jsonl   # 100 examples
│       └── edu_tutor_preferences.jsonl    # 100 examples
├── docs/
│   ├── architecture.md
│   └── quality.md
├── .github/
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
└── landing.html   # simple GitHub Pages site
```

---

## Quickstart (Generate Sample Dataset)

```bash
git clone https://github.com/GBOYEE/alignlab.git
cd alignlab
pip install -r requirements.txt
python -m alignlab.cli generate --domain secure_code --num 10 --output data/samples/secure_code_preferences.jsonl
```

This will produce a JSONL file where each line is:

```json
{
  "prompt": "Write a Python function that withdraws ETH from a smart contract...",
  "chosen": "secure implementation with checks",
  "rejected": "vulnerable implementation with reentrancy",
  "domain": "secure_code",
  "generator": "hive_agent"
}
```

A quality report will be written alongside: `data/samples/secure_code_preferences.quality.json`.

To score an existing dataset:

```bash
python -m alignlab.cli score --input data/samples/secure_code_preferences.jsonl
```

---

## Integration with Existing Projects

- **web3-security-scout**: Provides vulnerability patterns to auto-label insecure code.
- **xander-hive-framework**: Supplies the multi-agent orchestration for response generation and consensus.

This repo demonstrates how to turn a general agent framework into a domain-specific RLHF pipeline.

---

## Roadmap

- [ ] Expand sample datasets to 1k+ examples per domain
- [ ] Add human review UI (Label Studio integration)
- [ ] Publish case studies: fine-tuning a 7B model with our dataset
- [ ] Add African language samples (Yoruba, Pidgin)
- [ ] Implement agentic trajectory collection

---

## Contributing

We welcome contributions! Please read `CONTRIBUTING.md` and the `CODE_OF_CONDUCT.md`. Issues and PRs are open for:

- New domain datasets
- Improved scoring heuristics
- Documentation and translations
- UI for human review

---

## License

MIT - see `LICENSE` for details.

---

## Contact & Collaboration

Interested in piloting RLHF for your domain? Open an issue or reach out via Calendly on our landing page. Let's build the future of accessible AI alignment together.
