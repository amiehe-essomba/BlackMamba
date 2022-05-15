from colorama import Fore, init, Style
from script.DATA_BASE   import ansi

class DATA_BASE:
    def __init__(self):
        pass

    def STORAGE(self):
        self.function_name, self.function_expressions = DATA_BASE().FUNCTIONS()

        self.data_base      = {
        'global_vars'       : {
            'vars'          : [],
            'values'        : []
            },
        'variables'         : {
            'vars'          : [],
            'values'        : []
            },
        'classes'           : [],
        'irene'             : None,
        'functions'         : [],
        'class_names'       : [],
        'func_names'        : [],
        'loop_for'          : [],
        'loop_while'        : [],
        'loop_until'        : [],
        'try'               : None,
        'begin'             : None,
        'if'                : [],
        'switch'            : [],
        'unless'            : [],
        'return'            : {
            'def'           : [],
            'class'         : []
            },
        'print'             : [],
        'sub_print'         : None,
        'current_func'      : None,
        'transformation'    : None,
        'no_printed_values' : [],
        'line'              : None,
        'LIB'               : {
            'func_names'    : self.function_name,
            'functions'     : self.function_expressions
            }
        }

        return self.data_base

    def FUNCTIONS(self):
        self.chaine = "'tt__show__ * {"+'ansi("fg", 34)'+"}"+"TypeError'"
        self.function_name  = ['integer', 'float', 'string', 'complex', 'type', 'list', 'tuple', 'boolean', 'dictionary',
                               'sqrt', 'length', 'sum', 'mean', 'range', 'ansi', 'square', 'rand', 'GetLine', 'scan']
        self.function_expressions   = [
            {
                'integer'              : {
                'type'              : [ 'any' ],                                        # input type
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
                'type'              : [ 'any' ],
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
                'type'              : [ 'any' ],
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
                'type'              : [ 'any' ],
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
                'type'              : [ 'any' ],
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
                'type'              : [ 'tuple' ],
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
                'type'              : [ 'list' ],
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
                'type'              : [ 'any' ],
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
                'type'              : [ 'list', 'list' ],
                'value'             : [ '[ None ]', '[ None ]' ],
                'arguments'         : [ 'keys', 'values' ],
                'history_of_data'   : [
                                        ( 't_dictionary_ * keys, values         ', True ),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
                },
            {
                'sqrt'              : {
                'type'              : [ 'any' ],
                'value'             : [ None ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ('t_sqrt_ * input                       ', True),
                                        ( 'end:                                 ', False )
                                      ]
                                    }
                },

            {
                'length'            : {
                'type'              : [ 'any'   ],
                'value'             : [ None    ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ('t_length_ * input                                            ', True),
                                        ( 'end:                                                         ', False )
                                      ]
                                    }
            },

            {
                'sum'               : {
                'type'              : [ 'any' ],
                'value'             : [ None ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ('t_sum_ * input                                                ', True),
                                        ( 'end:                                                         ', False )
                                      ]
                                    }
            },
            {
                'mean'              : {
                'type'              : [ 'any'   ],
                'value'             : [ None    ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ('t_mean_ * input                                               ', True),
                                        ('end:                                                          ', False)
                                        ]
                                    }
            },
            {
                'range'             : {
                'type'              : [ 'int', 'int', 'int' ],
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
                'type'              : [ 'string', 'string' ],
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
                'square'            : {
                'type'              : [ 'any'   ],
                'value'             : [ None    ],
                'arguments'         : [ 'input' ],
                'history_of_data'   : [
                                        ('tline     = GetLine()                                             ', True),
                                        ('t# computing of the square number                                 ', True),
                                        ('tif type( input ) in [ type( integer() ), type( float() ), type( boolean() ), '\
                                         'type( complex()) ] :',
                                                                                                                True),
                                        [
                                            ('ttreturn  input ^ 2                     ', True),
                                            ('telse  :                                ', False),
                                            ('tt__show__ * "{ansi(\'fg\', \'M\')}TypeError : '\
                                                '{ansi(\'fgl\', \'Y\')} << input >> {ansi(\'fg\', \'M\')} is not'\
                                                '{ansi(\'fg\', \'R\')} an integer()'\
                                                '{ansi(\'fg\', \'B\')} a boolean()'\
                                                '{ansi(\'fgl\', \'G\')} a float()'\
                                                '{ansi(\'fgl\', \'C\')} or a complex()'\
                                                '{ansi(\'fg\', \'M\')} type. '\
                                                '{ansi(\'fgl\', \'W\')}line : {ansi(\'fgl\', \'Y\')}{line} '\
                                                '{ansi(\'fg\', \'M\')} in {ansi(\'fgl\', \'G\')} square( ) function.'\
                                                '{ansi(\'r\', \'reset\')}"                ', True),
                                            ('tend:                                    ', False)
                                        ],
                                        ('end:                                                              ', False)
                                        ]
                }
            },
            {
                'rand'              : {
                'type'              : [ 'string', 'tuple' ],
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
                'type'              : [ 'any'],
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
                'type'              : [ 'string' ],
                'value'             : [ '""'     ],
                'arguments'         : [ 'input'  ],
                'history_of_data'   : [
                    ('t__scan__ * input                         ', True),
                    ('end:                                      ', False),
                    ]
                }
            }
        ]


        return self.function_name, self.function_expressions

    def GET_ERROR(self, _type_ : str = 'value'):
        self.value
        if _type_ == 'value': return '{}{} : {}'.format( self.ve, 'ValueError', )





