from script.MATHS import arithmetic_modules

class MAGIC_MATH_BASE:
    def __init__(self, master:str, data_base:dict, history_of_operators: str, line: int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.history_of_operators   = history_of_operators
        self.math_modules   = arithmetic_modules.MATHS(self.master, self.data_base, self.history_of_operators, self.line )

    def MATHS_OPERATIONS(self, name: str = 'python' ):
        self.value                  = None
        self.error                  = None

        if   MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, '0_0'):
            self.value, self.error = self.math_modules.ADD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, 's_0_0'):
            self.value, self.error = self.math_modules.SOUS()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, 'm_0_0'):
            self.value, self.error = self.math_modules.MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, 'd_0_0'):
            self.value, self.error = self.math_modules.DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, 'p_0_0'):
            self.value, self.error = self.math_modules.POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line ).OPERATORS(self.history_of_operators, 'o_0_0'):
            self.value, self.error = self.math_modules.MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '1_1'):
            self.value, self.error = self.math_modules.ADD_SOUS()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '1_2'):
            self.value, self.error = self.math_modules.ADD_MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '1_3'):
            self.value, self.error = self.math_modules.ADD_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '1_4'):
            self.value, self.error = self.math_modules.ADD_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '1_5'):
            self.value, self.error = self.math_modules.ADD_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_m'):
            self.value, self.error = self.math_modules.SOUS_MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_d'):
            self.value, self.error = self.math_modules.SOUS_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_p'):
            self.value, self.error = self.math_modules.SOUS_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_o'):
            self.value, self.error = self.math_modules.SOUS_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_d'):
            self.value, self.error = self.math_modules.MUL_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_p'):
            self.value, self.error = self.math_modules.MUL_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_o'):
            self.value, self.error = self.math_modules.MUL_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'd_p'):
            self.value, self.error = self.math_modules.DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'd_o'):
            self.value, self.error = self.math_modules.DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'p_o'):
            self.value, self.error = self.math_modules.POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_1'):
            self.value, self.error = self.math_modules.ADD_SOUS_MUL()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_2'):
            self.value, self.error = self.math_modules.ADD_SOUS_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_3'):
            self.value, self.error = self.math_modules.ADD_SOUS_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_4'):
            self.value, self.error = self.math_modules.ADD_SOUS_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_5'):
            self.value, self.error = self.math_modules.ADD_MUL_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_5'):
            self.value, self.error = self.math_modules.ADD_MUL_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_7'):
            self.value, self.error = self.math_modules.ADD_MUL_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_8'):
            self.value, self.error = self.math_modules.ADD_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_9'):
            self.value, self.error = self.math_modules.ADD_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '2_10'):
            self.value, self.error = self.math_modules.ADD_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_m_d'):
            self.value, self.error = self.math_modules.SOUS_MUL_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_m_p'):
            self.value, self.error = self.math_modules.SOUS_MUL_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_m_o'):
            self.value, self.error = self.math_modules.SOUS_MUL_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_d_p'):
            self.value, self.error = self.math_modules.SOUS_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_d_o'):
            self.value, self.error = self.math_modules.SOUS_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 's_p_o'):
            self.value, self.error = self.math_modules.SOUS_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_d_p'):
            self.value, self.error = self.math_modules.MUL_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_d_o'):
            self.value, self.error = self.math_modules.MUL_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'm_p_o'):
            self.value, self.error = self.math_modules.MUL_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, 'd_p_o'):
            self.value, self.error = self.math_modules.DIV_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_1'):
            self.value, self.error = self.math_modules.ADD_SOUS_MUL_DIV()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_2'):
            self.value, self.error = self.math_modules.ADD_SOUS_MUL_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_3'):
            self.value, self.error = self.math_modules.ADD_SOUS_MUL_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_4'):
            self.value, self.error = self.math_modules.ADD_SOUS_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_5'):
            self.value, self.error = self.math_modules.ADD_SOUS_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_6'):
            self.value, self.error = self.math_modules.ADD_SOUS_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_7'):
            self.value, self.error = self.math_modules.ADD_MUL_DIV_POW()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_8'):
            self.value, self.error = self.math_modules.ADD_MUL_DIV_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_9'):
            self.value, self.error = self.math_modules.ADD_MUL_POW_MOD()
        elif MAGIC_MATH_BASE(self.master, self.data_base, None, self.line).OPERATORS(self.history_of_operators, '3_10'):
            self.value, self.error = self.math_modules.ADD_DIV_POW_MOD()

        if name == 'cython':
            self.value = [self.value]
            if self.error is None: self.error = ""
            else: pass 
        else: pass
            
        return self.value, self.error

    def OPERATORS(self, master, n: str):
        mask_sous   = ('+' not in master and '*' not in master and '/' not in master and '^' not in master and '%' not in master)  # -
        mask_mul    = ('+' not in master and '-' not in master and '/' not in master and '^' not in master and '%' not in master)  # *
        mask_div    = ('+' not in master and '-' not in master and '*' not in master and '^' not in master and '%' not in master)  # /
        mask_square = ('+' not in master and '-' not in master and '*' not in master and '/' not in master and '%' not in master)  # ^
        mask_mod    = ('+' not in master and '*' not in master and '/' not in master and '^' not in master and '-' not in master)  # %

        #########################                group A            ##########################################
        mask_sous_mul       = (('+' not in master and '/' not in master and '^' not in master and '%' not in master) and ('-' in master and '*' in master))  # -*
        mask_sous_div       = (('*' not in master and '+' not in master and '^' not in master and '%' not in master) and ('-' in master and '/' in master))  # -/
        mask_sous_square    = (('*' not in master and '/' not in master and '+' not in master and '%' not in master) and ('-' in master and '^' in master))  # -^
        mask_sous_mod       = (('*' not in master and '/' not in master and '^' not in master and '+' not in master) and ('-' in master and '%' in master))  # -%

        #########################                group B            ##########################################
        mask_mul_div        = (('+' not in master and '-' not in master and '^' not in master and '%' not in master) and ('/' in master and '*' in master))  # */
        mask_mul_square     = (('/' not in master and '+' not in master and '-' not in master and '%' not in master) and ('^' in master and '*' in master))  # *^
        mask_mul_mod        = (('-' not in master and '/' not in master and '+' not in master and '^' not in master) and ('%' in master and '*' in master))  # *%

        #########################                group D            ##########################################
        mask_div_square     = (('-' not in master and '%' not in master and '+' not in master and '*' not in master) and ('/' in master and '^' in master))  # /^
        mask_div_mod        = (('-' not in master and '^' not in master and '+' not in master and '*' not in master) and ('/' in master and '%' in master))  # /%
        #########################                group D            ##########################################
        mask_square_mod     = (('-' not in master and '/' not in master and '+' not in master and '*' not in master) and ('%' in master and '^' in master)) # ^%

        ##########################                groupe 0            ########################################

        mask_add    = ('-' not in master and '*' not in master and '/' not in master and '^' not in master and '%' not in master)  # +

        ##########################                groupe 1            ########################################

        mask_add_sous   = (('*' not in master and '/' not in master and '^' not in master and '%' not in master) and ('+' in master and '-' in master))  # +-
        mask_add_mul    = (('-' not in master and '/' not in master and '^' not in master and '%' not in master) and ('+' in master and '*' in master))  # +*
        mask_add_div    = (('*' not in master and '-' not in master and '^' not in master and '%' not in master) and ('+' in master and '/' in master))  # +/
        mask_add_square = (('*' not in master and '/' not in master and '-' not in master and '%' not in master) and ('+' in master and '^' in master))  # +^
        mask_add_mod    = (('*' not in master and '/' not in master and '^' not in master and '-' not in master) and ('+' in master and '%' in master))  # +%

        ##########################                groupe 2            ########################################

        mask_add_sous_mul       = (('/' not in master and '^' not in master and '%' not in master) and ('+' in master and '-' in master and '*' in master))  # +-*
        mask_add_sous_div       = (('^' not in master and '%' not in master and '*' not in master) and ('+' in master and '-' in master and '/' in master))  # +-/
        mask_add_sous_square    = (('*' not in master and '/' not in master and '%' not in master) and ('+' in master and '-' in master and '^' in master))  # +-^
        mask_add_sous_mod       = (('/' not in master and '^' not in master and '*' not in master) and ('+' in master and '-' in master and '%' in master))  # +-%
        mask_add_mul_div        = (('-' not in master and '^' not in master and '%' not in master) and ('+' in master and '*' in master and '/' in master))  # +*/
        mask_add_mul_square     = (('-' not in master and '/' not in master and '%' not in master) and ('+' in master and '*' in master and '^' in master))  # +*^
        mask_add_mul_mod        = (('/' not in master and '^' not in master and '-' not in master) and ('+' in master and '*' in master and '%' in master))  # +*%
        mask_add_div_square     = (('-' not in master and '*' not in master and '%' not in master) and ('+' in master and '/' in master and '^' in master))  # +/^
        mask_add_div_mod        = (('*' not in master and '^' not in master and '-' not in master) and ('+' in master and '/' in master and '%' in master))  # +/%
        mask_add_square_mod     = (('/' not in master and '-' not in master and '*' not in master) and ('+' in master and '^' in master and '%' in master))  # +^%
        mask_sous_mul_square    = (('/' not in master and '-' in master and '*' in master) and ('+' not in master and '^' in master and '%' not in master))  # -*^
        mask_sous_mul_mod       = (('/' not in master and '-' in master and '*' in master) and ('+' not in master and '^' not in master and '%' in master))  # -*%
        mask_sous_mul_div       = (('/' in master and '-' in master and '*' in master) and ('+' not in master and '^' not in master and '%' not in master))  # -*/
        mask_sous_div_square    = (('/' in master and '-' in master and '*' not in master) and ('+' not in master and '^' in master and '%' not in master))  # -/^
        mask_sous_div_mod       = (('/' in master and '-' in master and '*' not in master) and ('+' not in master and '^' not in master and '%' in master))  # -/%
        mask_sous_square_mod    = (('/' not in master and '-' in master and '*' not in master) and ('+' not in master and '^' in master and '%'  in master)) # -^%
        mask_div_square_mod     = (('/' in master and '-' not in master and '*' not in master) and ('+' not in master and '^' in master and '%' in master))  # /^%
        mask_mul_div_square     = (('/' in master and '-' not in master and '*' in master) and ('+' not in master and '^' in master and '%' not in master))  # */^
        mask_mul_div_mod        = (('/' in master and '-' not in master and '*' in master) and ('+' not in master and '^' not in master and '%' in master))  # */%
        mask_mul_square_mod     = (('/' not in master and '-' not in master and '*' in master) and ('+' not in master and '^' in master and '%' in master))  # *^%
        ##########################                groupe 3            ########################################

        mask_add_sous_mul_div       = (('^' not in master and '%' not in master) and ('+' in master and '-' in master and '*' in master and '/' in master))  # +-*/
        mask_add_sous_mul_square    = (('/' not in master and '%' not in master) and ('+' in master and '-' in master and '*' in master and '^' in master))  # +-*^
        mask_add_sous_mul_mod       = (('^' not in master and '/' not in master) and ('+' in master and '-' in master and '*' in master and '%' in master))  # +-*%
        mask_add_sous_div_square    = (('*' not in master and '%' not in master) and ('+' in master and '-' in master and '/' in master and '^' in master))  # +-/^
        mask_add_sous_div_mod       = (('*' not in master and '^' not in master) and ('+' in master and '-' in master and '/' in master and '%' in master))  # +-/%
        mask_add_sous_square_mod    = (('*' not in master and '/' not in master) and ('+' in master and '-' in master and '^' in master and '%' in master))  # +-^%
        mask_add_mul_div_square     = (('-' not in master and '%' not in master) and ('+' in master and '*' in master and '/' in master and '^' in master))  # +*/^
        mask_add_mul_div_mod        = (('-' not in master and '^' not in master) and ('+' in master and '*' in master and '/' in master and '%' in master))  # +*/%
        mask_add_mul_square_mod     = (('-' not in master and '/' not in master) and ('+' in master and '*' in master and '^' in master and '%' in master))  # +*^%
        mask_add_div_square_mod     = (('-' not in master and '*' not in master) and ('+' in master and '/' in master and '^' in master and '%' in master))  # +/^%

        ##########################                groupe 4            ########################################

        mask_add_sous_mul_div_square    = (('%' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '^' in self.master))  # +-*/^
        mask_add_sous_mul_div_mod       = (('^' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '%' in self.master))  # +-*/%
        mask_add_sous_mul_square_mod    = (('/' not in self.master) and ('+' in self.master and '-' in self.master and '*' in self.master and '^' in self.master and '%' in self.master))  # +-*^%
        mask_add_sous_div_square_mod    = (('*' not in self.master) and ('+' in self.master and '-' in self.master and '/' in self.master and '^' in self.master and '%' in self.master))  # +-/^%
        mask_add_mul_div_square_mod     = (('-' not in self.master) and ('+' in self.master and '*' in self.master and '/' in self.master and '^' in self.master and '%' in self.master))  # +*/^%


        ##########################                groupe 5            ########################################

        mask_add_sous_mul_div_square_mod = ('+' in self.master and '-' in self.master and '*' in self.master and '/' in self.master and '^' in self.master and '%' in self.master)  # +-*/^%

        #######################################################################################################

        if   n == '0_0':        return mask_add
        elif n == '1_1':        return mask_add_sous
        elif n == '1_2':        return mask_add_mul
        elif n == '1_3':        return mask_add_div
        elif n == '1_4':        return mask_add_square
        elif n == '1_5':        return mask_add_mod
        elif n == '2_1':        return mask_add_sous_mul
        elif n == '2_2':        return mask_add_sous_div
        elif n == '2_3':        return mask_add_sous_square
        elif n == '2_4':        return mask_add_sous_mod
        elif n == '2_5':        return mask_add_mul_div
        elif n == '2_6':        return mask_add_mul_square
        elif n == '2_7':        return mask_add_mul_mod
        elif n == '2_8':        return mask_add_div_square
        elif n == '2_9':        return mask_add_div_mod
        elif n == '2_10':       return mask_add_square_mod
        elif n == '3_1':        return mask_add_sous_mul_div
        elif n == '3_2':        return mask_add_sous_mul_square
        elif n == '3_3':        return mask_add_sous_mul_mod
        elif n == '3_4':        return mask_add_sous_div_square
        elif n == '3_5':        return mask_add_sous_div_mod
        elif n == '3_6':        return mask_add_sous_square_mod
        elif n == '3_7':        return mask_add_mul_div_square
        elif n == '3_8':        return mask_add_mul_div_mod
        elif n == '3_9':        return mask_add_mul_square_mod
        elif n == '3_10':       return mask_add_div_square_mod
        elif n == '4_1':        return mask_add_sous_mul_div_square
        elif n == '4_2':        return mask_add_sous_mul_div_mod
        elif n == '4_3':        return mask_add_sous_mul_square_mod
        elif n == '4_4':        return mask_add_sous_div_square_mod
        elif n == '4_5':        return mask_add_mul_div_square_mod
        elif n == '5_0':        return mask_add_sous_mul_div_square_mod
        elif n == 'm_0_0':      return mask_mul
        elif n == 's_0_0':      return mask_sous
        elif n == 'p_0_0':      return mask_square
        elif n == 'o_0_0':      return mask_mod
        elif n == 'd_0_0':      return mask_div
        elif n == 's_m':        return mask_sous_mul
        elif n == 's_d':        return mask_sous_div
        elif n == 's_p':        return mask_sous_square
        elif n == 's_o':        return mask_sous_mod
        elif n == 'm_d':        return mask_mul_div
        elif n == 'm_p':        return mask_mul_square
        elif n == 'm_o':        return mask_mul_mod
        elif n == 'p_o':        return mask_square_mod
        elif n == 'd_p':        return mask_div_square
        elif n == 'd_o':        return mask_div_mod
        elif n == 's_m_d':      return mask_sous_mul_div
        elif n == 's_m_p':      return mask_sous_mul_square
        elif n == 's_m_o':      return mask_sous_mul_mod
        elif n == 's_d_p':      return mask_sous_div_square
        elif n == 's_d_o':      return mask_sous_div_mod
        elif n == 's_p_o':      return mask_sous_square_mod
        elif n == 'm_d_p':      return mask_mul_div_square
        elif n == 'm_d_o':      return mask_mul_div_mod
        elif n == 'm_p_o':      return mask_mul_square_mod
        elif n == 'd_p_o':      return mask_div_square_mod