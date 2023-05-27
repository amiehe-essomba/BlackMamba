import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
from src.ggplot import error as er
from src.ggplot import dim

def plot_colors(color : str, line : int = 0, typ="color" ):
    error = None
    # Get all the color names
    all_colors = list(mcolors.CSS4_COLORS.keys())
    if type(color) == type(str()):
        if color in all_colors : pass
        else: error = er.ERRORS(line).ERROR0(color, str( all_colors ))
    else:
        for i, c in enumerate(color):
            if type(c) == type(str()):
                if c in all_colors : pass
                else: 
                    error = er.ERRORS(line).ERROR0(c, str( all_colors )) 
                    break
            elif type(c) == type(int()):
                try: color[i] = all_colors[c]
                except IndexError: color[i] = all_colors[-1]
            else: 
                error = er.ERRORS(line).ERROR14(color, c) 
                break
    return color, error

def scatter_colors(X, color : str, line : int = 0 ):
    error = None
    # Get all the color names
    if type(X) == type(np.array([1])):
        for i, c in enumerate(color):
            if type(c) == type(list()):
                if X.shape[0] == len(c):
                    for s in c:
                        if type(s) == type(int()): pass 
                        else: 
                            error = er.ERRORS(line).ERROR5('color')
                            break
                    if error is None: pass
                    else: break
                else: 
                    error = er.ERRORS(line).ERROR6( X.shape[0], len(c)) 
                    break
            elif type(c) in [ type(int()), type(str())]:
                c, error = plot_colors(c, line)
                if error : break  
            else:
                error = er.ERRORS(line).ERROR15( idd=i) 
                break
    else:
        for c, i in enumerate(color):
            if type(c) == type(list()):
                if len(X) == len(c):
                    for s in c :
                        if type(s) == type(int()): pass 
                        else: 
                            error = er.ERRORS(line).ERROR5('color')
                            break
                    if error : break
                else:
                    error = er.ERRORS(line).ERROR6( len(X), len(c)) 
                    break
            elif type(c) in [ type(int()), type(str())]:
                c, error = plot_colors(c, line)
                if error : break  
            else:
                error = er.ERRORS(line).ERROR15( idd=i) 
                break
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

def Size( dim_size : tuple, line : int = 0 ):
    typ = ['xlim', "ylim"]
    error, dim_size = None, list(dim_size)
    chaine = None 

    for i, size in enumerate(dim_size):
        if size is not None:
            if len(size) == 2:
                for s in size:
                    if type(s) in [type(int()), type(float())]: pass
                    else: 
                        error = er.ERRORS(line).ERROR9(size, s)
                        break
                if error is None: 
                    if dim_size[i][1] > dim_size[i][0] : dim_size[i] = list(dim_size[i])
                    else: 
                        error = er.ERRORS(line).ERROR12(data=tuple(dim_size[i]))
                        break
                else: break
            else: 
                error = er.ERRORS(line).ERROR8(string=typ[i])
                break
        else: pass

    if error is None:
        if dim_size[0] is None: 
            if dim_size[1] is None: pass
            else: chaine = "ylim"
        else:
            if dim_size[1] is None:  chaine = "xlim"
            else: chaine = "all"
    else: pass  

    return dim_size, error, chaine

def Loc(loc: str , line: int = 0):
    error = None
    true_loc = {
        "B" : 'best', 'UR' : 'upper right', "UL" : 'upper left', 
        'LL' : 'lower left', 'LR':'lower right', 'R':'right', 'CL':'center left', 
        'CR':'center right', 'LC':'lower center', 'UC':'upper center', 'C':'center'
        }
    if loc in list(true_loc.keys()): loc = true_loc[loc]
    else: error = er.ERRORS(line=line).ERROR11(len(true_loc.keys()), "location")
    
    return loc, error 

def rebuild_color(color, N, sc : str = "plot"):
    
    all_colors = list(mcolors.CSS4_COLORS.keys())
    if type(color) == type(str()):
        if N == 1: 
            if sc == 'plot': color = [color]
            else: color = [color]
        else: 
            color = [color]
            for i in range(N-1):
                for s in all_colors:
                    if s not in color: 
                        color.append(s)
                        break 
                    else: pass 
    else:
        if len(color) == N: pass 
        elif len(color) > N: color = color[: N]
        else: 
            for i in range(N-len(color)):
                for s in all_colors:
                    if s not in color: 
                        color.append(s)
                        break 
                    else: pass 

    return color

def color_scatter_rebuild(color, N, line):
    error = None 

    for i, s in enumerate(color):
        if type(s) == type(str()) : pass 
        elif type(s) == type(list()):
            if len(s) == N:
                for w in s:
                    if type(w) == type(int()): pass 
                    else:
                        error = er.ERRORS(line).ERROR17(i) 
                        break
                if error is None: pass 
                else: break
            else: 
                error = er.ERRORS(line).ERROR16(i)
                break
        else:
            error = er.ERRORS(line).ERROR15(i) 
            break
    
    return color, error 

def pie_params(DATA, colname, groupby):
    error = None
    if type(colname) == type(str()):
        if colname in list(DATA.keys()): DATA.groupby(groupby)[[colname]].sum()
        else: pass 
    else: 
        for i, name in enumerate(colname):
            if name in list(DATA.keys()): pass 
            else :break

        if not error:
            DATA = DATA.groupby(groupby)[colname].sum()
        else: pass 

    return DATA 

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
    
    def plot(self, X, Y, color : str, ls : str, lw : int, label : any, col : any):
        # checking the X and Y dimensions 
        self.error, self.DATA, self.LABEL = dim.check_dim(X, Y, label, col, self.line)
   
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
                            self.color = rebuild_color(self.color, len(self.LABEL))
                            
                            self.DATA[self.LABEL].plot(kind="line", ax=ax, color=self.color, lw=lw, ls=self.ls, label=self.LABEL)
                            ax.set_title(self.title)
                            ax.set_xlabel(xlabel=self.xlab, fontsize="medium" )
                            ax.set_ylabel(ylabel=self.ylab, fontsize="medium" )
                            if self.legend is True:  ax.legend()
                            else: pass 
                            plt.show()
                        else: pass 
                    else: pass 
                else: pass
            else: pass 
        else: pass 

        return self.error 
    
    def scatter(self, X, Y, color : str, size : int, label : str,  marker : int, rest : tuple):
        # checking the X and Y dimensions 
        dim_size, loc, col = rest 

        self.error, self.DATA, self.LABEL = dim.check_dim(X, Y, label, col, self.line)

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
                        self.marker, self.error = dim.scatter_params(self.line, marker=marker)
                        if self.error is None:
                            self.dim_size,  self.chaine, self.error =  dim.scatter_Size(size=dim_size, line=self.line)
                            
                            if self.error is None:
                                self.loc, self.error = Loc(loc, self.line)
                                if self.error is None:
                                    self.color = rebuild_color(self.color, len(self.LABEL), "scatter")
                                    if self.error is None:
                                        plt.style.use(self.plot_style)
                                        
                                        self.all_values = {
                                            'DATA'      : self.DATA,
                                            'LABEL'     : self.LABEL,
                                            'X'         : X,
                                            'color'     : self.color,
                                            'legend'    : self.legend,
                                            "loc"       : self.loc,
                                            "lab"       : [self.xlab, self.ylab],
                                            "title"     : self.title,
                                            "marker"    : self.marker,
                                            "figsize"   : self.size_,
                                            "size"      : size,
                                            "dim_size"  : self.dim_size,
                                            "label"     : label, 
                                            "chaine"    : self.chaine
                                        }
                                        
                                        plot_scatter(self.all_values, line=self.line)     
                                    else: pass
                                else: pass
                            else: pass
                        else: pass
                    else: pass 
                else: pass
            else: pass 
        else: pass 

        return self.error 
    
    def pie(self, DATA : any, groupby : str, colname : any, label : any="", title : str = "pie plot"):
        def pct_t(pct, datasets):
            try:
                value = int(round(pct / np.sum(datasets)) ** 100.0)
                return "{0:0.1f}".format(value, pct)
            except ValueError: pass 

        if groupby in list(DATA.keys()):
            PIE, error = pie_params(DATA=DATA, colname=colname, groupby=groupby)
            if error is None:
                PIE.plot(kind='pie', autopct = lambda pct : pct_t(pct, PIE), textprops = dict(color="w"), label="")
                plt.legend(bbox_to_anchor = (0.1, 0.1, 0.5, 0.5))
                plt.title(title, fontsize="medium")
                plt.show( )
            else: pass 
        else: pass

def plot_scatter( all_value : dict, line : int = 0):

    DATA            = all_value['DATA']
    LABEL           = all_value['LABEL']
    X               = all_value['X']
    color           = all_value['color']
    size            = all_value['size']
    marker          = all_value['marker']
    lab             = all_value['lab']
    title           = all_value['title']
    loc             = all_value['loc']
    legend          = all_value['legend']
    figsize         = all_value['figsize']
    label           = all_value['label']
    chaine          = all_value['chaine']
    dim_size        = all_value['dim_size']
    length          = len(LABEL)
    N               = DATA.iloc[:, [0]].values.shape[0]
    color, error    = color_scatter_rebuild(color=color, N=N, line=line)

    if error is None:
        if length % 2 == 0: length //= 2 
        else: length = (length + 1)//2
        fig, axes = plt.subplots(length,length, figsize=figsize)
        try:  axes = axes.ravel()
        except AttributeError:  axes = [axes]

        for i, ax in enumerate(axes):
            if i < len(LABEL):
                Y = DATA.iloc[:, [i]]
                if chaine is None:
                    scatter = ax.scatter(X, Y, c=color[i], s=size, marker=marker)
                else:
                    scatter = ax.scatter(X, Y, c=color[i], s=size, marker=marker, 
                                         vmax=dim_size[1], vmin=dim_size[0])

                ax.set_title(title, loc="center")
                ax.set_xlabel(xlabel=lab[0], fontsize="medium", color="black")
                ax.set_ylabel(ylabel=lab[1], fontsize="medium", color="black")
                    
                if legend is True:
                    if type(color[i]) == type(str()):
                        if label is None: ax.legend(loc=loc)
                        else: ax.legend(labels=label, loc=loc)
                    else : 
                        if label is not None : 
                            ax.legend(handles = scatter.legend_elements()[0], labels=label, loc=loc)
                        else: 
                            ax.legend(handles = scatter.legend_elements()[0], loc=loc)
                else: pass 
            else: break
        plt.show()
    else: pass

    return error