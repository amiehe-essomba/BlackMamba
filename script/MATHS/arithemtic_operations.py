from script.MATHS import arithmetic_modules

class MAGIC_MATH_BASE:
    def __init__(self, 
        master      :str, 
        data_base   :dict, 
        line        :int, 
        operator    :bool = False
        ) -> None:
        
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self._operator_     = operator
        self.math_modules   = arithmetic_modules.OPERATIONS( self.master, self.data_base, self.line, self._operator_ )

    def MATHS_OPERATIONS(self):
        self.value          = None
        self.error          = None
        
        if   MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, '0_0'):
            self.value, self.error = self.math_modules.ADD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, 's_0_0'):
            self.value, self.error = self.math_modules.SOUS()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, 'm_0_0'):
            self.value, self.error = self.math_modules.MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, 'd_0_0'):
            self.value, self.error = self.math_modules.DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, 'p_0_0'):
            self.value, self.error = self.math_modules.POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line ).OPERATORS(self.master, 'o_0_0'):
            self.value, self.error = self.math_modules.MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '1_1'):
            self.value, self.error = self.math_modules.ADD_SOUS()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '1_2'):
            self.value, self.error =  self.math_modules.ADD_MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '1_3'):
            self.value, self.error = self.math_modules.ADD_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '1_4'):
            self.value, self.error = self.math_modules.ADD_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '1_5'):
            self.value, self.error = self.math_modules.ADD_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_1'):
            self.value, self.error = self.math_modules.ADD_SOUS_MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_2'):
            self.value, self.error = self.math_modules.ADD_SOUS_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_3'):
            self.value, self.error = self.math_modules.ADD_SOUS_SQUARE()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_4'):
            self.value, self.error = self.math_modules.ADD_SOUS_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_5'):
            self.value, self.error = self.math_modules.ADD_MUL_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_6'):
            self.value, self.error = self.math_modules.ADD_MUL_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_7'):
            self.value, self.error = self.math_modules.ADD_MUL_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_8'):
            self.value, self.error = self.math_modules.ADD_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_9'):
            self.value, self.error = self.math_modules.ADD_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, self.line).OPERATORS(self.master, '2_10'):
            self.value, self.error = self.math_modules.ADD_POW_MOD()


        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_1'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_MUL_DIV()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_2'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_MUL_SQUARE()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_3'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_MUL_MOD()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_4'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_DIV_SQUARE()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_5'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_DIV_MOD()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_6'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_SOUS_SQUARE_MOD()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_7'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_MUL_DIV_SQUARE()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_8'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_MUL_DIV_MOD()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_9'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_MUL_SQUARE_MOD()

        elif MAGIC_MATH_BASE(self.master, self.data).OPERATORS(self.master, '3_10'):
            self.value, self.error = MAGIC_MATH_BASE(self.master, self.data).ADD_DIV_SQUARE_MOD()

        return self.value, self.error

    def OPERATORS(self, master, n: str):
        mask_sous   = (
                    '+' not in master and '*' not in master and '/' not in master and '^' not in master and '%' not in master)  # -
        mask_mul    = (
                    '+' not in master and '-' not in master and '/' not in master and '^' not in master and '%' not in master)  # *
        mask_div    = (
                    '+' not in master and '-' not in master and '*' not in master and '^' not in master and '%' not in master)  # /
        mask_square = (
                    '+' not in master and '-' not in master and '*' not in master and '/' not in master and '%' not in master)  # ^
        mask_mod    = (
                    '+' not in master and '*' not in master and '/' not in master and '^' not in master and '-' not in master)  # %

        mask_sous_mul       = ('+' not in master and '/' not in master and '^' not in master and '%' not in master)  # -*
        mask_sous_div       = ('*' not in master and '+' not in master and '^' not in master and '%' not in master)  # -/
        mask_sous_square    = ('*' not in master and '/' not in master and '+' not in master and '%' not in master)  # -^
        mask_sous_mod       = ('*' not in master and '/' not in master and '^' not in master and '+' not in master)  # -%

        ##########################                groupe 0            ########################################

        mask_add    = ('-' not in master and '*' not in master and '/' not in master and '^' not in master and '%' not in master)  # +

        ##########################                groupe 1            ########################################

        mask_add_sous   = (('*' not in master and '/' not in master and '^' not in master and '%' not in master) and ('+' in self.master and '-' in self.master))  # +-
        mask_add_mul    = (('-' not in master and '/' not in master and '^' not in master and '%' not in master) and ('+' in self.master and '*' in self.master))  # +*
        mask_add_div    = (('*' not in master and '-' not in master and '^' not in master and '%' not in master) and ('+' in self.master and '/' in self.master))  # +/
        mask_add_square = (('*' not in master and '/' not in master and '-' not in master and '%' not in master) and ('+' in self.master and '^' in self.master))  # +^
        mask_add_mod    = (('*' not in master and '/' not in master and '^' not in master and '-' not in master) and ('+' in self.master and '%' in self.master))  # +%

        ##########################                groupe 2            ########################################

        mask_add_sous_mul       = (('/' not in master and '^' not in master and '%' not in master) and ('+' in self.master and '-' in self.master and '*' in self.master))  # +-*
        mask_add_sous_div       = (('^' not in master and '%' not in master and '*' not in master) and ('+' in self.master and '-' in self.master and '/' in self.master))  # +-/
        mask_add_sous_square    = (('*' not in master and '/' not in master and '%' not in master) and ('+' in self.master and '-' in self.master and '^' in self.master))  # +-^
        mask_add_sous_mod       = (('/' not in master and '^' not in master and '*' not in master) and ('+' in self.master and '-' in self.master and '%' in self.master))  # +-%
        mask_add_mul_div        = (('-' not in master and '^' not in master and '%' not in master) and ('+' in self.master and '*' in self.master and '/' in self.master))  # +*/
        mask_add_mul_square     = (('-' not in master and '/' not in master and '%' not in master) and ('+' in self.master and '*' in self.master and '^' in self.master))  # +*^
        mask_add_mul_mod        = (('/' not in master and '^' not in master and '-' not in master) and ('+' in self.master and '*' in self.master and '%' in self.master))  # +*%
        mask_add_div_square     = (('-' not in master and '*' not in master and '%' not in master) and ('+' in self.master and '/' in self.master and '^' in self.master))  # +/^
        mask_add_div_mod        = (('*' not in master and '^' not in master and '-' not in master) and ('+' in self.master and '/' in self.master and '%' in self.master))  # +/%
        mask_add_square_mod     = (('/' not in master and '-' not in master and '*' not in master) and ('+' in self.master and '^' in self.master and '%' in self.master))  # +^%
        mask_sous_mul_square    = (('/' not in master and '-' in master and '*' in master) and ('+' not in self.master and '^' in self.master and '%' not in self.master))  # -*^
        mask_sous_mul_mod       = (('/' not in master and '-' in master and '*' in master) and ('+' not in self.master and '^' not in self.master and '%' in self.master))  # -*%
        mask_sous_mul_div       = (('/' in master and '-' in master and '*' in master) and ('+' not in self.master and '^' not in self.master and '%' not in self.master))  # -*/
        mask_sous_div_square    = (('/' in master and '-' in master and '*' not in master) and ('+' not in self.master and '^' in self.master and '%' not in self.master))  # -/^
        mask_sous_div_mod       = (('/' in master and '-' in master and '*' not in master) and ('+' not in self.master and '^' not in self.master and '%' in self.master))  # -/%
        mask_sous_square_mod    = (('/' not in master and '-' in master and '*' not in master) and ('+' not in self.master and '^' in self.master and '%'  in self.master))  # -^%
        mask_div_square_mod     = (('/' in master and '-' not in master and '*' not in master) and ('+' not in self.master and '^' in self.master and '%' in self.master))  # /^%

        ##########################                groupe 3            ########################################

        mask_add_sous_mul_div       = (('^' not in master and '%' not in master) and ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master))  # +-*/
        mask_add_sous_mul_square    = (('/' not in master and '%' not in master) and ('+' in self.master and '-' in self.master and '*' in self.master and '^' in self.master))  # +-*^
        mask_add_sous_mul_mod       = (('^' not in master and '/' not in master) and ('+' in self.master and '-' in self.master and '*' in self.master and '%' in self.master))  # +-*%
        mask_add_sous_div_square    = (('*' not in master and '%' not in master) and ('+' in self.master and '-' in self.master and '/' in self.master and '^' in self.master))  # +-/^
        mask_add_sous_div_mod       = (('*' not in master and '^' not in master) and ('+' in self.master and '-' in self.master and '/' in self.master and '%' in self.master))  # +-/%
        mask_add_sous_square_mod    = (('*' not in master and '/' not in master) and ('+' in self.master and '-' in self.master and '^' in self.master and '%' in self.master))  # +-^%
        mask_add_mul_div_square     = (('-' not in master and '%' not in master) and ('+' in self.master and '*' in self.master and '/' in self.master and '^' in self.master))  # +*/^
        mask_add_mul_div_mod        = (('-' not in master and '^' not in master) and ('+' in self.master and '*' in self.master and '/' in self.master and '%' in self.master))  # +*/%
        mask_add_mul_square_mod     = (('-' not in master and '/' not in master) and ('+' in self.master and '*' in self.master and '^' in self.master and '%' in self.master))  # +*^%
        mask_add_div_square_mod     = (('-' not in master and '*' not in master) and ('+' in self.master and '/' in self.master and '^' in self.master and '%' in self.master))  # +/^%

        ##########################                groupe 4            ########################################

        mask_add_sous_mul_div_square    = (('%' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '^' in self.master))  # +-*/^
        mask_add_sous_mul_div_mod       = (('^' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '%' in self.master))  # +-*/%
        mask_add_sous_mul_square_mod    = (('/' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '^' in self.master and '%' in self.master))  # +-*^%
        mask_add_sous_div_square_mod    = (('*' not in self.master) and ('+' in self.master and '-' in self.master and '/' in self.master and '^' in self.master and '%' in self.master))  # +-/^%
        mask_add_mul_div_square_mod     = (('-' not in self.master) and ('+' in self.master and '*' in self.master and '/' in self.master and '^' in self.master and '%' in self.master))  # +*/^%


        ##########################                groupe 5            ########################################

        mask_add_sous_mul_div_square_mod = ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '^' in self.master and '%' in self.master)  # +-*/^%

        #######################################################################################################

        if n == '0_0':
            return mask_add
        elif n == '1_1':
            return mask_add_sous
        elif n == '1_2':
            return mask_add_mul
        elif n == '1_3':
            return mask_add_div
        elif n == '1_4':
            return mask_add_square
        elif n == '1_5':
            return mask_add_mod
        elif n == '2_1':
            return mask_add_sous_mul
        elif n == '2_2':
            return mask_add_sous_div
        elif n == '2_3':
            return mask_add_sous_square
        elif n == '2_4':
            return mask_add_sous_mod
        elif n == '2_5':
            return mask_add_mul_div
        elif n == '2_6':
            return mask_add_mul_square
        elif n == '2_7':
            return mask_add_mul_mod
        elif n == '2_8':
            return mask_add_div_square
        elif n == '2_9':
            return mask_add_div_mod
        elif n == '2_10':
            return mask_add_square_mod
        elif n == '3_1':
            return mask_add_sous_mul_div
        elif n == '3_2':
            return mask_add_sous_mul_square
        elif n == '3_3':
            return mask_add_sous_mul_mod
        elif n == '3_4':
            return mask_add_sous_div_square
        elif n == '3_5':
            return mask_add_sous_div_mod
        elif n == '3_6':
            return mask_add_sous_square_mod
        elif n == '3_7':
            return mask_add_mul_div_square
        elif n == '3_8':
            return mask_add_mul_div_mod
        elif n == '3_9':
            return mask_add_mul_square_mod
        elif n == '3_10':
            return mask_add_div_square_mod
        elif n == '4_1':
            return mask_add_sous_mul_div_square
        elif n == '4_2':
            return mask_add_sous_mul_div_mod
        elif n == '4_3':
            return mask_add_sous_mul_square_mod
        elif n == '4_4':
            return mask_add_sous_div_square_mod
        elif n == '4_5':
            return mask_add_mul_div_square_mod
        elif n == '5_0':
            return mask_add_sous_mul_div_square_mod
        elif n == 'm_0_0':
            return mask_mul
        elif n == 's_0_0':
            return mask_sous
        elif n == 'p_0_0':
            return mask_square
        elif n == 'o_0_0':
            return mask_mod
        elif n == 'd_0_0':
            return mask_div