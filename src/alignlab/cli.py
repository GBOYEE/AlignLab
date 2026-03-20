#!/usr/bin/env python3
"""
AlignLab CLI: generate RLHF preference datasets with quality reporting.
"""
import json, argparse, sys
from pathlib import Path
from .quality import score_dataset
from .generate_preferences import generate_pair

def main():
    parser = argparse.ArgumentParser(description="AlignLab — RLHF dataset toolkit")
    sub = parser.add_subparsers(dest='cmd', required=True)

    gen = sub.add_parser("generate", help="Generate a synthetic dataset")
    gen.add_argument("--output", type=Path, required=True)
    gen.add_argument("--domain", choices=["secure_code","edu_tutor"], action='append', required=True)
    gen.add_argument("--num", type=int, default=100, help="Total pairs to generate")
    gen.add_argument("--balance", action='store_true', help="Split evenly across specified domains")

    score = sub.add_parser("score", help="Score an existing dataset")
    score.add_argument("--input", type=Path, required=True)

    args = parser.parse_args()

    if args.cmd == 'generate':
        domains = args.domain
        if args.balance:
            per_domain = args.num // len(domains)
            remainder = args.num % len(domains)
            counts = {d: per_domain for d in domains}
            # distribute remainder to first domains
            for i in range(remainder):
                counts[domains[i]] += 1
        else:
            counts = {domains[0]: args.num}  # all to first domain

        pairs = []
        for domain, count in counts.items():
            for _ in range(count):
                pairs.append(generate_pair(domain))

        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w") as f:
            for p in pairs:
                f.write(json.dumps(p) + "\n")
        print(f"Generated {len(pairs)} pairs to {args.output}")

        # Also produce quality report
        report = score_dataset(pairs)
        report_path = args.output.with_suffix('.quality.json')
        with report_path.open("w") as f:
            json.dump(report, f, indent=2)
        print(f"Quality report: {report_path}")
        if report['quality_warnings']:
            print("Warnings:")
            for w in report['quality_warnings']:
                print(f"- {w}")

    elif args.cmd == 'score':
        pairs = []
        with args.input.open() as f:
            for line in f:
                if line.strip():
                    pairs.append(json.loads(line))
        report = score_dataset(pairs)
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    sys.exit(main())