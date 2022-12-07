"""
CLI tool to fetch data from "https://xkcd.com/"

python task_one.py --max 87  --any 15
"""

import argparse

if __name__=="__main__":
    example = """example:
    python task_one.py --max 87  --any 15
    """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )

    # print(parser.print_help())
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunck of resources to be fetched"
    )

    args = parser.parse_args()
    print(args.any)
    print(args.max)

    print(parser.print_help())

