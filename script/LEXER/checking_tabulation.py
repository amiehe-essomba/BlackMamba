"""
this function is created to control the first part of string syntax.
is the first function of the lexer that a created is based on 3 differents modules
-   COOMMENT_LINE()
-   BACKSLASH()
-   SEGMENTATIO()
these 3 functions represent the basis of the basis of my lexer.
comment_line used to define comments like this ( # that's is my fist programming language )
but we have also the possibility to set multi-line comments  by using the < begin > statment block.
i am gonna to show you further how it's possible to set multi-line = comments. but for momment let's
# focious out attention on the basis of out lexer.

"""

from script.LEXER                   import segmentation
from script                         import control_string
from script.LEXER                   import checking_if_backslash
from script.LEXER                   import comment_line
from script.STDIN.LinuxSTDIN        import bm_configure as bm

class CHECK_TAB:
    def __init__(self,
                master      : str,      #   that's the concatenate main string
                long_chaine : str,      #   non-concatenate main string
                data_base   : dict,     #   the data base containing all informations that will be used by the parxer
                line        : int       #   current line number
                ):

        self.master         = master                                                                                    # concatenate main string
        self.long_chaine    = long_chaine                                                                               # non-concatenate main string
        self.line           = line                                                                                      # currently line
        self.data_base      = data_base                                                                                 # data base where data are stored
        self.error_init     = segmentation.ERROR( self.line )                                                           # errror
        self.treatment      = segmentation.SEGMENTATION( self.master, self.long_chaine, self.data_base, self.line )     # segmentation anylises
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )                                # string controlling function
        self.backslash      = checking_if_backslash                                                                     # backslash initialization
        self.comment        = comment_line                                                                              # comment line line initialization
        self.color          = bm.fg.cyan_L

    def CHECK_LINE(self,
            _id_: int       # tab number
           ):

        self.error          = None
        self.string_check   = None

        for i, str_ in enumerate( self.long_chaine ):
            if i == 0  :

                # checking if tabulation key was pressed or not on keyboard or if space was also set
                # at the beginning. the first character depends of the value of _id_,
                # _id_ is an integer and take theirs values in this range [0, .... N] and set the indent blocks

                if str_ not in ['\t', ' ']: pass
                else:
                    self.error = self.error_init.ERROR9( )
                    break
            else: pass

        if self.error is None:

            # if the first character of the line is < # > it means comment line was defined then the function < COMMENT_LINE >
            # will be call , and string_check takes another value instead "string" value
            # to set comment line it's very easy simple by using < # > as a first character

            self.string_check, self._, self.error = self.comment.COMMENT_LINE( self.master, self.data_base, self.line ).COMMENT()
            if self.error is None:
                if self.string_check in [ 'string', 'stringcomment' ]:

                    # in first of all after checking if comment line was or not difined the next step is to control
                    # if the backslash key was set or not to check that i create a function called < BACKSLASH >.
                    # backslash function is used to split the main string.
                    if self._ is None: pass
                    else:

                        if self.master[0] in  ['"', "'"] and self.master[-1] == self.master[0]: pass
                        else:
                            if self._ is None: pass
                            else: self.master = self.master[: self._]

                    self.string_check, self.error             = self.backslash.BACKSSLASH(master=self.master,
                                                                data_base=self.data_base, line=self.line).BACKSLASH( _id_=_id_ )
                    if self.error is None:

                        # after checking if backslash is defined i rebuild the entire main string
                        # by using < SEGMENTATION > function that a very powerful function which control many things,
                        # surch as the parentheses, backets .....

                        self.string_check, self.error   = segmentation.SEGMENTATION(self.string_check, self.string_check,
                                                            self.data_base, self.line).TREATEMENT(_id_, self.color)
                    else: pass
                else: self.string_check = None
            else: pass
        else: pass

        # returning expression, cleaning main string and error got during all processes
        return self.string_check, self.error

class CHECK_TAB_FOR_INTERPRETER:
    def __init__(self,
                        master      : str,      #   that's the concatenate main string
                        long_chaine : str,      #   non-concatenate main string
                        data_base   : dict,     #   the data base containing all informations that will be used by the parxer
                        line        : int       #   current line number
                ):

        self.master         = master                                                                                    # concatenate main string
        self.long_chaine    = long_chaine                                                                               # non-concatenate main string
        self.line           = line                                                                                      # currently line
        self.data_base      = data_base                                                                                 # data base where data are stored
        self.error_init     = segmentation.ERROR( self.line )                                                           # errror
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )                                # string controlling function
        self.backslash      = checking_if_backslash                                                                     # backslash initialization
        self.comment        = comment_line                                                                              # comment line line initialization

    def CHECK_LINE(self,
                        _id_        : int,       # tab number
                        MainList    : list       # main list 
                   ):

        self.error          = None
        self.string_check   = None

        for i, str_ in enumerate( self.long_chaine ):
            if i == 0  :

                # checking if tabulation key was pressed or not on keyboard or if space was also set
                # at the beginning. the first character depends of the value of _id_,
                # _id_ is an integer and take theirs values in this range [0, .... N] and set the indent blocks

                if str_ not in ['\t', ' ']: pass
                else:
                    self.error = self.error_init.ERROR9( )
                    break
            else: pass

        if self.error is None:

            # if the first character of the line is < # > it means comment line was defined then the function < COMMENT_LINE >
            # will be call , and string_check takes another value instead "string" value
            # to set comment line it's very easy simple by using < # > as a first character

            self.string_check, self._, self.error = self.comment.COMMENT_LINE( self.master, self.data_base, self.line ).COMMENT()
            if self.error is None:
                if self.string_check in [ 'string', 'stringcomment' ]:

                    # in first of all after checking if comment line was or not difined the next step is to control
                    # if the backslash key was set or not to check that i create a function called < BACKSLASH >.
                    # backslash function is used to split the main string.

                    if self.master[0] in ['"', "'"] and self.master[-1] == self.master[0]:  pass
                    else:
                        if self._ is None: pass
                        else: self.master = self.master[: self._]

                    self.string_check, self.error             = self.backslash.BACKSSLASH_FOR_INTERPRETER( master=self.master,
                                                            data_base=self.data_base, line=self.line ).BACKSLASH(_id_= _id_, MainList=MainList )
                    if self.error is None:

                        # after checking if backslash is defined i rebuild the entire main string
                        # by using < SEGMENTATION > function that a very powerful function which control many things,
                        # surch as the parentheses, backets .....

                        self.string_check, self.error   = segmentation.SEGMENTATION_FOR_INTERPRETER(self.string_check, self.string_check,
                                                            self.data_base, self.line).TREATEMENT(_id_, MainList)
                    else: pass
                else: self.string_check = None
            else: pass
        else: pass

        # returning expression, cleaning main string and error got during all processes
        return self.string_check, self.error

