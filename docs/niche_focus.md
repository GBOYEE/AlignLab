# Niche Focus Areas

AlignLab targets RLHF gaps that are underserved by commercial providers.

## 1. SecureCode RLHF

Align code generation models to produce secure, vulnerability‑free outputs.

- **Prompts**: Coding tasks with security implications (e.g., ETH withdrawal, token transfers).
- **Chosen**: Secure implementations following best practices (reentrancy guard, input validation).
- **Rejected**: Vulnerable patterns (reentrancy, unchecked calls, integer overflow).

**Integration**: Uses `web3-security-scout` to detect vulnerabilities automatically.

## 2. EduTutor RLHF

Train AI tutors to use Socratic scaffolding instead of giving direct answers.

- **Prompts**: Student questions or misconceptions.
- **Chosen**: Guided hints, probing questions, step‑by‑step reasoning.
- **Rejected**: Direct answers, minimal explanation.

**Integration**: Uses `prof` agent’s pedagogical rubrics.

## 3. SmallModel Starter

General preference pairs for 7B–13B models to improve helpfulness and safety.

- Generic conversational prompts
- High‑quality helpful vs unhelpful responses

## 4. LangAlign

Preference pairs for low‑resource languages (Yoruba, Swahili, Pidgin).

- Bilingual prompts and responses
- Cultural appropriateness scoring

## 5. Agentic RLHF

Multi‑step trajectories for tool‑using agents.

- Prompts requiring multiple actions
- Chosen: efficient tool selection and ordering
- Rejected: wasted steps or incorrect tool use

**Integration**: Uses `degen-trader` and other agents to generate traces.

---

Each area will eventually have dedicated datasets and documentation. Contributions welcome!
