"""
Dataset quality metrics for RLHF preference pairs.
Metrics: lexical diversity, prompt length variance, domain balance.
"""
import json, statistics
from collections import Counter
from pathlib import Path
from typing import List, Dict

def lexical_diversity(text: str) -> float:
    words = text.lower().split()
    if not words:
        return 0.0
    unique = set(words)
    return len(unique) / len(words)

def score_dataset(pairs: List[Dict]) -> Dict:
    """Compute aggregate quality metrics."""
    n = len(pairs)
    prompts = [p['prompt'] for p in pairs]
    chosen = [p['chosen'] for p in pairs]
    rejected = [p['rejected'] for p in pairs]

    # Prompt length distribution
    prompt_lens = [len(p.split()) for p in prompts]
    chosen_lens = [len(c.split()) for c in chosen]
    rejected_lens = [len(r.split()) for r in rejected]

    # Lexical diversity per response
    chosen_div = [lexical_diversity(c) for c in chosen]
    rejected_div = [lexical_diversity(r) for r in rejected]

    # Domain balance
    domains = Counter(p['domain'] for p in pairs)

    return {
        "total_pairs": n,
        "prompt_len": {"mean": statistics.mean(prompt_lens), "stdev": statistics.stdev(prompt_lens) if n>1 else 0},
        "chosen_len": {"mean": statistics.mean(chosen_lens), "stdev": statistics.stdev(chosen_lens) if n>1 else 0},
        "rejected_len": {"mean": statistics.mean(rejected_lens), "stdev": statistics.stdev(rejected_lens) if n>1 else 0},
        "lexical_diversity": {"chosen_mean": statistics.mean(chosen_div), "rejected_mean": statistics.mean(rejected_div)},
        "domain_distribution": dict(domains),
        "quality_warnings": _warnings(prompt_lens, chosen_div, domains, n)
    }

def _warnings(prompt_lens, chosen_div, domains, total) -> List[str]:
    warnings = []
    if statistics.mean(prompt_lens) < 5:
        warnings.append("Prompts are very short; may lack context.")
    if statistics.mean(chosen_div) < 0.5:
        warnings.append("Chosen responses have low lexical diversity; likely repetitive.")
    if total > 0 and max(domains.values()) / total > 0.9:
        warnings.append("Dataset is heavily imbalanced towards one domain.")
    return warnings