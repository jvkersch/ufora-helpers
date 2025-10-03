"""Command-line interface for Ufora scores processing."""

import argparse
import sys

import pandas as pd


def parse_args():
    """Parse command line arguments."""
    p = argparse.ArgumentParser(
        description="Convert custom score format to format suitable for Ufora upload"
    )
    p.add_argument("csv", help="Input CSV file with scores")
    p.add_argument("column", help="Column name containing the scores")
    p.add_argument("--id", default="ID", help="Column name for student IDs (default: ID)")
    p.add_argument("--max", default=10, type=int, help="Maximum points for the assignment (default: 10)")
    return p.parse_args()


def main():
    """Main entry point for the CLI."""
    args = parse_args()
    scores = pd.read_csv(args.csv).sort_values(args.id)
    scores = scores.loc[~pd.isna(scores[args.id])]

    colname = f"{args.column} Points Grade <Numeric MaxPoints:{args.max}>"
    org_defined_id = scores[args.id].astype(int).apply(lambda s: f"#0{s}")

    upload = pd.DataFrame(
        {
            "OrgDefinedId": org_defined_id,
            colname: scores[args.column],
            "End-of-Line indicator": "#",
        }
    )

    upload.to_csv(sys.stdout, sep=",", index=None)


if __name__ == "__main__":
    main()