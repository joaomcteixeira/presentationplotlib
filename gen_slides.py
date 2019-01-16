import sys
import importlib.machinery

from matplotlib import pyplot as plt

for i, slide_path in enumerate(sys.argv[1:], start=1):
    
    sld = importlib.machinery.SourceFileLoader("s", slide_path).load_module()
    
    fig, ax = sld.slide(i)
    
    plt.savefig(f"page_{i:0>4}_{slide_path[:-3]}.pdf")
    plt.close("all")
