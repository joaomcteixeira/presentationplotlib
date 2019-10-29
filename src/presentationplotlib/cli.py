"""
Slides generator.
"""
import sys
import importlib.machinery
import argparse

from matplotlib import pyplot as plt

ap = argparse.ArgumentParser(description=__doc__)

ap.add_argument(
    "slides",
    help="list of slides PATHs in page order.",
    type=str,
    nargs="+",
    )

ap.add_argument(
    "-g",
    "--grid",
    help="Adds grid to slides",
    action="store_true",
    )

ap.add_argument(
    "-pg",
    "--page",
    help="The starting page number. Defaults to 1.",
    default=1,
    type=int,
    )

args = ap.parse_args()


def main():

    for i, slide_path in enumerate(args.slides, start=args.page):
        
        sld = importlib.machinery.SourceFileLoader("s", slide_path).load_module()
        
        fig, ax = sld.slide(
            i,
            grid=args.grid,
            )
        
        file_name = f"page_{i:0>4}_{slide_path[:-3]}.pdf"
        
        plt.savefig(f"{file_name}")
        print(f"Saved: {file_name}")
        plt.close("all")

if __name__ == '__main__':
   
    main()
