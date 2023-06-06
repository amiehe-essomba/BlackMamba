import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
from src.ggplot import error as er
from src.ggplot import dim
import pandas as pd 

def LAB(label : list, line : int, M : int):
    error = None 

    if label:
        for i, s in enumerate(label):
            if type(s) == type(list()): 
                if s:
                    for j, ss in enumerate(s):
                        if type(ss) == type(str()) : pass 
                        else:
                            error = er.ERRORS(line).ERROR22(string1="a strin()", string2=f"label[{i}, {j}]") 
                            break
                else:
                    error = er.ERRORS(line).ERROR7(string=f"label[{i}]") 
                    break
            else:
                error = er.ERRORS(line).ERROR22(string1="a list()", string2=f"label[{i}]") 
                break

        if error is None:
            if len(label) == M: pass 
            elif len(label) < M:
                idd = len(label)
                while idd < M:
                    label.append(None)
                    idd += 1
            else: error = er.ERRORS(line).ERROR20(string="label", N=M)
    else: label = [None for i in range(M)]  

    return label, error  

def plot_colors(color : str, line : int = 0, typ="color" ):
    error = None
    # Get all the color names
    all_colors = list(mcolors.CSS4_COLORS.keys())
    if type(color) == type(str()):
        if color in all_colors : pass
        else: error = er.ERRORS(line).ERROR0(color, str( all_colors ))
    elif type(color) == type(int()):
        try: color = all_colors[color]
        except IndexError: color = all_colors[-1]
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
                    for j, s in enumerate(c):
                        
                        if type(s) in [type(int()), np.int64, np.int16, np.int32]: 
                            c[j] = int(s)
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
    else:  error = er.ERRORS(line).ERROR0('style', str( plt_style ))
   
    
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
    else:  error = er.ERRORS(line).ERROR3( )
         
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

def Loc(loc: list , line: int = 0, M : int = 0):
    error = None
    true_loc = {
        "B" : 'best', 'UR' : 'upper right', "UL" : 'upper left', 
        'LL' : 'lower left', 'LR':'lower right', 'R':'right', 'CL':'center left', 
        'CR':'center right', 'LC':'lower center', 'UC':'upper center', 'C':'center'
        }
    if loc:
        for i, _loc_ in enumerate(loc):
            if _loc_ in list(true_loc.keys()): 
                _loc_ = true_loc[_loc_]
                loc[i] = _loc_
            else: 
                error = er.ERRORS(line=line).ERROR11(list(true_loc.keys()), f"location[{i}]")
                break 

        if error is None:
            if len(loc) == M : pass 
            elif len(loc) < M:
                idd = len(loc)
                while idd < M:
                    loc.append(true_loc['B'])
                    idd += 1
            else: error = er.ERRORS(line).ERROR20(string="location", N=M)
        else: pass
    else:
        for i in range(M):
            loc.append(true_loc['B'])
    
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

def color_scatter_rebuild(color, N, line, M):
    error = None 
    # Get all the color names
    all_colors = list(mcolors.CSS4_COLORS.keys())
    
    if M == 1:
        if type(color) == type(list()):
            if len(color) == 1:
                if type(color[0]) == type(str()) : 
                    if color[0] in all_colors : pass
                    else: error = er.ERRORS(line).ERROR0(color, str( all_colors ))
                elif type(color[0]) == type(int()) : 
                    try: color[0] = all_colors[color[0]]
                    except IndexError: color[0] = all_colors[-1]
                elif type(color[0]) == type(list()): pass 
                else: error = er.ERRORS(line).ERROR14(color, 0) 
            else:
                if len(color) == N: 
                    for i, c in enumerate(color):
                        if type(c) == type(list()):
                            for j, s in enumerate(c):
                                if type(s) ==  type(int()): pass
                                else: break 
                            if error is None: pass
                            else: break 
                        elif type(c) == type(str()): pass 
                        else:
                            error = er.ERRORS(line).ERROR17(i) 
                            break 
                    if error is None: pass
                else: error = er.ERRORS(line).ERROR16(0)
        elif type(color) == type(str()): pass 
        elif type(color) == type(int()) : 
            try: color[0] = all_colors[color[0]]
            except IndexError: color[0] = all_colors[-1]
        else: pass
    else:
        for i, s in enumerate(color):
            if type(s) == type(str()) : pass 
            elif type(s) == type(list()):
                if len(s) == N:
                    for w in s:
                        if type(w) == type(int()): pass 
                        else:
                            error = er.ERRORS(line).ERROR17(i) 
                            break
                    if error is None: color[i] = [s]
                    else: break
                else: 
                    error = er.ERRORS(line).ERROR16(i)
                    break
            else:
                error = er.ERRORS(line).ERROR15(i) 
                break
      
    return color, error 

def pie_params(DATA, colnames, line):
    error, pie = None, None
    if len(DATA) == len(colnames):
        if DATA:
            sum_ = 0
            for i, val in enumerate(DATA):
                try: sum_ += val
                except TypeError: 
                    error = er.ERRORS(line).ERROR23(f"data[{i}]")
                    break
            
            if error is None: pie = pd.Series(data=DATA, index=colnames)
            else: pass 
        else: error = er.ERRORS(line).ERROR23("data")
    else: error = er.ERRORS(line).ERROR24()

    return pie, error

def AXES(axes : any, N : int = 0, line : int = 0):
    identical, error = [], None

    if axes:
        for i, ax in  enumerate(axes):
            if type(ax) == type(int()): 
                if 0 <= ax < N: 
                    if ax not in identical: identical.append(ax)
                    else: pass
                else: 
                    error = er.ERRORS(line).ERROR18(ax=i, N=N) 
                    break
            else:
                error = er.ERRORS(line).ERROR19(ax=i) 
                break
        if error is None:
            if   len(axes) == N  : pass
            elif len(axes) < N   :
                for i in range(N):
                    if i not in identical: 
                        axes.append(i)
                        identical.append(i)
                    else: pass 
            else: error = er.ERRORS(line).ERROR20(N=N)
        else: pass
    else: 
        axes = []
        for i in range(N):
            axes.append(i)
            identical.append(i)
    return axes, error

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
        self.figsize        = figsize #
        self.title          = title
        self.plot_style     = plot_style #
    
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
        dim_size, loc, col, Axes = rest 
        self.LAB = label.copy()
        self.error, self.DATA, self.LABEL = dim.check_dim(X, Y, label, col, self.line)

        if self.error is None:
            # checking color
            N  = self.DATA.iloc[:, [0]].values.shape[0]
            M  = len(self.LABEL)
            if type(color) == type(str()) : self.color, self.error = plot_colors(color, self.line)
            else :  self.color, self.error = scatter_colors(X, color, self.line)
            
            if self.error is None:
                # checking plot style
                self.plot_style, self.error = plot_style(self.plot_style, self.line) 
                
                if self.error is None: 
                    self.size_, self.error = figuresize(self.figsize, self.line)
                    if self.error is None : 
                        self.marker, self.error = dim.scatter_params(self.line, marker=marker, M=M)#
                        if self.error is None:
                            self.dim_size,  self.chaine, self.error =  dim.scatter_Size(size=dim_size, line=self.line, M=M)#
                            
                            if self.error is None:
                                self.loc, self.error = Loc(loc, self.line, M)#
                                if self.error is None:
                                    self.color = rebuild_color(self.color, len(self.LABEL), "scatter")
                                    if self.error is None:
                                        self.color, self.error    = color_scatter_rebuild(color=color, N=N, line=self.line, M = M)#
                                        if self.error is None:
                                            self.LAB, self.error = LAB(label=self.LAB, line=self.line, M=M)
                                            if self.error is None:
                                                plt.style.use(self.plot_style)
                                                Axes, self.error = AXES(Axes, N=M)

                                                if self.error is None:
                                                    self.all_values = {
                                                        'DATA'      : self.DATA,
                                                        'LABEL'     : self.LABEL,
                                                        'X'         : X,
                                                        'legend'    : self.legend,
                                                        "loc"       : self.loc,
                                                        "lab"       : [self.xlab, self.ylab],
                                                        "title"     : self.title,
                                                        "marker"    : self.marker,
                                                        "figsize"   : self.size_,
                                                        "size"      : size,
                                                        "dim_size"  : self.dim_size,
                                                        "label"     : self.LAB, 
                                                        "chaine"    : self.chaine,
                                                        "Axes"      : Axes
                                                    }
                                                    self.error = plot_scatter(self.all_values.copy(), color=self.color, line=self.line) 
                                                else: pass 
                                            else: pass   
                                        else: pass 
                                    else: pass
                                else: pass
                            else: pass
                        else: pass
                    else: pass 
                else: pass
            else: pass 
        else: pass 

        return self.error 
    
    def pie(self, DATA : list, colnames : any, loc : tuple = (), AX=None):
        def pct_t(pct, datasets):
            value = int(round(pct / np.sum(datasets)) ** 100.0)
            return "{0:0.1f}%".format(pct, value)
        
        def LOC(location, line):
            e = None
            if location:
                if len(location) == 4:
                    sum_ = 0.0
                    
                    for i, val in enumerate(location):
                        try: sum_ += val
                        except TypeError : 
                            e = er.ERRORS(line).ERROR23(f"box_loc[{i}]")
                            break 
                else: e = er.ERRORS(line).ERROR25()
            else: pass 

            return location, e

        PIE, self.error = pie_params(DATA=DATA, colnames=colnames, line=self.line)
        if self.error is None:
            self.plot_style, self.error = plot_style(self.plot_style, self.line) 
            if self.error is None:
                plt.style.use(self.plot_style)
                self.size_, self.error = figuresize(self.figsize, self.line)
                if self.error is None:
                    if AX is None:
                        fig, axes = plt.subplots(1,1, figsize=self.size_)
                    else: axes = AX
                    PIE.plot(kind='pie', autopct = lambda pct : pct_t(pct, PIE), textprops = dict(color="w"), label="", ax=axes)
                    bbox_to_anchor, self.error = LOC(loc, self.line)
                    if self.error is None:
                        if self.legend is True:
                            if not self.title: 
                                if bbox_to_anchor is None: pass 
                                else: axes.legend(bbox_to_anchor = bbox_to_anchor) 
                            else:
                                if bbox_to_anchor is None: pass 
                                else: axes.legend(title=self.title, bbox_to_anchor = bbox_to_anchor, fontsize="medium")
                        else: pass
                        if AX is None: plt.show( )
                        else: pass
                    else: pass 
                else: pass
            else: pass
        else: pass

        return self.error

def plot_scatter( all_value : dict, color : any, line : int = 0):

    DATA            = all_value['DATA']
    LABEL           = all_value['LABEL']
    X               = all_value['X']
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
    Axes            = all_value['Axes']
    N               = DATA.iloc[:, [0]].values.shape[0]
    error = None
    if error is None:
        #try:
        if length % 2 == 0: length //= 2 
        else: length = (length + 1)//2
        fig, axes = plt.subplots(length,length, figsize=figsize)
        try:  axes = axes.ravel()
        except AttributeError:  axes = [axes]
        
        for i, ax in enumerate(axes):
            if i < len(LABEL):
                Y = DATA.iloc[:, [i]]
                if dim_size[i] is None:
                    scatter = axes[Axes[i]].scatter(X, Y, c=color[i], s=size, marker=marker[i])
                else:
                    scatter = axes[Axes[i]].scatter(X, Y, c=color[i], s=size, marker=marker[i], 
                                        vmax=dim_size[i][1], vmin=dim_size[i][0])
                
                axes[Axes[i]].set_title(title, loc="center")
                axes[Axes[i]].set_xlabel(xlabel=lab[0], fontsize="medium", color="black")
                axes[Axes[i]].set_ylabel(ylabel=lab[1], fontsize="medium", color="black")
                
                if legend is True:
                    if type(color[i]) == type(str()):
                        if label[i] is None: 
                            axes[Axes[i]].legend(loc=loc[i], labels=' ')
                        else: axes[Axes[i]].legend(labels=label[i], loc=loc[i])
                    else : 
                        if label[i] is not None : 
                            axes[Axes[i]].legend(handles = scatter.legend_elements()[0], labels=label[i], loc=loc[i])
                        else: 
                            axes[Axes[i]].legend(loc=loc[i], handles = scatter.legend_elements()[0])
                else: pass 
            else: break
        plt.show()
        
    else: pass

    return error