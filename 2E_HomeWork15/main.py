from Station import Work_site
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="my_parser")
    parser.add_argument(
        "numbers", metavar="N", type=int, nargs=1, help="input number of workers"
    )
    args = parser.parse_args()
    fabric = Work_site()
    fabric.start_shift(args.numbers[0])
