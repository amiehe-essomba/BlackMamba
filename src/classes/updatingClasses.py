from src.classes            import errorClass as EC
from src.classes            import db

class UPDATING:
    def __init__(self, data_base : int , line: int, extra : dict):
        self.data_base          = data_base
        self.line               = line
        self.extra_class_data   = extra
    
    def UPDATE_FUNCTION_BEFORE(self,  lexer : dict):
        self.error              = None
        self.key_init           = False
        self.functions          = lexer[ 'def' ]
        self.type               = self.functions[ 'type' ]
        self.arguments          = self.functions[ 'arguments' ]
        self.values             = self.functions[ 'value' ]
        self.history            = self.functions[ 'history_of_data' ]
        self.db                 = db.DB.def_data_base
        self.func_name          = self.db[ 'func_names' ][ 0 ]
        self.class_name         = self.data_base[ 'current_class' ]

        if not self.extra_class_data[ 'function_names' ] :
            if self.func_name == 'initialize':
                self.key_init   = True
                self.extra_class_data[ 'function_names' ].append( 'initialize' )
                self.extra_class_data[ 'init_function' ] = {
                    'initialize'    : True,
                    'self'          : True,
                    'variables'     : {
                        'vars'      : [],
                        'values'    : []
                    },
                    'function'      : None,
                    'active'        : False
                }
            else: self.extra_class_data[ 'function_names' ].append( self.func_name )
        else:
            if self.func_name == 'initialize':
                if 'initialize' in self.extra_class_data[ 'function_names' ]:
                    self.error = EC.ERRORS( self.line ).ERROR1( self.class_name )
                else: self.error = EC.ERRORS( self.line ).ERROR2( )
            else:
                if self.func_name in self.extra_class_data[ 'function_names' ]:
                    self.error = EC.ERRORS( self.line ).ERROR0( self.func_name, self.class_name )
                else:   self.extra_class_data[ 'function_names' ].append( self.func_name )

        return  self.key_init, self.error

    def UPDATE_FUNCTION_AFTER( self , header : tuple, db : dict, subClass : bool = False, subDict = None):
        
        self.error = None 
        
        if subClass is False:
            self.db                 = db
            self.func_name          = self.db[ 'func_names' ][ 0 ]
            self.class_name         = self.data_base[ 'current_class' ]
        
            if self.func_name == 'initialize':
                self.extra_class_data[ 'init_function' ]['function'] = [ header, self.db[ 'functions'][ : ] ]
            else:
                if not self.extra_class_data[ 'functions' ]:
                    self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
                else:
                    if self.func_name in self.extra_class_data[ 'function_names' ]:
                        try:
                            self.index = self.extra_class_data[ 'function_names' ].index( self.func_name )
                            self.extra_class_data[ 'functions' ][ self.index] = [ header, self.db[ 'functions'][ : ] ]
                        except IndexError:
                            self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
                    else:
                        self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
            
            self.db[ 'current_func' ]       = None
            self.db[ 'func_names' ]         = []
            self.db[ 'functions' ]          = []
        
        else:
            self.db = db 
            self.subClasses         = self.db[ 'classes' ]
            self.subNames           = self.db[ 'class_names' ]

            if not subDict['class_names']:
                subDict['class_names'].append( self.subNames[ 0 ] )
                subDict['classes'].append( self.subClasses[ 0 ] )
            else:
                if self.subNames[ 0 ] not in subDict['class_names']:
                    subDict['class_names'].append( self.subNames[ 0 ] )
                    subDict['classes'].append( self.subClasses[ 0 ] )
                else: self.error = EC.ERRORS( self.line ).ERROR18( self.subNames[ 0 ] )
                  
            self.db['class_names']  = []
            self.db['classes']      = []
        
        return self.error 
    
    def UPDATE_CLASS( self, history_of_data: list ):
        self.class_names        = self.data_base[ 'class_names' ]
        self.current_class      = self.data_base[ 'current_class' ]
        self.position_in_lists  = self.class_names.index( self.current_class )
        
        self.data_base[ 'classes' ][ self.position_in_lists ] = history_of_data
        self.data_base[ 'current_class' ]         = None