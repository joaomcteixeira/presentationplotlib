from matplotlib import pyplot as plt

import templates


@templates.template1
def slide(page_number, figure=None, ax=None):
    
    # write your slide here!!
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
