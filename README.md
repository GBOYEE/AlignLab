# 🧪 AlignLab

> **RLHF dataset toolkit for underserved domains.** Build high-quality preference datasets for code security, African languages, ethics, and agentic behavior — affordably and without massive compute.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
- 🎯 **Why it exists:** RLHF shouldn't be limited to big English chatbots. We need alignment for secure code, low-resource languages, and specialized tasks.
- 📊 **What it does:** Tools to curate, annotate, and manage preference datasets — with built-in quality scoring and checkpointing.
- 🤝 **Who uses it:** Researchers, startups, and developers building custom-aligned models (7B–13B) who can't afford OpenAI-level RLHF pipelines.

---

## 🎯 Key Use Cases

| Domain | What AlignLab Solves |
|--------|----------------------|
| **Secure Code** | Gather preferences for safe vs. vulnerable code (connects to `VulnFix-Agent`, `web3-security-scout`) |
| **African Languages** | Build alignment datasets for Yoruba, Pidgin, Swahili, Hausa, Igbo (powered by `AfriCode-Aligner`) |
| **Ethics** | Curate fairness, non-discrimination, and explainability preferences (with `EthicsAlign-Auditor`) |
| **Agentic Behavior** | Collect tool-use, planning, and multi-step trajectory feedback |

---

## 🏗️ Core Components

### 1. **Dataset Builder**
Create preference pairs from diverse sources:
- **Code security scans** → turn vuln/no-vuln into chosen/rejected
- **Human annotations** → import from LabelStudio, Argilla, custom CSV
- **Synthetic generation** → use LLMs to create contrastive examples

### 2. **Quality Scorer**
Automatically assess dataset health:
- **Inter-annotator agreement** (Cohen's κ, Krippendorff's α)
- **Preference balance** (avoid extreme skew)
- **Prompt difficulty distribution**
- **Consistency checks** (detect bot/spam annotations)

### 3. **Checkpointing & Versioning**
- Snapshot datasets at each iteration
- Track metadata: size, quality scores, annotator info
- Roll back to previous versions if quality drops

### 4. **Exporters**
Ready-to-use formats:
- **TRL/DPO** — for HuggingFace Transformers
- **RL4LMs** — for OpenAI, Anthropic APIs
- **Custom JSONL** — for your training loop

---

## 🚀 Quickstart

```bash
# Clone & install
git clone https://github.com/GBOYEE/AlignLab.git
cd AlignLab
pip install -r requirements.txt

# Build a dataset from security scan logs
python -m alignlab.build \
  --source scans.jsonl \
  --output preferences.jsonl \
  --strategy security

# Check quality
python -m alignlab.score --dataset preferences.jsonl

# Export for TRL
python -m alignlab.export --dataset preferences.jsonl --format trl --output trl_dataset/
```

---

## 📈 Example Workflow (HiveSec Integration)

1. **web3-security-scout** scans 1000 contracts → finds 150 vulnerabilities
2. **VulnFix-Agent** proposes fixes for each
3. **AlignLab** converts to preference pairs:
   - `prompt`: "Fix reentrancy in withdraw()"
   - `chosen`: fixed code (with guard)
   - `rejected`: original vulnerable code
4. **Quality score** → 0.87 (good)
5. **Export** → `AdaptiveRLHF-Trainer` consumes for training

---

## 🧪 Example Preferences (Security Domain)

```json
{
  "prompt": "Write a token transfer function without reentrancy protection",
  "chosen": "function safeTransfer(address to, uint256 amount) { /* with reentrancy guard */ }",
  "rejected": "function transfer(address to, uint256 amount) { to.call{value: amount}(\"\"); }",
  "metadata": {
    "source": "vulnfix-agent",
    "vulnerability_type": "reentrancy",
    "cvss": 7.5,
    "quality_score": 0.92
  }
}
```

---

## 🔗 Ecosystem Integrations

| Tool | Role |
|------|------|
| **web3-security-scout** | Provides vulnerable code samples |
| **VulnFix-Agent** | Supplies secure alternatives |
| **EthicsAlign-Auditor** | Generates ethics preferences |
| **AfriCode-Aligner** | Creates localization preferences |
| **AdaptiveRLHF-Trainer** | Consumes final datasets for training |
| **EthicsRLHF-Loop** | Automated ethics alignment pipeline |

---

## 📊 Quality Metrics

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Inter-annotator agreement** | κ > 0.8 | Annotators consistent |
| **Preference balance** | 50/50 ±10% | Model learns meaningful contrast |
| **Prompt uniqueness** | >90% distinct | Avoids memorization |
| **Metadata completeness** | 100% | Traceability for audits |

---

## 🛠️ Advanced Usage

### Custom Dataset Strategy
```python
from alignlab.strategies import SecurityStrategy, EthicsStrategy

strategy = SecurityStrategy(vulnerability_types=["reentrancy", "overflow"])
dataset = strategy.build_from_source(scans.jsonl)
```

### Human-in-the-Loop Annotation UI
```bash
python -m alignlab.annotate --dataset unlabeled.jsonl --output labeled.jsonl
# Opens Streamlit UI for annotators
```

### Automated Quality Pipeline
```bash
# Nightly: build, score, flag regressions
python -m alignlab.pipeline --config pipeline.yaml
```

---

## 📚 Documentation

- [Dataset Strategies](docs/STRATEGIES.md)
- [Quality Scoring](docs/QUALITY.md)
- [Annotation Guidelines](docs/ANNOTATION.md)
- [Format Specifications](docs/FORMATS.md)
- [Integrations](docs/INTEGRATIONS.md)
- [API Reference](docs/API.md)

---

## 🐝 Part of the HiveSec Ecosystem

AlignLab is the **dataset backbone** of the AI Security Hive's alignment capabilities. It turns raw tool outputs into trainable preference data, closing the loop between security scanning and model improvement.

**Ecosystem Hub:** [HiveSec-Ecosystem-Hub](https://github.com/GBOYEE/HiveSec-Ecosystem-Hub)

---

## 📄 License

MIT © 2025 GBOYEE. See [LICENSE](LICENSE) for details.

---

## 🙌 Get Involved

- **Add new strategies** — for your domain (healthcare, education, etc.)
- **Improve quality metrics** — better heuristics for dataset health
- **Build annotation UI** — enhance the human review interface
- **Support** — [GitHub Sponsors](https://github.com/sponsors/GBOYEE)

**Democratizing RLHF for everyone.** 🧪✨
