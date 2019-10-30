"""
Contains functions that draw objects.
"""

from matplotlib import patches


def draw_arrow(ax, x, y, dx, dy, **kwargs):
    """Draw arrow."""
    ax.arrow(x, y, dx, dy, **kwargs)


def draw_curved_arrow(
        ax,
        start,
        end,
        **kwargs,):
    
    a1 = patches.FancyArrowPatch(
        start,
        end,
        **kwargs,
        )

    ax.add_patch(a1)


def draw_rectangle(ax, x=0.1, y=0.1, w=0.1, h=0.1, **kwargs):
    

    rect = patches.Rectangle(
        (x, y),
        width=w,
        height=h,
        **kwargs,
        )

    ax.add_patch(rect)
