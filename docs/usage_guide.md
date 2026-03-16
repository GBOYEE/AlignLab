# Usage Guide

This guide shows how to generate RLHF preference datasets with AlignLab.

## Prerequisites

- Python 3.10+
- Git
- Access to XANDER hive (Redis running, agents up) – optional for synthetic generation; you can also use mock data.

## Installation

```bash
git clone https://github.com/GBOYEE/alignlab.git
cd alignlab
pip install -r requirements.txt
```

## Quick Example

Generate 10 secure code preference pairs:

```bash
python src/generate_preferences.py --domain secure_code --num 10 --output data/samples/demo_secure.jsonl
```

View the output:

```bash
head -n 1 data/samples/demo_secure.jsonl | python -m json.tool
```

## Supported Domains

- `secure_code` – Secure vs vulnerable code snippets
- `edu_tutor` – Scaffolding vs direct答案 for tutoring

## Custom Domain

To add a new domain:

1. Edit `src/generate_preferences.py`:
   - Add prompt list
   - Add `chosen` and `rejected` example lists
   - Extend `generate_pair` function
2. Run with `--domain your_name`.

## Integrating with Real Hive Agents

Replace the random choice logic with actual calls:

```python
from hive_messenger.hive_agent import HiveAgent
agent = HiveAgent(name="hunter", capabilities=["solana_meme_scan"])
agent.start()
response = agent.send("developer", {"type":"analyze_contract", ...})
```

See `xander-hive-framework` for agent setup.

## Output Format

Each line is a JSON object:

```json
{
  "prompt": "...",
  "chosen": "...",
  "rejected": "...",
  "domain": "...",
  "generator": "..."
}
```

Suitable for RLHF libraries (OpenRLHF, LlamaFactory).

## Next Steps

- Expand to 1k+ examples per domain
- Add human review (Label Studio)
- Fine‑tune a small model (7B) with the dataset and measure improvement
