from colorama import Fore
from script.MATHS import arithmetic_object
from script.MATHS import arithmetic_calculations
from script.LEXER import particular_str_selection
from script.MATHS import deep_checking

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class MATHS:
    def __init__(self, master: list, data_base: dict, history_of_operators: str, line: int ):
        self.master                 = master
        self.data_base              = data_base
        self.line                   = line
        self.arithmetic             = arithmetic_object.ARITHMETICS(self.data_base, self.line)
        self.history_of_operators   = history_of_operators

    def ADD( self )         :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, _  = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        if len( self.storage ) > 1:
            self.sum = self.storage[ 0 ]

            for value in self.storage[ 1 : ]:
                self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                if self.error is None : pass
                else: break
            self.result = self.sum

        else: self.result = self.storage[ 0 ]

        return self.result, self.error
    def SOUS(self)          :
        self.result         = None
        self.error          = None
        self.storage        = []
        self.vector         = False
        self.storage, self.operators, _ = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()
        if len( self.storage ) > 1:
            if len( self.storage ) < len( self.operators ):
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
            else: self.sous = self.storage[ 0 ]

            if self.error is None:
                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break

                self.result = self.sous

            else: self.error = self.error

        else:
            self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
            if self.error is None: self.result = self.sous
            else: pass

        return self.result, self.error
    def MUL( self )         :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        
        self.storage, self.operators, _  = SPLIT_DATA( self.master, '*', self.history_of_operators ).SPLIT()

        self.mul = self.storage[ 0 ]
        for value in self.storage[ 1 : ]:
            self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
            if self.error is None : pass
            else: break

        self.result = self.mul

        return self.result, self.error
    def DIV( self )         :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.storage, self.operators, _  = SPLIT_DATA( self.master, '/', self.history_of_operators ).SPLIT()

        self.mul = self.storage[ 0 ]
        for value in self.storage[ 1 : ]:
            self.mul, self.error = self.arithmetic.OBJECT_DIV( self.mul, value )
            if self.error is None : pass
            else: break

        self.result = self.mul

        return self.result, self.error
    def POW( self )         :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, _  = SPLIT_DATA( self.master, '^', self.history_of_operators ).SPLIT()
        self.pow = self.storage[ 0 ]
        for value in self.storage[ 1 : ]:
            self.pow, self.error = self.arithmetic.OBJECT_SQUARE( self.pow, value )
            if self.error is None : pass
            else: break

        self.result = self.pow

        return self.result, self.error
    def MOD( self )         :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.storage, self.operators, _  = SPLIT_DATA( self.master, '%', self.history_of_operators ).SPLIT()

        self.mul = self.storage[ 0 ]
        for value in self.storage[ 1 : ]:
            self.mul, self.error = self.arithmetic.OBJECT_MOD( self.mul, value )
            if self.error is None : pass
            else: break

        self.result = self.mul

        return self.result, self.error
    def ADD_SOUS( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()
        for i in self.index:
            self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_DIV( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            if self.error is None:
                self.storage[ i ] = self.div
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.pow, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
            if self.error is None:
                self.storage[ i ] = self.pow
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.mod, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MOD()
            if self.error is None:
                self.storage[ i ] = self.mod
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def SOUS_MUL( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        
        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_DIV( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            if self.error is None:
                self.storage[ i ] = self.div
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.key            = False
        
        if self.master[ 0 ] == '-':
            if self.history_of_operators[0] == '-' and self.history_of_operators[1] == '^':
                self.new_value = self.master[1][0] * (-1)
                self.master[1] = [self.new_value]
                del self.master[0]
                self.history_of_operators = self.history_of_operators[1:]
                self.key = True
            else: pass
        else: pass

        if '-' not in list(self.history_of_operators):
            self.storage, self.operators, self.index = SPLIT_DATA(self.master, '^', self.history_of_operators).SPLIT()
            self.pow = self.storage[0]
            for value in self.storage[1:]:
                self.pow, self.error = self.arithmetic.OBJECT_SQUARE(self.pow, value)
                if self.error is None:
                    pass
                else:
                    break

            if type(self.pow) == type(complex()):
                self.result = complex(str(self.pow.imag) + 'j')
            else:
                self.result = self.pow

        else:
            self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()
            for i in self.index:
                self.pow, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
                if self.error is None:
                    self.storage[ i ] = self.pow
                else: self.error = self.error

            if self.error is None:
                if len( self.storage ) > 1:
                    if self.key is False:
                        if len( self.storage ) < len( self.operators ):
                            self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                        else:
                            self.sous = self.storage[ 0 ]
                    else:
                        self.sous = self.storage[ 0 ]
                    for value in self.storage[ 1 : ]:
                        self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                        if self.error is None : pass
                        else: break
                    self.result = self.sous

                else:
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                    if self.error is None: self.result = self.sous
                    else: pass
            else : pass

        return self.result, self.error
    def SOUS_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.mod, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MOD()
            if self.error is None:
                self.storage[ i ] = self.mod
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def MUL_DIV( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '*', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            if self.error is None:
                self.storage[ i ] = self.div
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def MUL_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '*', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.pow, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
            if self.error is None:
                self.storage[ i ] = self.pow
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def MUL_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.type_inv       = None
        self.type           = None

        for string in list( self.history_of_operators ):
            if string in ['*', '%']:
                self.type = string
                break
            else: pass

        if self.type == '*': self.type_inv = '%'
        else: self.type_inv = '*'

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, self.type_inv, self.history_of_operators ).SPLIT()

        for i in self.index:
            self.multi_type                     = None
            if self.type  in [ '*' ]:
                self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            else:
                self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MOD()

            if self.error is None:
                self.storage[ i ] = self.multi_type
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    if self.type_inv in [ '*' ] :
                        self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    else:
                        self.mul, self.error = self.arithmetic.OBJECT_MOD( self.mul, value )
                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def DIV_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '/', self.history_of_operators ).SPLIT()

        for i in self.index:
            self.pow, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()

            if self.error is None:
                self.storage[ i ] = self.pow
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.div = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.div, self.error = self.arithmetic.OBJECT_DIV( self.div, value )
                    if self.error is None : pass
                    else: break
                self.result = self.div

            else: self.result = self.storage[ 0 ]
        else : pass

        return self.result, self.error
    def DIV_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.type_inv       = None
        self.type           = None

        for string in list( self.history_of_operators ):
            if string in ['/', '%']:
                self.type = string
                break
            else: pass

        if self.type == '/': self.type_inv = '%'
        else: self.type_inv = '/'

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, self.type_inv, self.history_of_operators ).SPLIT()

        for i in self.index:
            self.multi_type                     = None
            if self.type  in [ '/' ]:
                self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            else:
                self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MOD()

            if self.error is None:
                self.storage[ i ] = self.multi_type
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.div = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    if self.type_inv in [ '/' ] :
                        self.div, self.error = self.arithmetic.OBJECT_DIV( self.div, value )
                    else:
                        self.div, self.error = self.arithmetic.OBJECT_MOD( self.div, value )
                    if self.error is None : pass
                    else: break
                self.result = self.div

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '%', self.history_of_operators ).SPLIT()
        for i in self.index:
            self.pow, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()

            if self.error is None:
                self.storage[ i ] = self.pow
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mod = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.mod, self.error = self.arithmetic.OBJECT_MOD( self.mod, value )
                    if self.error is None : pass
                    else: break
                self.result = self.mod

            else: self.result = self.storage[ 0 ]
        else : pass

        return self.result, self.error
    def ADD_SOUS_MUL( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_DIV( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '-' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '-' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '-' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_DIV( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_DIV_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_DIV_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
            elif '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def SOUS_MUL_DIV( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            else:
                self.mul, self.error = MATHS(self.storage[i], self.data_base, self.operators[ i ], self.line).MUL_DIV()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_MUL_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            else:
                self.mul, self.error = MATHS(self.storage[i], self.data_base, self.operators[ i ], self.line).MUL_POW()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_MUL_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '*' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.mul, self.error = MATHS(self.storage[i], self.data_base, self.operators[ i ], self.line).MUL_MOD()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_DIV_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            else:
                self.mul, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_DIV_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.mul, self.error = MATHS(self.storage[i], self.data_base, self.operators[ i ], self.line).DIV_MOD()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def SOUS_POW_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '-', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
            elif '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.mul, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            else:
                self.mul, self.error = MATHS(self.storage[i], self.data_base, self.operators[ i ], self.line).POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.mul
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                if len( self.storage ) < len( self.operators ):
                    self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1)
                else:
                    self.sous = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sous, self.error = self.arithmetic.OBJECT_SOUS( self.sous, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sous

            else:
                self.sous, self.error = self.arithmetic.OBJECT_MUL( self.storage[ 0 ], -1 )
                if self.error is None: self.result = self.sous
                else: pass

        else : pass

        return self.result, self.error
    def MUL_DIV_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '*', self.history_of_operators ).SPLIT()

        for i in self.index:
            if '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()
            else:
                self.div, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.div
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def MUL_DIV_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.type_inv1      = None
        self.type_inv2      = None
        self.type           = None

        for string in list( self.history_of_operators ):
            if string in ['*', '%', '/']:
                if self.type is None:
                    self.type = string
                else:
                    if string != self.type:
                        if self.type_inv1 is None:
                            self.type_inv1 = string
                        else:
                            if string != self.type_inv1:
                                self.type_inv2 = string
                                break
                            else: pass
                    else: pass
            else: pass

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, self.type_inv1, self.history_of_operators ).SPLIT()

        for i in self.index:
            self.multi_type                     = None
            if self.type  in list( self.operators[ i ] ) and self.type_inv2 not in list( self.operators[ i ] ):
                if self.type == '*':
                    self.multi_type, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
                elif self.type == '/':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
                elif self.type == '%':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()

            elif self.type  not in list( self.operators[ i ] ) and self.type_inv2 in list( self.operators[ i ] ):
                if self.type_inv2 == '*':
                    self.multi_type, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
                elif self.type_inv2 == '/':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
                elif self.type_inv2 == '%':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()

            else:
                if ( self.type == '*' and self.type_inv2 == '/' ) or ( self.type == '/' and self.type_inv2 == '*' ):
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL_DIV()
                elif ( self.type == '*' and self.type_inv2 == '%' ) or ( self.type == '%' and self.type_inv2 == '*' ):
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL_MOD()
                elif ( self.type == '/' and self.type_inv2 == '%' ) or ( self.type == '%' and self.type_inv2 == '/' ) :
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV_MOD()

            if self.error is None:
                self.storage[ i ] = self.multi_type
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    if self.type_inv1 == '*' :
                        self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    elif self.type_inv1 == '%' :
                        self.mul, self.error = self.arithmetic.OBJECT_MOD( self.mul, value )
                    else:
                        self.mul, self.error = self.arithmetic.OBJECT_DIV( self.mul, value )

                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]
        else : pass

        return self.result, self.error
    def MUL_POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.type           = None
        self.type_inv       = None

        for string in list( self.history_of_operators ):
            if string in ['%', '*']:
                self.type = string
                break
            else: pass

        if self.type == '%': self.type_inv = '*'
        else: self.type_inv = '%'
        self.storage, self.operators, self.index = SPLIT_DATA( self.master, self.type_inv, self.history_of_operators ).SPLIT()

        for i in self.index:
            self.multi_type                     = None
            if self.type  in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                if self.type == '*':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL()
                elif self.type == '%':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()

            elif self.type  not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.multi_type, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()

            else:
                if  self.type == '*':
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL_POW()
                elif self.type == '%' :
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.multi_type
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    if self.type_inv == '*' :
                        self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, value )
                    elif self.type_inv == '%' :
                        self.mul, self.error = self.arithmetic.OBJECT_MOD( self.mul, value )

                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]
        else : pass

        return self.result, self.error
    def DIV_POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.type           = None
        self.type_inv       = None

        for string in list( self.history_of_operators ):
            if string in ['%', '/']:
                self.type = string
                break
            else: pass

        if self.type == '%': self.type_inv = '/'
        else: self.type_inv = '%'
        self.storage, self.operators, self.index = SPLIT_DATA( self.master, self.type_inv, self.history_of_operators ).SPLIT()

        for i in self.index:
            self.multi_type                     = None
            if self.type  in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                if self.type == '/':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
                elif self.type == '%':
                    self.multi_type, self.error = MATHS(self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()

            elif self.type  not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.multi_type, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW()

            else:
                if  self.type == '/':
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV_POW()
                elif self.type == '%' :
                    self.multi_type, self.error     = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.multi_type
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.mul = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    if self.type_inv == '/' :
                        self.mul, self.error = self.arithmetic.OBJECT_DIV( self.mul, value )
                    elif self.type_inv == '%' :
                        self.mul, self.error = self.arithmetic.OBJECT_MOD( self.mul, value )

                    if self.error is None : pass
                    else: break
                self.result = self.mul

            else: self.result = self.storage[ 0 ]
        else : pass

        return self.result, self.error
    def ADD_SOUS_MUL_DIV( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL()
            elif '-' not in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            elif '-' in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL()
            elif '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL_DIV()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_MUL_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL()
            elif '-' not in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '-' in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL()
            elif '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_POW()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_MUL_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL()
            elif '-' not in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '-' in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL()
            elif '-' in list( self.operators[ i ] ) and '*' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MOD()
            elif '-' not in list( self.operators[ i ] ) and '*' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MUL_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_DIV_POW( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            elif '-' not in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '-' in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV()
            elif '-' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_POW()
            elif '-' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_DIV_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            elif '-' not in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '-' in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV()
            elif '-' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MOD()
            elif '-' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_SOUS_POW_MOD( self )    :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '-' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).SOUS()
            elif '-' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '-' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '-' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_POW()
            elif '-' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_MOD()
            elif '-' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).SOUS_POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_DIV_POW( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            elif '*' not in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '*' in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV()
            elif '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_POW()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV_POW()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_DIV_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV()
            elif '*' not in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '*' in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV()
            elif '*' in list( self.operators[ i ] ) and '/' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_MOD()
            elif '*' not in list( self.operators[ i ] ) and '/' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_DIV_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_MUL_POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).MUL()
            elif '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '*' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '*' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_POW()
            elif '*' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_MOD()
            elif '*' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MUL_POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error
    def ADD_DIV_POW_MOD( self )     :
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.storage, self.operators, self.index = SPLIT_DATA( self.master, '+', self.history_of_operators ).SPLIT()

        for i in self.index:
            if   '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line ).DIV()
            elif '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW()
            elif '/' not in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).MOD()
            elif '/' in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' not in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW()
            elif '/' in list( self.operators[ i ] ) and '^' not in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_MOD()
            elif '/' not in list( self.operators[ i ] ) and '^' in list( self.operators[ i ] ) and '%' in list( self.operators[ i ] ):
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).POW_MOD()
            else:
                self.sous, self.error = MATHS( self.storage[ i ], self.data_base, self.operators[ i ], self.line).DIV_POW_MOD()

            if self.error is None:
                self.storage[ i ] = self.sous
            else: break

        if self.error is None:
            if len( self.storage ) > 1:
                self.sum = self.storage[ 0 ]

                for value in self.storage[ 1 : ]:
                    self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, value )
                    if self.error is None : pass
                    else: break
                self.result = self.sum

            else: self.result = self.storage[ 0 ]

        else : pass

        return self.result, self.error

class OPERATIONS:
    def __init__(self, master:str, data_base:dict, line:int, operator: bool = False):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.arithmetic     = arithmetic_object.ARITHMETICS( self.data_base, self.line )
        self.calculation    = arithmetic_calculations
        self.selection      = particular_str_selection
        self._operator_     = operator

    def ADD(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        #if self._operator_ is True:
        self.string, self.error = self.selection.SELECTION( self.master, self.master, self.data_base,
                                                                      self.line ).CHAR_SELECTION( '+' )
        self.string = deep_checking.DEEP_CHECKING( self.string[ : ]).CHECKING('+')
        #else:
        #    self.string = [ self.master ]

        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')
                    self.value, self.error =   self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )

                    else:
                        self.error = self.error
                        break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[0]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS(self):
        self.result         = None
        self.error          = None
        self.storage        = []
        self.vector         = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '-' )
        self.string = deep_checking.DEEP_CHECKING(self.string[ : ]).CHECKING('-')

        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector     = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()

                    if self.error is None:
                        self.storage.append( self.value )

                    else:
                        break

                else:
                    pass

            if self.error is None:
                if self.vector  == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[ 1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '*' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                str_ = str_.replace("'", '"')
                self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()

                if self.error is None:
                    self.storage.append( self.value )

                else:
                    break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.mul = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.mul

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def DIV(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '/' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                str_ = str_.replace("'", '"')
                self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()

                if self.error is None:
                    self.storage.append( self.value )

                else:
                    break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.div = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.div, self.error = self.arithmetic.OBJECT_DIV( self.div, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.div

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def POW(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '^' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                str_ = str_.replace("'", '"')
                self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()

                if self.error is None:
                    self.storage.append( self.value )

                else:
                    break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.pow = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.pow, self.error = self.arithmetic.OBJECT_SQUARE( self.pow, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.pow

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MOD(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '%' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                str_ = str_.replace("'", '"')
                self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()

                if self.error is None:
                    self.storage.append( self.value )

                else:
                    break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.mod = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.mod, self.error = self.arithmetic.OBJECT_MOD( self.mod, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.mod

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_SOUS(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '-' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).SOUS( )
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[0]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_MUL(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '*' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).MUL( )
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[0]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_DIV(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '/' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).DIV( )
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[0]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_POW(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).POW( )
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_MOD(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '%' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).MOD( )
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[0]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_MUL(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '-' )
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '*' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_DIV(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '-' )
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '/' in str_:
                        self.value , self.error = OPERATIONS( str_, self.data_base, self.line ).DIV()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[ 1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '-' )
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_:
                        self.value , self.error = OPERATIONS( str_, self.data_base, self.line ).POW()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL( -1, self.storage[ 0 ] )

                else:
                    pass

                if self.error is None:
                    if len( self.storage ) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[ 1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '%' in str_:
                        self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).MOD()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len( self.storage ) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_DIV(self):
        self.result         = None
        self.error          = None
        self.storage        = [ ]
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '*' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                str_ = str_.replace("'", '"')

                if '/' in str_:
                    self.value, self.error = OPERATIONS( str_, self.data_base, self.line ).DIV()
                    if self.error is None :
                        self.storage.append( self.value )
                    else:
                        break
                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.mul = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.mul, self.error = self.arithmetic.OBJECT_MUL( self.mul, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.mul

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['*', '^']:
                self.type = q
                break
            else:
                pass

        if self.type == '*':
            self.type_inv = '^'
        else:
            self.type_inv = '*'
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')
                if self.type_inv in str_:
                    if self.type_inv in [ '*' ]:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len(self.storage) > 1:
                    self.mul = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '*' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_MUL(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_SQUARE(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['*', '%']:
                self.type = q
                break
            else:
                pass

        if self.type == '*':
            self.type_inv = '%'
        else:
            self.type_inv = '*'
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type_inv in str_:
                    if self.type_inv in [ '*' ]:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len( self.storage ) > 1:
                    self.mul = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '*' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_MUL(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_MOD(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def DIV_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['/', '^']:
                self.type = q
                break
            else:
                pass

        if self.type == '/':
            self.type_inv = '^'
        else:
            self.type_inv = '/'

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')
                if self.type_inv in str_:
                    if self.type_inv in [ '/' ]:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len(self.storage) > 1:
                    self.div = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '/' ]:
                            self.div, self.error = self.arithmetic.OBJECT_DIV( self.div, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.div, self.error = self.arithmetic.OBJECT_SQUARE( self.div, val )
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.div

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def DIV_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['/', '%']:
                self.type = q
                break
            else:
                pass

        if self.type == '/':
            self.type_inv = '%'
        else:
            self.type_inv = '/'

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type_inv in str_:
                    if self.type_inv in [ '/' ]:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len(self.storage) > 1:
                    self.div = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '/' ]:
                            self.div, self.error = self.arithmetic.OBJECT_DIV( self.div, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.div, self.error = self.arithmetic.OBJECT_MOD( self.div, val )
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.div

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def POW_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['%', '^']:
                self.type = q
                break
            else:
                pass

        if self.type == '^':
            self.type_inv = '%'
        else:
            self.type_inv = '^'

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type_inv in str_:
                    if self.type_inv in [ '^' ]:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                    if self.error is None:
                        self.storage.append( self.value )
                    else:
                        break

            if self.error is None:

                if len(self.storage) > 1:
                    self.pow_mod = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '^' ]:
                            self.pow_mod, self.error = self.arithmetic.OBJECT_SQUARE( self.pow_mod, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.pow_mod, self.error = self.arithmetic.OBJECT_MOD( self.pow_mod, val )
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.pow_mod

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_SOUS_MUL(self):
        self.error      = None
        self.result     = None
        self.storage    = []

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                         self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '-' in str_ and '*' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '-' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '-' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS_MUL()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break
                else:
                    pass

            if self.error is None:
                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_SOUS_DIV(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '-' in str_ and '/' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '-' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '-' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS_DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_SOUS_POW(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '-' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '^' in str_ and '-' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '-' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS_POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_SOUS_MOD(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '-' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '%' in str_ and '-' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '%' in str_ and '-' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).SOUS_MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_MUL_DIV(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '/' in str_ and '*' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '/' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '/' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_MUL_POW(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_ and '*' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_MUL_MOD(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '%' in str_ and '*' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '*' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_DIV_POW(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_ and '/' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_DIV_MOD(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '/' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '%' in str_ and '/' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '/' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def ADD_POW_MOD(self):
        self.error      = None
        self.result     = None
        self.storage    = []
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '+' )
        if self.error is None:
            for i, str_ in enumerate( self.string ):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '%' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    elif '%' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW_MOD()
                        if self.error == None:
                            self.storage.append( self.value )
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error == None:
                            self.storage.append(self.value)
                        else:
                            self.err = self.err
                            break

                else:
                    pass

            if self.error is None:

                if len( self.storage ) > 1:
                    self.sum = self.storage[ 0 ]
                    for val in self.storage[ 1 : ]:
                        self.sum, self.error = self.arithmetic.OBJECT_ADD( self.sum, val )
                        if self.error is None :
                            pass
                        else:
                            break

                    self.result = self.sum

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_MUL_DIV(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( '-' )
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '*' in str_ and '/' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' not in str_ and '/' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '/' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_MUL_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '*' in str_ and '^' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' not in str_ and '^' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_MUL_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '*' in str_ and '%' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' not in str_ and '%' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_DIV_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_ and '/' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' not in str_ and '/' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '/' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_DIV_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '%' in str_ and '/' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '%' not in str_ and '/' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '%' in str_ and '/' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def SOUS_POW_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.vector     = False
        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION('-')
        if self.error is None:
            if self.string[ 0 ] in [ '' ]:
                self.vector = True
            else:
                pass

            for i, str_ in enumerate(self.string):
                if str_ != '':
                    str_ = str_.replace("'", '"')

                    if '^' in str_ and '%' not in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' not in str_ and '%' in str_:
                        self.value , self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '%' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                 self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                else:
                    pass

            if self.error is None:
                if self.vector == True:
                    self.storage[ 0 ], self.error = self.arithmetic.OBJECT_MUL(-1, self.storage[ 0 ])

                else:
                    pass

                if self.error is None:
                    if len(self.storage) > 1:
                        self.sum = self.storage[ 0 ]
                        for val in self.storage[1 : ]:
                            self.sum, self.error = self.arithmetic.OBJECT_SOUS( self.sum, val )
                            if self.error is None:
                                pass
                            else:
                                break

                        self.result = self.sum

                    else:
                        self.result = self.storage[ 0 ]

                else:
                    pass

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_DIV_POW(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv   = None

        for q in self.master:
            if q in ['*', '^']:
                self.type = q
                break
            else:
                pass

        if self.type == '*':
            self.type_inv = '^'
        else:
            self.type_inv = '*'

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION( self.type )
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type_inv in str_:
                    if self.type_inv in [ '*' ]:
                        if '/' not in str_ and '*' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break
                        elif '/' in str_ and '*' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_DIV()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break

                    else:
                        if '/' not in str_ and '^' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break
                        elif '/' in str_ and '^' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_POW()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break

                else:
                    if '/' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE( str_, self.data_base,
                                                                                     self.line ).ARITHMETIC()
                        if self.error is None:
                            self.storage.append( self.value )
                        else:
                            break

            if self.error is None:

                if len(self.storage) > 1:
                    self.mul = self.storage[ 0 ]
                    for val in self.storage[1 : ]:
                        if self.type in [ '*' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_MUL(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_SQUARE(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul

                else:
                    self.result = self.storage[ 0 ]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_DIV_MOD(self):
        self.result = None
        self.error = None
        self.storage = []
        self.type = None
        self.type_inv = None

        for q in self.master:
            if q in ['*', '%']:
                self.type = q
                break
            else:
                pass

        if self.type == '*':
            self.type_inv = '%'
        else:
            self.type_inv = '*'

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION(self.type)
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type_inv in str_:
                    if self.type_inv in ['*']:
                        if '/' not in str_ and '*' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break
                        elif '/' in str_ and '*' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_DIV()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break

                    else:
                        if '/' not in str_ and '%' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break
                        elif '/' in str_ and '%' in str_:
                            self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_MOD()
                            if self.error is None:
                                self.storage.append(self.value)
                            else:
                                break

                else:
                    if '/' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

            if self.error is None:
                if len(self.storage) > 1:
                    self.mul = self.storage[0]
                    for val in self.storage[1:]:
                        if self.type in ['*']:
                            self.mul, self.error = self.arithmetic.OBJECT_MUL(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break
                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_MOD(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul
                else:
                    self.result = self.storage[0]
            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def MUL_POW_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv1  = None
        self.type_inv2  = None

        for q in self.master:
            if q in ['*', '^', '%']:
                self.type = q
                break
            else:
                pass

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION(self.type)
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type == '*':
                    if '^' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' not in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                elif self.type == '^':
                    if '*' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' not in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                else:
                    if '*' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' not in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MUL_POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

            if self.error is None:
                if len(self.storage) > 1:
                    self.mul = self.storage[0]
                    for val in self.storage[1:]:
                        if self.type in [ '*' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_MUL(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break
                        elif self.type in [ '^' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_SQUARE(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break
                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_MOD(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul
                else:
                    self.result = self.storage[0]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

    def DIV_POW_MOD(self):
        self.result     = None
        self.error      = None
        self.storage    = []
        self.type       = None
        self.type_inv1  = None
        self.type_inv2  = None

        for q in self.master:
            if q in ['/', '^', '%']:
                self.type = q
                break
            else:
                pass

        self.string, self.error = self.selection.SELECTION(self.master, self.master, self.data_base,
                                                           self.line).CHAR_SELECTION(self.type)
        if self.error is None:
            for i, str_ in enumerate(self.string):
                str_ = str_.replace("'", '"')

                if self.type == '/':
                    if '^' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' not in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '^' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                elif self.type == '^':
                    if '/' in str_ and '%' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '/' not in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '*' in str_ and '%' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_MOD()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                else:
                    if '/' in str_ and '^' not in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '/' not in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    elif '/' in str_ and '^' in str_:
                        self.value, self.error = OPERATIONS(str_, self.data_base, self.line).DIV_POW()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break
                    else:
                        self.value, self.error = self.calculation.MAGIC_MATH_BASE(str_, self.data_base,
                                                                                  self.line).ARITHMETIC()
                        if self.error is None:
                            self.storage.append(self.value)
                        else:
                            break

            if self.error is None:
                if len(self.storage) > 1:
                    self.mul = self.storage[0]
                    for val in self.storage[1:]:
                        if self.type in [ '/' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_DIV(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break
                        elif self.type in [ '^' ]:
                            self.mul, self.error = self.arithmetic.OBJECT_SQUARE(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break
                        else:
                            self.mul, self.error = self.arithmetic.OBJECT_MOD(self.mul, val)
                            if self.error is None:
                                pass
                            else:
                                break

                    self.result = self.mul
                else:
                    self.result = self.storage[0]

            else:
                pass
        else:
            self.error = self.error

        return self.result, self.error

class SPLIT_DATA:
    def __init__(self, master: list, operator: str, history_of_operators: str):
        self.master                 = master
        self.operator               = operator
        self.history_of_operators   = history_of_operators

    def SPLIT(self):
        self._return_       = []
        self.index_value    = []
        self.double_index   = []
        self.index_sum      = 0
        self.return_index   = []

        for i, values in enumerate( self.master ):
            if i < len( self.master ) - 1:
                if values == self.operator:
                    if not self.index_value:
                        if len( self.master[ : i] ) > 1:
                            self._return_.append( self.master[ : i] )
                            self.return_index.append( len( self._return_ ) - 1 )
                        else:
                            try:
                                self._return_.append( self.master[ : i ][ 0 ])
                                self.double_index.append( len( self._return_ ) - 1 )
                            except IndexError: pass

                        self.index_value.append( i )

                    else:
                        j = self.index_value[ -1 ] + 1
                        if len( self.master[ j : i] ) > 1:
                            self._return_.append( self.master[ j : i] )
                            self.return_index.append( len( self._return_ ) - 1 )
                        else:
                            self._return_.append( self.master[ j : i ][ 0 ] )
                            self.double_index.append( len( self._return_ ) - 1 )

                        self.index_value.append( i )

                else: self.index_sum += 1

            else:
                if not self.index_value:
                    self._return_ = self.master[ : ]
                else:
                    j = self.index_value[ -1 ] + 1
                    if len( self.master[ j : ] ) > 1:
                        self._return_.append( self.master[ j : ] )
                        self.return_index.append( len( self._return_ ) - 1 )
                    else:
                        self._return_.append(self.master[ j : ][ 0 ] )
                        self.double_index.append( len( self._return_ ) - 1 )

        for i in self.double_index:
                self._return_[ i ] = self._return_[ i ][ 0 ]

        return self._return_, self.history_of_operators.split( self.operator ), self.return_index











