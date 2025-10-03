""" Convert custom score format to format suitable for Ufora upload.

Assumes that the original scores are available as CSV file, with one column
referring to the student ID and one to the score item to extract (see arguments).
Prints a CSV file to stdout with formatted scores. 
"""

import argparse
import sys

import pandas as pd


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("column")
    p.add_argument("--id", default="ID")
    p.add_argument("--max", default=10, type=int)
    return p.parse_args()


def main():
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
