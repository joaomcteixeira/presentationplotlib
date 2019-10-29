"""
Stored attributes (variables) and helper functions that define
Template 1.
"""
from functools import wraps
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator


color = "#2A77D0"
"""
Main template colour
"""

font = "Cantarell"
"""
Main template font
"""

top_line_position = 0.98
"""
A line at the top of the slide
"""

bottom_line_position = 0.01
"""
A line at the bottom of the slide
"""

top_bottom_lines = {
    "linestyle": "-",
    "linewidth": 1,
    "color": color,
    }
"""
Line style for top and bottom lines.
"""

white_box = dict(
    boxstyle="square",
    pad=0.5,
    fc="white",
    lw=0,
    )
"""
A white box. Is useful to support text boxes or other objects.
"""

rounded_line_box = dict(
    boxstyle="round",
    pad=0.5,
    fc="white",
    lw=1,
    ec="black",
    )
"""
dict : A rounded line box.
"""

page_num_props = {
    "fontname": font,
    "color": color,
    "fontsize": 10,
    "ha": "center",
    "va": "center",
    "bbox": white_box,
    }
"""
dict : Properties for the page number.
"""

signature = (
    r"http://bit.ly/joaomcteixeira"
    )
"""
My signature
"""

signature_props = {
    "fontname": font,
    "color": color,
    "fontsize": 8,
    "bbox": white_box,
    }
"""
dict : Properties for the signature.
"""

suptitle_props = {
    "fontname": font,
    "fontsize": 12,
    "color": color,
    "bbox": white_box,
    "va": "center",
    }
"""
dict : properties for the suptitle.
"""

big_title_props = {
    "fontname": font,
    "color": color,
    "fontsize": 20,
    "va": "bottom",
    "ha": "left",
    }
"""
dict : Properties for the big title.
"""

main_title_props = {
    "fontname": font,
    "color": color,
    "fontsize": 20,
    "va": "center",
    "ha": "center",
    "x": 0.5,
    "y": 0.5,
    }
"""
dict : Properties for the main title.
"""

references_props = {
    "fontname": font,
    "color": "black",
    "fontsize": 10,
    "va": "bottom",
    "ha": "left",
    }
"""
dict : Properties for the references.
"""

text_box = {
    "fontname": font,
    "color": "black",
    "fontsize": 12,
    "va": "top",
    "ha": "left",
    "multialignment": "left",
    "linespacing": 1.5,
    }
"""
dict : properties for a general text box.
"""

labels_props = {
    "fontname": font,
    "fontsize": 16,
    "va": "bottom",
    "ha": "left",
    }
"""
dict : properties for labels.
"""

def add_axis(figure, rect):
    """
    Add a subplot (axis object) in rect position.
    """
    ax = figure.add_axes(rect)
    ax.axis('off')
    
    return ax


def add_figure(figure, rect, path):
    """
    Adds a figure.
    
    In matplotlib figures are subplots :-)
    """
    
    ax = add_axis(figure, rect)
    
    image = plt.imread(path)
    ax.imshow(image, aspect="equal", interpolation="none")
    
    return ax


def add_figure_border(figure, rect, path):
    """
    Adds a figure with border.
    
    See Template1.add_figure.
    """
    
    ax = add_figure(figure, rect, path)
    
    ax.axis("on")
    
    ax.tick_params(
        axis='both',
        which='both',
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
        )
    
    return ax


def add_maintitle(ax, s):
    """
    Adds main title.
    
    Parameters
    ----------
    ax : matplotlib axis.
    
    s : str
        the text to be added.
    """
    
    ax.text(s=s, **main_title_props)
    
    return


def add_suptitle(ax, s):
    """
    Adds suptitle.
    
    Parameters
    ----------
    ax : matplotlib axis.
    
    s : str
        the text to be added.
    """
    
    ax.text(
        x=0.02,
        y=top_line_position,
        s=s,
        **suptitle_props,
        )
    
    return


def set_screen():
    """
    Configures slide size and main properties.
    """
    figure, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=[11.02, 6.20],
        )
    
    ax.patch.set_facecolor('none')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    ax.axis("off")
    
    plt.tight_layout(
        rect=[-0.04, -0.06, 1.02, 1.028]
        )
    
    return figure, ax


def set_main_template():
    
    figure, ax = set_screen()
    
    x1 = 0.01
    x2 = 0.99
    y1 = top_line_position
    y2 = top_line_position
    
    ax.plot(
        [x1, x2],
        [y1, y2],
        **top_bottom_lines
        )
    
    x1 = 0.01
    x2 = 0.99
    y1 = bottom_line_position
    y2 = bottom_line_position
    
    ax.plot(
        [x1, x2],
        [y1, y2],
        **top_bottom_lines
        )
    
    return figure, ax

def add_grid(ax):
    """
    Adds grid to slide.
    """
    
    ax.set_xticks(np.arange(0, 1, 0.1))
    ax.set_yticks(np.arange(0, 1, 0.1))
    
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    
    ax.grid(b=True, which="major", axis='both', color='grey')
    ax.grid(b=True, which="minor", axis='both', color='lightgrey', ls="-.")
    
    ax.axis("on")
    
    return

def page0(func):
    """
    Decorator template for page 0.
    
    This is a specific page of Template1.
    """
    figure, ax = set_screen()
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        if kwargs["grid"]:
            add_grid(ax)
        
        slide = func(*args, figure=figure, ax=ax, **kwargs)
        
        return slide
    
    return wrapper
    

def main_title_template(func):
    """
    Decorator template for main title page.
    
    This is a specific page of Template1.
    """
    
    figure, ax = set_main_template()
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        if kwargs["grid"]:
            add_grid(ax)
        
        slide = func(*args, figure=figure, ax=ax, **kwargs)
        
        return slide
    
    return wrapper


def template(func):
    """
    Decorator template for general slides.
    """
    
    figure, ax = set_main_template()
    
    ax.text(
        x=0.88,
        y=bottom_line_position,
        s=signature,
        **signature_props
        )

    @wraps(func)
    def wrapper(*args, **kwargs):
        
        if kwargs["grid"]:
            add_grid(ax)
        
        slide = func(*args, figure=figure, ax=ax, **kwargs)
        
        ax.text(
            0.5,
            bottom_line_position,
            args[0],
            **page_num_props
            )
        
        return slide

    return wrapper

