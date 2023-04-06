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

from CythonModules.Windows.LEXER.backslash      import bs_interpretor as BSI
from CythonModules.Windows.LEXER.seg            import seg_interpretor as SI
from CythonModules.Windows.LEXER                import comment_line
from CythonModules.Windows.LEXER.seg            import segError as SE

cdef class CHECK_TAB_FOR_INTERPRETER:
    cdef public :
        str master 
        str long_chaine
        dict data_base
        unsigned long int line 

    cdef:
        str error
        str string_check 
        
    def __cinit__(self,
        master      ,     #   that's the concatenate main string
        long_chaine ,     #   non-concatenate main string
        data_base   ,     #   the data base containing all informations that will be used by the parxer
        line              #   current line number
        ):

        # concatenate main string
        self.master         = master                                                                                    
        # non-concatenate main string
        self.long_chaine    = long_chaine                                                                               
        # currently line
        self.line           = line                                                                                      
        # data base where data are stored
        self.data_base      = data_base   
        self.error          = ""
        self.string_check   = ""                                                                              
        
        
    cpdef CHECK_LINE(self,  unsigned long _id_, list  MainList ) :
        
        cdef :
            int i , idd
            str str_ 

        for i, str_ in enumerate( self.long_chaine ):
            if i == 0  :

                # checking if tabulation key was pressed or not on keyboard or if space was also set
                # at the beginning. the first character depends of the value of _id_,
                # _id_ is an integer and take theirs values in this range [0, .... N] and set the indent blocks

                if str_ not in ['\t', ' ']: pass
                else:
                    self.error = SE.ERROR( self.line ).ERROR9( )
                    break
            else: pass

        if not self.error:

            # if the first character of the line is < # > it means comment line was defined then the function < COMMENT_LINE >
            # will be call , and string_check takes another value instead "string" value
            # to set comment line it's very easy simple by using < # > as a first character

            self.string_check, idd, self.error = comment_line.COMMENT_LINE( self.master, self.data_base, self.line ).COMMENT()
            if not  self.error :
                if self.string_check in [ 'string', 'stringcomment' ]:

                    # in first of all after checking if comment line was or not difined the next step is to control
                    # if the backslash key was set or not to check that i create a function called < BACKSLASH >.
                    # backslash function is used to split the main string.

                    if self.master[0] in ['"', "'"] and self.master[-1] == self.master[0]:  pass
                    else:
                        if idd == -1: pass
                        else: self.master = self.master[: idd]

                    self.string_check, self.error             = BSI.BACKSSLASH( master=self.master,
                                                            data_base=self.data_base, line=self.line ).BACKSLASH(_id_= _id_, MainList=MainList )
                    if not self.error:

                        # after checking if backslash is defined i rebuild the entire main string
                        # by using < SEGMENTATION > function that a very powerful function which control many things,
                        # surch as the parentheses, backets .....

                        self.string_check, self.error   = SI.SEGMENTATION(self.string_check, self.string_check,
                                                            self.data_base, self.line).TREATEMENT(_id_, MainList)
                    else: pass
                else: pass
            else: pass
        else: pass

        # returning expression, cleaning main string and error got during all processes
        if (not self.string_check ) and (not self.error)    :  return None, None 
        elif (not self.string_check ) and (self.error)      :  return None, self.error 
        elif (self.string_check ) and (not self.error)      :  self.string_check, None 
        else:  return self.string_check, self.error