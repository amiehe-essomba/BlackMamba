"""
This python module will be used to make a treatment on the
internal < if statement blocks > like [ if, for, try, unless,
until, while, begin, switch] in the case of IDE and [ if, for,
try, unless, until, while, begin, switch, elif, end, default,
else, except , finally] when the interpreter is running.
"""

from script                                             import control_string
from script.PARXER.LEXER_CONFIGURE                      import numeric_lexer
from statement.error                                    import error as er
from statement.comment                                  import structure
from statement                                          import mainStatement as MS
from loop                                               import mainFor
from statement.comment                                  import externalBlocks
try: from CythonModules.Windows                         import fileError as fe
except ImportError:  from CythonModules.Linux           import fileError as fe

class INTERNAL_BLOCKS:
    def __init__(self, 
                string          : str,          # concatenated string
                normal_string   : str,          # normal string
                data_base       : dict,         # data base
                line            : int           # current line
                ):
        
        self.line               = line
        self.string             = string
        self.normal_string      = normal_string
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer         = numeric_lexer
        self.chars              = self.control.LOWER_CASE()+self.control.UPPER_CASE()+['_']

    def BLOCKS(self, 
                tabulation      : int,              # tabulation
                function        : any   = None,     # functionn
                interpreter     : bool  = False,    # interpreter
                ):
        """
        :param tabulation:
        :param function:
        :param interpreter:
        :return:
        """
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None
        self.badFunctions   = ['elif', 'else', 'except', 'finally', 'case', 'default', 'func', 'class']
        self.len            = [4, 4, 6, 7, 4, 7, 4, 5]

        self.string         = self.string[ self.back_end : ]
        self.normal_string  = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 2 ] == 'if'      :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 2 ] in [ ' ' ]:
                                self._return_ = 'if:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(typ = 'if',
                                                    opposite= False, interpreter = interpreter, function = function)
                            else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:  
                            try: 
                                if self.normal_string[ 2 ] in [ ' ' ]:  self.error = er.ERRORS(self.line).ERROR1( 'if' )
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: self.error  = er.ERRORS(self.line).ERROR1( 'if' )
                    elif self.normal_string[ : 3 ] == 'for'     :
                        self._return_, self.value, self.error = mainFor.FOR_BLOCK(normal_string =self.normal_string,
                            data_base=self.data_base, line=self.line).FOR( function = function, interpreter = interpreter)
                    elif self.normal_string[ : 6 ] == 'unless'  :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 6 ] in [ ' ' ]:
                                self._return_ = 'unless:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='unless', opposite=True, interpreter=interpreter, function=function)
                            else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 6 ] in [ ' ' ]:  self.error = er.ERRORS(self.line).ERROR1( 'if' )
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: self.error  = er.ERRORS(self.line).ERROR1( 'unless' )
                    elif self.normal_string[ : 5 ] == 'until'   :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 5 ] in [ ' ' ]:
                                self._return_ = 'until:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='until', opposite=True, interpreter=interpreter, function=function)
                            else : self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 5 ] in [ ' ' ]:  self.error = er.ERRORS(self.line).ERROR1( 'until' )
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: self.error  = er.ERRORS(self.line).ERROR1( 'until' )
                    elif self.normal_string[ : 5 ] == 'while'   :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 5 ] in [ ' ' ]:
                                self._return_ = 'while:'

                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='while', opposite=False, interpreter=interpreter, function=function)
                            else:  self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 5 ] in [' ']: self.error = er.ERRORS(self.line).ERROR1('while')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:  self.error = er.ERRORS(self.line).ERROR1('while')
                    elif self.normal_string[ : 6 ] == 'switch'  :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 6 ] in [ ' ' ]:
                                self._return_ = 'switch:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='switch', opposite=False, interpreter=interpreter, function=function)
                            else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 6 ] in [ ' ' ]: self.error = er.ERRORS(self.line).ERROR1('switch')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:  self.error = er.ERRORS( self.line ).ERROR1( 'switch' )
                    elif self.normal_string[ : 3 ] == 'try'     :
                        self._return_, self.value, self.error = structure.STRUCT(data_base=self.data_base, line=self.line).STRUCT( num = 3,
                                                            normal_string=self.normal_string, tabulation=self.tabulation, split = True)
                    elif self.normal_string[ : 5 ] == 'begin'   :
                        self._return_, self.value, self.error = structure.STRUCT(data_base=self.data_base, line=self.line).STRUCT( num = 5,
                                                            normal_string=self.normal_string, tabulation=self.tabulation, split = True)
                    else:
                        if self.normal_string[ -1 ] != ':':
                            if self.normal_string not in self.badFunctions:
                                for i, num in enumerate(self.len):
                                    try:
                                        if self.normal_string[ : num ] in  self.badFunctions:
                                            if self.normal_string[ num ] in self.chars: pass
                                            else:
                                                self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
                                                break
                                        else : pass
                                    except IndexError: continue
                                if self.error is None:
                                    self._return_       = 'any'
                                    self.value          = self.normal_string
                                else: pass
                            else:  _, self.error    = self.control.CHECK_NAME(self.normal_string)
                        else: self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
                        self._return_   = 'any'
                        self.value      = self.normal_string
                except IndexError:  self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        return self._return_, self.value, self.error

    def INTERPRETER_BLOCKS(self,
                tabulation      : int,              # tabulation
                function        : any = None,       # function type [class, def , loop, try]
                typ             : str = 'if'        # type of structure
                ):
        """
        :param tabulation:
        :param function:
        :param typ:
        :return:
        """
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.string                 = self.string[ self.back_end : ]
        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 2 ] == 'if'          :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 2 ] in [ ' ' ]:
                                self._return_ = 'if:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='if', opposite=False, interpreter=True, function=function)
                            else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 2 ] in [ ' ' ]:
                                    self.error = er.ERRORS(self.line).ERROR1('if')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:  self.error = er.ERRORS(self.line).ERROR1('if')
                    elif self.normal_string[ : 3 ] == 'for'         :
                        self._return_, self.value, self.error = mainFor.FOR_BLOCK(self.normal_string,
                                                                                  self.data_base, self.line).FOR( function=function, interpreter=True)
                    elif self.normal_string[ : 6 ] == 'unless'      :
                        if self.normal_string[-1] == ':':
                            if self.normal_string[6] in [' ']:
                                self._return_ = 'unless:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='unless', opposite=True, interpreter=True, function=function)
                            else:
                                self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[6] in [' ']:
                                    self.error = er.ERRORS(self.line).ERROR1('if')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:
                                self.error = er.ERRORS(self.line).ERROR1('unless')
                    elif self.normal_string[ : 5 ] == 'until'       :
                        if self.normal_string[-1] == ':':
                            if self.normal_string[5] in [' ']:
                                self._return_ = 'until:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='until', opposite=True, interpreter=True, function=function)
                            else:
                                self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[5] in [' ']:
                                    self.error = er.ERRORS(self.line).ERROR1('until')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:
                                self.error = er.ERRORS(self.line).ERROR1('until')
                    elif self.normal_string[ : 5 ] == 'while'       :
                        if self.normal_string[-1] == ':':
                            if self.normal_string[5] in [' ']:
                                self._return_ = 'while:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='while', opposite=False, interpreter=True, function=function)
                            else:
                                self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[5] in [' ']:
                                    self.error = er.ERRORS(self.line).ERROR1('while')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:
                                self.error = er.ERRORS(self.line).ERROR1('while')
                    elif self.normal_string[ : 6 ] == 'switch'      :
                        if self.normal_string[-1] == ':':
                            if self.normal_string[6] in [' ']:
                                self._return_ = 'switch:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                    typ='switch', opposite=False, interpreter=True, function=function)
                            else:
                                self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[6] in [' ']:
                                    self.error = er.ERRORS(self.line).ERROR1('switch')
                                else:
                                    self._return_ = 'any'
                                    self.value = self.normal_string
                            except IndexError:
                                self.error = er.ERRORS(self.line).ERROR1('switch')
                    elif self.normal_string[ : 3 ] == 'try'         :
                        self._return_, self.value, self.error = structure.STRUCT(data_base=self.data_base, line=self.line).STRUCT(num=3,
                                                        normal_string=self.normal_string, tabulation=self.tabulation, split = True)
                    elif self.normal_string[ : 5 ] == 'begin'       :
                        self._return_, self.value, self.error = structure.STRUCT(data_base=self.data_base, line=self.line).STRUCT(num=5,
                                                        normal_string=self.normal_string, tabulation=self.tabulation, split = True)
                    elif self.normal_string[ : 3 ] == 'end'         :
                        if self.normal_string[-1] == ':':
                            self._return_ = 'end:'
                            self.error = externalBlocks.EXTERNAL(data_base=self.data_base, line=self.line).EXTERNAL(snum=3,
                                                            normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                        else:
                            if self.normal_string in ['end']: self.error = er.ERRORS(self.line).ERROR1('end')
                            else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 4 ] == 'elif'        :
                        if typ in [ 'if' ]:
                            if self.normal_string[ -1 ] == ':':
                                if self.normal_string[ 4 ] in [ ' ' ]:
                                    self._return_ = 'elif:'
                                    self.value, self.error = MS.MAIN(master=self.normal_string, data_base=self.data_base, line=self.line).MAIN(
                                        typ='elif', opposite=False, interpreter=True, function=function)
                                else:
                                    try:
                                        if self.normal_string[ 4 ] in [ ' ' ]: self.error = er.ERRORS(self.line).ERROR1('elif')
                                        else:
                                            self._return_   = 'any'
                                            self.value      = self.normal_string
                                    except IndexError:
                                        self.error = er.ERRORS(self.line).ERROR1('elif')
                            else: self.error = er.ERRORS(self.line).ERROR1('elif')
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 4 ] == 'case'        :
                        if typ in [ 'switch' ]:
                            if self.normal_string[ -1 ] == ':':
                                if self.normal_string[ 4 ] in [ ' ' ]:
                                    self._return_ = 'case:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='case', opposite=False, interpreter=True, function=function)
                                else:
                                    try:
                                        if self.normal_string[ 4 ] in [ ' ' ]: self.error = er.ERRORS(self.line).ERROR1('case')
                                        else:
                                            self._return_   = 'any'
                                            self.value      = self.normal_string
                                    except IndexError:
                                        self.error = er.ERRORS(self.line).ERROR1('case')
                            else: self.error = er.ERRORS(self.line).ERROR1('case')
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 6 ] == "except"      :
                        if typ in [ 'try' ]:
                            if self.normal_string[ -1 ] == ':':
                                if self.normal_string[ 6 ] in [ ' ' ]:
                                    self._return_ = 'except:'
                                    self.value, self.error = structure.STRUCT().EXCEPTIONS( normal_tring=self.normal_string,
                                                                            tabulation=self.tabulation, split=True)
                                else:
                                    try:
                                        if self.normal_string[ 6 ] in [ ' ' ]: self.error = er.ERRORS(self.line).ERROR1('except')
                                        else:
                                            self._return_   = 'any'
                                            self.value      = self.normal_string
                                    except IndexError: self.error = er.ERRORS(self.line).ERROR1('except')
                            else: self.error = er.ERRORS(self.line).ERROR1('except')
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 4 ] == 'else'        :
                        if typ in [ 'if' ]:
                            if self.normal_string[ -1 ] == ':':
                                self._return_ = 'else:'
                                self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL( num=4,
                                                                    normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                            else:
                                if self.normal_string in [ 'else' ]: self.error = er.ERRORS(self.line).ERROR1('else')
                                else: self.error = er.ERRORS(self.line).ERROR4()
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 7 ] == 'default'     :
                        if typ in [ 'switch' ]:
                            if self.normal_string[ -1 ] == ':':
                                self._return_ = 'default:'
                                self.error = externalBlocks.EXTERNAL(data_base=self.data_base, line=self.line).EXTERNAL(num=7,
                                                                normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                            else:
                                if self.normal_string in ['default']: self.error = er.ERRORS(self.line).ERROR1('default')
                                else: self.error = er.ERRORS(self.line).ERROR4()
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 7 ] == 'finally'     :
                        if typ in [ 'try' ]:
                            if self.normal_string[ -1 ] == ':':
                                self._return_ = 'finally:'
                                self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=7,
                                                            normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                            else:
                                if self.normal_string in ['finally']: self.error = er.ERRORS(self.line).ERROR1('finally')
                                else: self.error = er.ERRORS(self.line).ERROR4()
                        else: self.error = er.ERRORS(self.line).ERROR4()
                    else:
                        self._return_   = 'any'
                        self.value      = self.normal_string
                except IndexError:  self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_   = 'empty'
            self.error      = None

        return self._return_, self.value, self.error

       

