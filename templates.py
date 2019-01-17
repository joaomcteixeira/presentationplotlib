from functools import wraps
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

class Template1:
    
    color = "#2A77D0"
    font = "Cantarell"
    top_line_position = 0.98
    bottom_line_position = 0.01
    signature = (
        r"http://bit.ly/joaomcteixeira"
        )
    
    white_box = dict(
        boxstyle="square",
        pad=0.5,
        fc="white",
        lw=0,
        )
    
    rounded_line_box = dict(
        boxstyle="round",
        pad=0.5,
        fc="white",
        lw=1,
        ec="black",
        )
    
    top_bottom_lines = {
        "linestyle": "-",
        "linewidth": 1,
        "color": color,
        }
    
    page_num_props = {
        "fontname": font,
        "color": color,
        "fontsize": 10,
        "ha": "center",
        "va": "center",
        "bbox": white_box,
        }
        
    
    signature_props = {
        "fontname": font,
        "color": color,
        "fontsize": 8,
        "bbox": white_box,
        }
    
    suptitle_props = {
        "fontname": font,
        "fontsize": 12,
        "color": color,
        "bbox": white_box,
        "va": "center",
        }
    
    
    main_title_props = {
        "fontname": font,
        "color": color,
        "fontsize": 20,
        "va": "center",
        "ha": "center",
        "x": 0.5,
        "y": 0.5,
        }
    
    references_props = {
        "fontname": font,
        "color": "black",
        "fontsize": 10,
        "va": "bottom",
        "ha": "left",
        }
    
    text_box_lined = {
        "fontname": font,
        "color": "black",
        "fontsize": 10,
        "va": "top",
        "ha": "left",
        "multialignment": "left"
        }
    
    def add_axis(figure, rect):
        
        ax = figure.add_axes(rect)
        ax.axis('off')
        
        return ax
    
    
    def add_figure(figure, rect, path):
        
        ax = Template1.add_axis(figure, rect)
        
        image = plt.imread(path)
        ax.imshow(image, aspect="equal", interpolation="none")
        
        return ax
    
    def add_figure_border(figure, rect, path):
        
        ax = Template1.add_figure(figure, rect, path)
        
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
        
        ax.text(s=s, **Template1.main_title_props)
        
        return
    
    
    def add_suptitle(ax, s):
        ax.text(
        x=0.02,
        y=Template1.top_line_position,
        s=s,
        **Template1.suptitle_props,
        )
        
        return
    
    def template(func):
        
        figure, ax = plt.subplots(
            nrows=1,
            ncols=1,
            figsize=[11.02, 6.20],
            )
        
        ax.patch.set_facecolor('none')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        ax.set_xticks(np.arange(0, 1, 0.1))
        ax.set_yticks(np.arange(0, 1, 0.1))
        
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))
        
        ax.grid(b=True, which="major", axis='both', color='grey')
        ax.grid(b=True, which="minor", axis='both', color='lightgrey', ls="-.")
        
        ax.axis("on")
        
        
        plt.tight_layout(
            rect=[-0.04, -0.06, 1.02, 1.028]
            )
        
        x1 = 0.01
        x2 = 0.99
        y1 = Template1.top_line_position
        y2 = Template1.top_line_position
        
        ax.plot(
            [x1, x2],
            [y1, y2],
            **Template1.top_bottom_lines
            )
        
        x1 = 0.01
        x2 = 0.99
        y1 = Template1.bottom_line_position
        y2 = Template1.bottom_line_position
        
        ax.plot(
            [x1, x2],
            [y1, y2],
            **Template1.top_bottom_lines
            )
        
        bbox_props = dict(boxstyle="square,pad=0.5", fc="white", lw=0)
        ax.text(
            x=0.88,
            y=Template1.bottom_line_position,
            s=Template1.signature,
            **Template1.signature_props
            )
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            slide = func(*args, figure=figure, ax=ax, **kwargs)
            
            ax.text(
                0.5,
                Template1.bottom_line_position,
                args[0],
                **Template1.page_num_props
                )
            
            return slide
        
        return wrapper
    
