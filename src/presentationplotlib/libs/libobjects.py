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
