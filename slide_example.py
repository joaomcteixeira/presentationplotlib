from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from presentationplotlib.templates import template1


@template1.template
def slide(
        page_number,
        figure=None,
        ax=None,
        title="",
        **kwargs
        ):
    
    template1.add_suptitle(s="your cool title here", ax=ax)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide_example.pdf")
