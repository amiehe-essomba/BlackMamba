from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from statement                                          import InternalStatement as IS
from statement                                          import externalIF as eIF
from updatingDataBase                                   import updating
try:  from CythonModules.Linux                          import loop_for
except ImportError: from CythonModules.Windows          import loop_for

cdef class EXTERNAL_IF_LOOP_STATEMENT:
    cdef public:
        master
        dict data_base 
        int  line 
    
    cdef :
        analyze, lex_par

    def __init__(self, master, data_base, line):
        self.master                 = master 
        self.data_base              = data_base 
        self.line                   = line 
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    cpdef IF_STATEMENT( self, bint bool_value, int tabulation, list loop_list, str _type_ = 'conditional', bint keyPass = False ):
        """
        module analize:
        #########################\n
        if < value >:
            < expressions >
        elif < value >:
            < expressions >
        else:
            < expressions >
        end:\n
        #########################\n
        params
        #########################\n
        :param bool_value:
        :param tabulation: {default value  = 1}
        :param loop_list:  {default value  = []}
        :param _type_:     {default value  = 'conditional'}
        :param keyPass:    {default value  = False}
        :return:           {self.error : str}
        """

        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [ self.bool_value ]
        self.index_else             = 0
        self.if_line                = 0
        self.break_                 = None

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(255, 20, 174)
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
