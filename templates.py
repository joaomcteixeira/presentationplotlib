from functools import wraps

from matplotlib import pyplot as plt


def template1(func):
    
    general_color = "#2A77D0"
    signature = """João M.C. Teixeira
http://bit.ly/joaomcteixeira"""
    
    figure, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=[11.02, 6.20],
        )
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    plt.tick_params(
        axis='both',
        bottom=False,
        left=False,
        labelbottom=False,
        )
    
    plt.tight_layout(
        rect=[-0.04, -0.035, 1.015, 1.028]
        )
    
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    
    x1 = 0.01
    x2 = 0.99
    y1 = 0.99
    y2 = 0.99
    
    ax.plot(
        [x1, x2],
        [y1, y2],
        color=general_color,
        linestyle='-',
        linewidth=1,
        )
    
    x1 = 0.01
    x2 = 0.99
    y1 = 0.01
    y2 = 0.01
    
    ax.plot(
        [x1, x2],
        [y1, y2],
        color=general_color,
        linestyle='-',
        linewidth=1,
        )
    
    bbox_props = dict(boxstyle="square,pad=0.5", fc="white", lw=0)
    ax.text(
        0.86,
        0.01,
        signature,
        fontsize=8,
        color=general_color,
        bbox=bbox_props,
        )
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        slide = func(*args, figure=figure, ax=ax, **kwargs)
        
        ax.text(
            0.5,
            0.01,
            args[0],
            ha="center",
            va="center",
            color=general_color,
            bbox=bbox_props,
            )
        
        return slide
    
    return wrapper
