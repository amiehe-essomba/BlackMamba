import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
from src.ggplot import error as er
from src.ggplot import dim

def plot_colors(color : str, line : int = 0 ):
    error = None
    # Get all the color names
    all_colors = list(mcolors.CSS4_COLORS.keys())

    if color in all_colors : pass
    else: error = er.ERRORS(line).ERROR0('color', str( all_colors ))

    return color, error

def scatter_colors(X, color : str, line : int = 0 ):
    error = None
    # Get all the color names
    if type(X) == type(np.array([1])):
        if X.shape[0] == len(color):
            for s in color:
                if type(s) == type(int()): pass 
                else: 
                    error = er.ERRORS(line).ERROR5('color')
                    break
        else: error = er.ERRORS(line).ERROR6( X.shape[0], len(color)) 
    else:
        if len(X) == len(color):
           for s in color:
                if type(s) == type(int()): pass 
                else: 
                    error = er.ERRORS(line).ERROR5('color')
                    break
        else:error = er.ERRORS(line).ERROR6( len(X), len(color)) 

    return color, error
   
def plot_style( style : str = 'classic', line : int = 0):
    error = None 
    # get all style available 
    plt_style = list( plt.style.available )

    if style in plt_style: pass
    else: error = er.ERRORS(line).ERROR0('style', str( plot_colors ))

    return style, error 

def line_style( ls : str, line : int = 0 ):
    error = None
    # get line style 
    line_s =  ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']

    if ls in line_s: pass 
    else: error = er.ERRORS(line).ERROR0('linestyle', str( plot_colors ))

    return ls, error

def figuresize(size : tuple, line : int = 0):
    error = None 

    if len(size) == 2:
        for s in size:
            if type(s) == type(int()): pass
            else: 
                error = er.ERRORS(line).ERROR4(size, s)
                break
    else: error = er.ERRORS(line).ERROR3()

    return size, error

class ggplot:
    def __init__(self, line, 
            xlab        : str, 
            ylab        : str, 
            figsize    : tuple, 
            legend      : bool,
            title       : str,
            plot_style  : str
            ) :
        self.line           = line
        self.xlab           = xlab
        self.ylab           = ylab 
        self.legend         = legend
        self.figsize        = figsize
        self.title          = title
        self.plot_style     = plot_style

    
    def plot(self, X, Y, color : str, ls : str, lw : int):
        # checking the X and Y dimensions 
        self.error = dim.check_dim(X, Y, self.line)
   
        if self.error is None:
            # checking color
            self.color, self.error = plot_colors(color, self.line)
            if self.error is None:
                # checking plot style
                self.plot_style, self.error = plot_style(self.plot_style, self.line)
                if self.error is None: 
                    # checking_line style 
                    self.ls , self.error = line_style(ls, self.line)
                    if self.error is None: 
                        self.size, self.error = figuresize(self.figsize, self.line)
                        if self.error is None : 
                            plt.style.use(self.plot_style)
                            fig, ax = plt.subplots(1,1, figsize=self.size)
                            ax.plot(X, Y, color=self.color, ls=self.ls, lw=lw)
                            ax.set_title(self.title)
                            ax.set_xlabel(xlabel=self.xlab, fontsize="medium", color=self.color)
                            ax.set_ylabel(ylabel=self.ylab, fontsize="medium", color=self.color)
                            if self.legend is True:  ax.legend("")
                            else: pass 
                            plt.show()
                        else: pass 
                    else: pass 
                else: pass
            else: pass 
        else: pass 

        return self.error 
    
    def scatter(self, X, Y, color : str, size : int, label : str,  marker : str):
        # checking the X and Y dimensions 
        self.error = dim.check_dim(X, Y, self.line)
        if self.error is None:
            # checking color
            if type(color) == type(str()) : self.color, self.error = plot_colors(color, self.line)
            else : self.color, self.error = scatter_colors(X, color, self.line)
            
            if self.error is None:
                # checking plot style
                self.plot_style, self.error = plot_style(self.plot_style, self.line)
                if self.error is None: 
                    self.size_, self.error = figuresize(self.figsize, self.line)
                    if self.error is None : 
                        plt.style.use(self.plot_style)
                        fig, ax = plt.subplots(1,1, figsize=self.size_)
                        scatter = ax.scatter(X, Y, c=self.color, s=size, marker=marker)
                        ax.set_title(self.title)
                        ax.set_xlabel(xlabel=self.xlab, fontsize="medium", color=self.color)
                        ax.set_ylabel(ylabel=self.ylab, fontsize="medium", color=self.color)
                        if self.legend is True:  ax.legend(handles = scatter.legend_elements()[0], label=label)
                        else: pass 
                        plt.show()
                    else: pass 
                else: pass
            else: pass 
        else: pass 

        return self.error 