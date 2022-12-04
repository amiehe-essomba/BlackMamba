"""
[if, unless, until, while, case, elif, switch]
"""

from script                                             import control_string
from statement.error                                    import error as er
from script.PARXER.LEXER_CONFIGURE                      import numeric_lexer
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try                : from CythonModules.Windows         import fileError as fe
except ImportError : from CythonModules.Linux           import fileError as fe

class MAIN:
    def __init__(self,
         master         : str,              # it's a main string
         data_base      : dict,             # DataBase
         line           : int               # current line
         ):

        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def MAIN( self,
            typ         : str   = 'if',     # type of struct :{if, unless, while, whitch, until}
            opposite    : bool  = False,    # opposite become True if typ = {until or unless}
            interpreter : bool  = False,    # False if IDE is used, True if interpreter is used
            function    : any   = None      # when typ is used in {loop, def, class, or try} to avoid error before running code
            ):

        """
        :param typ: {default value = 'if'}
        :param opposite: {default value = False}
        :param interpreter: {default value = False}
        :param function: {default value = None}
        :return: { self._return_ : any, self.error : str }
        """
        self.error          = None
        self._return_       = None
        self.type           = [type(int()), type(float()), type(complex())]
        self.type1          = [type(list()), type(tuple())]
        self.strin          = ''
        self.all_type       = [type(int()), type(float()), type(complex()), type(list()), type(tuple()),
                               type(None), type(range(1)), type(bool()), type(dict()), type(str())]

        if   typ == 'if'    :  self.string, self.error = self.control.DELETE_SPACE(self.master[2: -1])
        elif typ == 'elif'  :  self.string, self.error = self.control.DELETE_SPACE(self.master[4: -1])
        elif typ == 'case'  :  self.string, self.error = self.control.DELETE_SPACE(self.master[4: -1])
        elif typ == 'while' :  self.string, self.error = self.control.DELETE_SPACE(self.master[5: -1])
        elif typ == 'until' :  self.string, self.error = self.control.DELETE_SPACE(self.master[5: -1])
        elif typ == 'unless':  self.string, self.error = self.control.DELETE_SPACE(self.master[6: -1])
        elif typ == 'switch':  self.string, self.error = self.control.DELETE_SPACE(self.master[6: -1])

        if self.error is None:
            if interpreter is True:
                self._return_, self.error = numeric_lexer.NUMERCAL_LEXER(self.string, self.data_base,
                                                                                    self.line).LEXER(self.master)
                if self.error is None:
                    if typ in [ 'switch', 'case' ]: pass
                    else:
                        if   type(self._return_) == type(bool())    : pass
                        elif type(self._return_) in self.type       :
                            if opposite is False: self._return_ = True
                            else                : self._return_ = False
                        elif type(self._return_) in self.type1      :
                            if opposite is False:
                                if len(self._return_) == 0  : self._return_ = False
                                else                        : self._return_ = True
                            else:
                                if len(self._return_) == 0  : self._return_ = True
                                else                        : self._return_ = False
                        elif type(self._return_) == type(range(1))  :
                            if opposite is False: self._return_ = True
                            else                : self._return_ = False
                        elif type(self._return_) == type(None)      :
                            if opposite is False: self._return_ = False
                            else                : self._return_ = True
                        elif type(self._return_) == type(str())     :
                            if opposite is False: self._return_ = [True if self._return_ else False][0]
                            else                : self._return_ = [False if self._return_ else True][0]
                        elif type(self._return_) == type(dict())    :
                            if opposite is False:  self._return_ = [True if self._return_ else False][0]
                            else                : self._return_ = [False if self._return_ else True][0]
                else:
                    if interpreter is False:
                        if   function is None:  pass
                        elif function in ['def', 'class', 'loop', 'try']:
                            self._error_ = fe.FileErrors( self.error ).initError()
                            if self._error_ not in ['SyntaxError']: self.error = None
                            else:  pass
                        else: pass
                    else: pass
            else: pass
        else:  self.error = er.ERRORS(self.line).ERROR0(self.master)

        return self._return_, self.error