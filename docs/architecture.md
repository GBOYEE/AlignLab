# AlignLab Architecture

AlignLab demonstrates a pipeline for generating RLHF preference datasets using a multi‑agent hive. It is designed to be extensible to any domain, with current focus on underserved niches.

## Components

1. **Prompt Bank** – A collection of seed prompts for the target domain (e.g., secure coding tasks, educational questions). Can be static or generated dynamically.
2. **Response Generators** – Specialist agents (from XANDER hive) produce multiple candidate responses per prompt. For SecureCode, we use `web3-security-scout` to trigger code generation; for EduTutor, we use `prof` agent.
3. **Automatic Scorer** – A rule‑based or ML‑based function that assigns a preference score to each response. For SecureCode, we use static analysis (e.g., `bandit` or custom vulnerability checkers) to label secure vs insecure. For EduTutor, we use keyword/rubric matching.
4. **Pair Formatter** – Converts top‑scoring and low‑scoring responses into chosen/rejected pairs, formatted as JSONL.
5. **Export** – Writes pairs to `data/samples/` or a user‑specified location.

## Data Flow

```
prompt → generator agent(s) → candidates → scorer → chosen/rejected → JSONL
```

## Extending to New Domains

- Add a prompt list in `src/prompts.py`
- Implement a scorer function (or call external tool)
- Register in `generate_preferences.py` with a new `--domain` option
- Document in `docs/niche_focus.md`

## Integration with XANDER Hive

AlignLab does not require the full hive to run; it only needs access to the specialist agents' APIs. For full automation, start the hive Redis bus and ensure agents are running. The `hive_messenger` package is used to send requests and receive responses.

## Sample Output

```json
{
  "prompt": "Write a Python function that withdraws ETH from a smart contract.",
  "chosen": "Use reentrancy guard, check effects interactions pattern...",
  "rejected": "Call external transfer before updating balances; no guard...",
  "domain": "secure_code",
  "generator": "hunter_agent",
  "score_chosen": 0.9,
  "score_rejected": 0.2
}
```

## Future Enhancements

- Human review UI (Label Studio)
- Active learning: use model to select uncertain pairs for labeling
- Support for multi‑turn conversations
- Trajectory‑level preferences for agentic behavior
