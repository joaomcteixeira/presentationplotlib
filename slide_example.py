from matplotlib import pyplot as plt

import templates


@templates.Template1.template
def slide(page_number, figure=None, ax=None, title=""):
    
    ax.text(
        0.02,
        0.98,
        "Farseer-NMR",
        color=templates.general_color_1,
        bbox=templates.bbox_props_1,
        va="center",
        )
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
