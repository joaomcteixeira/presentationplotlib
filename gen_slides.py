import sys
import importlib.machinery

from matplotlib import pyplot as plt

for i, slide_path in enumerate(sys.argv[1:], start=1):
    
    sld = importlib.machinery.SourceFileLoader("s", slide_path).load_module()
    
    fig, ax = sld.slide(i)
    
    file_name = f"page_{i:0>4}_{slide_path[:-3]}.pdf"
    
    plt.savefig(f"{file_name}")
    print(f"Saved: {file_name}")
    plt.close("all")
