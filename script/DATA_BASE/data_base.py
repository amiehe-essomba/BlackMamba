#from colorama import Fore, init, Style
#from script.DATA_BASE   import ansi

from script.STDIN.LinuxSTDIN    import bm_configure as bm


class DATA_BASE:
    def __init__(self):
        pass

    def STORAGE(self):
        self.function_name, self.function_expressions = DATA_BASE().FUNCTIONS()

        self.data_base      = {
        'global_vars'       : {             # dict for variables and theirs values 
            'vars'          : [],           # variables
            'values'        : []            # values
            },
        'variables'         : {             # dict containing varaibles and values defined as global 
            'vars'          : [],           # variables
            'values'        : []           # values
            },
        'irene'             : None,         # contoling string(with or without bracket)
        'functions'         : [],           # all functions 
        'classes'           : [],           # all classes
        'class_names'       : [],           # all calsses names
        'func_names'        : [],           # all functions names 
        'loop_for'          : [],           # when loop for is call
        'loop_while'        : [],           # when loop while is called
        'loop_until'        : [],           # when loop until is called , it's opposited while function 
        'continue'          : None,         # continue move to the next line 
        'next'              : None,         # moving to de next line same as continue
        'pass'              : None,         # pass instruction 
        'break'             : None,         # break loop
        'exit'              : None,         # exit code
        'try'               : None,         # when try function is called
        'begin'             : None,         # when begin function is called 
        'if'                : [],           # when if function si called
        'switch'            : [],           # when switch function is called
        'unless'            : [],           # when unless function si called / opposited if function 
        'return'            : None,         # dict containing the values returned 
        'print'             : [],           # when print function is called
        'sub_print'         : None,         # if print function was used in loop, def, class etc...
        'current_func'      : None,         # current function called
        'current_class'     : None,         # current class called
        'transformation'    : None,         # when partial functions was used like __sum__, etc...
        'no_printed_values' : [],           # 
        'line'              : None,         # getting current line 
        'encoding'          : None,         # encoding/decoding
        'importation'       : None,         # defining on yes if importation 
        'LIB'               : {             # dict for internal function 
            'func_names'    : self.function_name,               # functions names from internal functions 
            'functions'     : self.function_expressions,        # values for each functions from internal functions
            'class_names'   : [],                               # class names
            'classes'       : []                                # values for each classes
            },
        'modulesImport'     : {             # dict for  modules importetd
            'moduleNames'   : [],           # modules names
            'TrueFileNames' : {             # history files load
                'names'     : [],           # name of file load
                'path'      : [],           # file location
                'line'      : []            # line error
                },
            'fileNames'     : [],           # names of files
            'expressions'   : [],           # values for each files
            'variables'     :{              # global variables and their values
                'vars'      : [],           # variables
                'values'    : []            # values
            }, 
            'classes'       : [],           # classes loaded
            'class_names'   : [],           # class names loaded
            'functions'     : [],           # functions loaded
            'func_names'    : [],           # function names load
            'mainFuncNames' : [],           # partial function names 
            'mainClassNames': [],           # partial class names
            'modules'       : [],           # names of modules
            'modulesLoadC'  : [],           # only if any modules were not specified
            'modulesLoadF'  : [],           # only if any modules were not specified
            'init'          : [],           # initialization
            'alias'         : []            # link
        },
        'open'              : {             # dict for open function 
            'name'          : [],           # file name
            'file'          : [],           # path where the file is situated 
            'action'        : [],           # action = 'r', 'w' 'a'
            'status'        : [],           # status = 'new', 'old'
            'encoding'      : [],           # encoding = 'utf-8', 'utf-16' etc. ...
            'nonCloseKey'   : []            # if not closed after reading 
        },
        'openKey'           : False,        # open and close function 
        'closeKey'          : False,        # for open and close function
        'assigment'         : None,         # def and classes : if return function doesn't use you cannot assign to any variable
        'globalIndex'       : None,         # for the interpreter 
        'starter'           : 0,            # for the interpreter
        'subFunctionNames'  : [],           # sub-functions name for the functions 
        'subclassNames'     : [],           # sub-classes names for the classes
        'empty_values'      : None,         # when defaults values defined in a function and any values was put when running function
        'total_vars'        : None,         # total variables = (local + global) variables
        'loading'           : False,        # for delecting values which sould be printed
        'matrix'            : None
        }

        return self.data_base

    def FUNCTIONS(self):
        self.function_name  = ['integer', 'float', 'string', 'complex', 'type', 'list', 'tuple', 'boolean', 'dictionary',
                               'length', 'range', 'ansi', 'rand', 'GetLine', 'scan', 
                               'min', 'max', 'fopen', 'floor', 'License', 'help', 'matrix1']
        
        self.function_expressions   = [
            {
                'integer'           : {
                'type'              : [ ['float', 'int', 'string', 'bool'] ],                                        # input type
                'value'             : [ '0' ],                                          # default value
                'arguments'         : [ 'input' ],                                      # argument's name
                'history_of_data'   : [
                                        ( 't_int_ * input                   ', True),
                                        ('end:                              ', False )
                                      ]                                                 # history of data
                                    }
                },
            {
                'float'             : {
                'type'              : [ ['float', 'int', 'string', 'bool'] ],
                'value'             : [ '0.0' ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_float_ * input                 ', True ),
                                        ( 'end:                             ', False )
                                      ]
                                    }
                },
            {
                'string'            : {
                'type'              : [ ['any'] ],
                'value'             : [ "''" ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_string_ * input                ', True ),
                                        ( 'end:                             ', False )
                                      ]
                                    }
                },
            {
                'complex'           : {
                'type'              : [ ['float', 'int', 'string', 'bool', 'cplx'] ],
                'value'             : [ '0.0' ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_complex_ * input               ', True ),
                                        ( 'end:                             ', False )
                                      ]
                                    }
                },
            {
                'type'              : {
                'type'              : [ ['any'] ],
                'value'             : [ None ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 'ttype = ? input                       ', True ),
                                        ( 'treturn type                          ', True ),
                                        ( 'end:                                  ', False )
                                        ]
                                    }
                },
            {
                'list'              : {
                'type'              : [ ['list', 'tuple', 'range', 'dict'] ],
                'value'             : [ '()' ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_list_ * input                      ', True ),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
                },
            {
                'tuple'             : {
                'type'              : [ ['list', 'tuple', 'range', 'dict'] ],
                'value'             : [ '[]' ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_tuple_ * input                     ', True ),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
                },
            {
                'boolean'           : {
                'type'              : [ ['float', 'int', 'string', 'bool'] ],
                'value'             : [ '1.0' ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ( 't_boolean_ * input                   ', True ),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
                },
            {
                'dictionary'        : {
                'type'              : [ ['list', 'tuple', 'range', 'dict'], ['list', 'tuple', 'range', 'dict'] ],
                'value'             : [ '[ None ]', '[ None ]' ],
                'arguments'         : [ 'keys', 'values' ],
                'history_of_data'   : [
                                        ( 't_dictionary_ * keys, values         ', True ),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
            },
            {
                'length'            : {
                'type'              : [ ['string', 'tuple', 'range', 'list']   ],
                'value'             : [ None    ],
                'arguments'         : [ 'master' ],
                'history_of_data'   : [
                                        ('t_length_ * master                                            ', True),
                                        ( 'end:                                                         ', False )
                                      ]
                                    }
            },
            {
                'range'             : {
                'type'              : [ ['int'], ['int'], ['int'] ],
                'value'             : [ None, None, '1' ],
                'arguments'         : [ 'started', 'stoped', 'step' ],
                'history_of_data'   : [
                                        ('t# i am computing the range value by using 3 inputs.          ', True),
                                        ('t# the input types are integer type not any orther type       ', True),
                                        ('t# the inputs are : started with not default value            ', True),
                                        ('t#                : stopped with not default value            ', True),
                                        ('t#                : step initilazed to 1                      ', True),
                                        ('tif step == 1:                                                ', True),
                                        [
                                            ('tt_rang_ * [ started, stoped ]        ', True),
                                            ('telif step !=  1:                     ', False),
                                            ('tt_rang_ * [ started, stoped, step ]  ', True),
                                            ('telse :                               ', False),
                                            ('tt_rang_ * [ started ]                ', True),
                                            ('tend:                                 ', False)
                                        ],
                                        ('end:                                                          ', False)
                                        ]
                                    }
            },
            {
                'ansi'              : {
                'type'              : [ ['string'], ['string'] ],
                'value'             : [ '"fg"', '"W"' ],
                'arguments'         : [ 'type', 'color'],
                'history_of_data'   : [
                                        ('t# ansi found ground color                                        ', True),
                                        ('tground   = type                                                  ', True),
                                        ('tcol      = color                                                 ', True),
                                        ('t__ansii__ * ( ground, col )                                      ', True),
                                        ('end:                                                              ', False)
                                        ]
                                    }
            },
            {
                'rand'              : {
                'type'              : [ ['string'], ['tuple'] ],
                'value'             : [ '"norm"', '(0, 1)' ],
                'arguments'         : [ 'rand_type', 'input' ],
                'history_of_data'   : [
                                        ('tline = GetLine() - 1                                         ', True),
                                        ('t# computational random number by using the randomint from C  ', True),
                                        ('t# i did not use python to compute my random number           ', True),
                                        ('t# the function was not initialized it means that we need'\
                                         'to give him an tuple input type                               ', True),
                                        ('t# input = (a, b) where a and are used for the rand function  ', True),
                                        ('tif rand_type in [ "norm", "int", "unif" ]:                   ', True),
                                        [
                                            ('ttif ? input == ? ():                     ', True),
                                            [
                                                ('tttif length( input ) == 2:           ', True),
                                                [
                                                    ('ttttif rand_type in [ "int", "unif" ] :', True),
                                                    [
                                                        ('ttttt__rand__ * input, rand_type   ', True),
                                                        ('ttttelse:                          ', False),
                                                        ('tttttif ( rand_type in [ "norm" ] ) && ( input == (0, 1) ):', True),
                                                        [
                                                            ('tttttt__rand__ * input, rand_type   ', True),
                                                            ('tttttelse :', False),
                                                            ('tttttt__show__ * "{ansi(\'fg\', \'M\')}TypeError : ' \
                                                             '{ansi(\'fg\', \'C\')} << input >> {ansi(\'fg\', \'M\')} is not egal to' \
                                                             '{ansi(\'fgl\', \'B\')} (0, 1) {ansi(\'fg\', \'M\')} because of ' \
                                                             '{ansi(\'fgl\', \'Y\')} rand_type = {ansi(\'fg\', \'M\')}norm. '\
                                                             '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\', \'Y\')}{line} '\
                                                             '{ansi(\'fg\', \'C\')} in {ansi(\'fgl\', \'G\')} rand( ) function.'\
                                                             '{ansi(\'r\', \'reset\')}"             ', True),
                                                            ('tttttend:                         ', False),
                                                        ],
                                                        ('ttttend:                              ', False),
                                                    ],
                                                    ('tttt__rand__ * input, rand_type   ', True),
                                                    ('tttelse:                          ', False),
                                                    ('tttt__show__ * "{ansi(\'fg\', \'M\')}TypeError : ' \
                                                     '{ansi(\'fg\', \'C\')} length( input ) {ansi(\'fg\', \'M\')} is not egal to' \
                                                     '{ansi(\'fgl\', \'B\')} 2' \
                                                     '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\',\'Y\')}{line} '\
                                                     '{ansi(\'fg\', \'C\')} in {ansi(\'fgl\', \'G\')} rand( ) function.'\
                                                     '{ansi(\'r\', \'reset\')}"             ', True),
                                                    ('tttend:                           ', False),
                                                ],
                                                ('ttelse:                               ', False),
                                                ('ttt__show__ * "{ansi(\'fg\', \'M\')}TypeError : ' \
                                                 '{ansi(\'fg\', \'C\')} << input >> {ansi(\'fg\', \'M\')} is not' \
                                                 '{ansi(\'fgl\', \'B\')} a tuple()' \
                                                 '{ansi(\'fg\', \'M\')} type. '\
                                                 '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\', \'Y\')}{line} '\
                                                 '{ansi(\'fg\', \'C\')} in {ansi(\'fgl\', \'G\')} rand( ) function.'\
                                                 '{ansi(\'r\', \'reset\')}"                 ', True),
                                                ('ttend:                                ', False),
                                            ],
                                            ('telif rand_type in [ "rand" ] :                           ', False),
                                            ('ttif ? input == ? 1:                      ', True),
                                            [
                                                ('ttt__rand__ * input, rand_type        ', True),
                                                ('ttelse:                               ', False),
                                                ('ttt__show__ * "{ansi(\'fg\', \'M\')}TypeError : ' \
                                                 '{ansi(\'fg\', \'C\')} << input >> {ansi(\'fg\', \'M\')} is not' \
                                                 '{ansi(\'fgl\', \'R\')} an integer()' \
                                                 '{ansi(\'fg\', \'M\')} type. ' \
                                                 '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\', \'Y\')}{line} '\
                                                 '{ansi(\'fg\', \'C\')} in {ansi(\'fgl\', \'G\')} rand( ) function.' \
                                                 '{ansi(\'r\', \'reset\')}"                 ', True),
                                                ('ttend:                                ', False),
                                            ],
                                            ('telse:                                                    ', False),
                                            ('tt__show__ * "{ansi(\'fg\', \'C\')}AttributeError : ' \
                                             '{ansi(\'fg\', \'R\')} << rand_type >> {ansi(\'fgl\', \'C\')} is not in' \
                                             '{ansi(\'fg\', \'R\')} [ norm, int, unif, rand ]. ' \
                                             '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\', \'Y\')}{line} '\
                                             '{ansi(\'fg\', \'C\')} in {ansi(\'fgl\', \'G\')} rand( ) function.'\
                                             '{ansi(\'r\', \'reset\')}"                     ', True),
                                            ('tend:                                                     ', False),
                                        ],

                                        ('end:                                                          ', False),
                                        ]
                }
            },
            {
                'GetLine'           : {
                'type'              : [ ['any'] ],
                'value'             : [ None ],
                'arguments'         : [ None ],
                'history_of_data'   : [
                                        ('t_get_line_ * ""                     ', True),
                                        ('end:                                 ', False),
                                      ]
                                    }
            },
            {
                'scan'             : {
                'type'              : [ ['string'] ],
                'value'             : [ '""'     ],
                'arguments'         : [ 'input'  ],
                'history_of_data'   : [
                                        ('t__scan__ * input                         ', True),
                                        ('end:                                      ', False),
                                      ]
                }
            },
            
            {
                'min'               : {
                'type'              : [ ['list', 'tuple', 'range'] ],
                'value'             : [ None  ],
                'arguments'         : ['master'],
                'history_of_data'   : [
                                        ('t_min_ * master                           ', True),
                                        ('end:                                      ', False),
                                      ]
                }
            },
            {
                'max'               : {
                'type'              : [ ['list', 'tuple', 'range'] ],
                'value'             : [ None  ],
                'arguments'         : ['master'],
                'history_of_data'   : [
                                        ('t_max_ * master                           ', True),
                                        ('end:                                      ', False),
                                      ]
                }
            },
            {
                'fopen'             : {
                'type'              : [ ['string'], ['string'], ['string'], ['string'], ['string', 'none'] ],
                'value'             : [ None, None, None, "'new'", 'False' ],
                'arguments'         : ['name', 'file', 'action', 'status', 'encoding' ],
                'history_of_data'   : [
                                        ('t__open__ * {open : [name, file, action, status, encoding]}       ', True ),
                                        ('end:                                                              ', False),
                                        ]
                }
            },
            {
                'floor'             : {
                'type'              : [ ['float']],
                'value'             : [ None ],
                'arguments'         : ['master' ],
                'history_of_data'   : [
                                        ('tvalue    = string( master )                                      ', True ),
                                        ('tnewValue = value.split( \".\")                                   ', True ),
                                        ('tnewValue = integer( newValue[ 0 ])                               ', True ),
                                        ('treturn newValue                                                  ', True ),
                                        ('end:                                                              ', False),
                                        ]
                }
            },
            {
                'License'           : {
                'type'              : [['any']],
                'value'             : [None],
                'arguments'         : [None],
                'history_of_data'   : [
                        ('t_std_ * [\"License\", \"License\"]                         ', True),
                        ('end:                                                       ', False),
                    ]
                }
            },
            {
                'help'              : {
                'type'              : [['string']],
                'value'             : [None],
                'arguments'         : ['arg'],
                'history_of_data'   : [
                        ('t_std_ * [ arg, \"help\"]                             ', True),
                        ('end:                                                  ', False),
                    ]
                }
            },
            {
                'matrix'            : {
                'type'              : [['list', 'tuple', 'range'], ['int', 'bool'], ['int', 'bool'], ['bool'],
                                       ['string', 'none'], ['int', 'none']],
                'value'             : [None, None, None, 'False', 'None', 'None'],
                'arguments'         : ['master', 'nrow', 'ncol', 'reverse', 'ctype', 'axis'],
                'history_of_data': [
                        ('t_std_ * [master, nrow, ncol, reverse, ctype, axis, \"matrix\"]             ', True),
                        ('end:                                                  ', False),
                    ]
                }
            },
        ]

        return self.function_name, self.function_expressions



