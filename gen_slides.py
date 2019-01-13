import sys
import importlib.machinery

from matplotlib import pyplot as plt

for i, slide_path in enumerate(sys.argv[1:], start=1):
    
    sld = importlib.machinery.SourceFileLoader("s", slide_path).load_module()
    
    fig, ax = sld.slide(i)
    
    plt.savefig(f"{slide_path[:-4]}_{i}.pdf")
    plt.close("all")
