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

cdef class CHECK_TAB:
    cdef public:
        str master 
        str long_chaine
        dict data_base
        int line 
    def __cinit__(master, long_chaine, data_base, line):
        self.master         = master 
        self.long_chaine    = long_chaine
        self.data_base      = data_base 
        self.line           = line 
        # errror
        self.error_init     = segmentation.ERROR( self.line )           
        # segmentation anylises                                                
        self.treatment      = segmentation.SEGMENTATION( self.master, self.long_chaine, self.data_base, self.line )     
        # string controlling function
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )       
        # backslash initialization                        
        self.backslash      = checking_if_backslash          
        # comment line
        self.comment        = comment_line