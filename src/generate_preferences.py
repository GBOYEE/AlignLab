#!/usr/bin/env python3
"""
Generate synthetic preference pairs for RLHF demo.
This script shows how the XANDER hive could be used to produce chosen/rejected pairs.
For real use, integrate with hive agents (hunter, prof, etc.) to generate responses.
"""

import json, time, random, argparse
from pathlib import Path

# Example templates for domains
SECURE_PROMPTS = [
    "Write a Python function that withdraws ETH from a smart contract.",
    "Implement a Solidity function that transfers tokens safely.",
    "Create a JavaScript function to parse user input for a web form."
]
SECURE_CHOSEN = [
    "Use reentrancy guard and check effects interactions.",
    "Apply checks-effects-interactions pattern and use a reentrancy lock.",
    "Validate inputs and use parameterized gas limits."
]
SECURE_REJECTED = [
    "Call external contract before updating state; no reentrancy protection.",
    "Direct transfer without balance checks; no event logs.",
    "Use eval() on user input without sanitization."
]

EDU_PROMPTS = [
    "Explain why the sky is blue to a 10-year-old.",
    "A student says photosynthesis is only about leaves. How would you correct them?",
    "What is the Pythagorean theorem and when is it used?"
]
EDU_CHOSEN = [
    "Let's think step by step: first, sunlight enters the atmosphere...",
    "Good question! Photosynthesis actually happens in chloroplasts, which are mostly in leaves, but also in stems...",
    "The Pythagorean theorem states that in a right triangle, a² + b² = c². It's used to find a missing side when you know the other two."
]
EDU_REJECTED = [
    "Because it just is.",
    "You're wrong, photosynthesis is everything.",
    "It's a math thing. Just memorize it."
]

def generate_pair(domain: str) -> dict:
    if domain == "secure_code":
        prompt = random.choice(SECURE_PROMPTS)
        chosen = random.choice(SECURE_CHOSEN)
        rejected = random.choice(SECURE_REJECTED)
    elif domain == "edu_tutor":
        prompt = random.choice(EDU_PROMPTS)
        chosen = random.choice(EDU_CHOSEN)
        rejected = random.choice(EDU_REJECTED)
    else:
        raise ValueError("Unknown domain")
    return {
        "prompt": prompt,
        "chosen": chosen,
        "rejected": rejected,
        "domain": domain,
        "generator": "alignlab-synthetic",
        "created": time.time()
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", choices=["secure_code","edu_tutor"], required=True)
    parser.add_argument("--num", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        for _ in range(args.num):
            pair = generate_pair(args.domain)
            f.write(json.dumps(pair) + "\n")
    print(f"Generated {args.num} {args.domain} pairs to {args.output}")

if __name__ == "__main__":
    main()
