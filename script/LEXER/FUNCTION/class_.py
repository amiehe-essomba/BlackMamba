from colorama import Fore
from script import control_string
from script.LEXER import particular_str_selection

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class CLASS:
    def __init__(self, master: list, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.accepted_chars = self.control.LOWER_CASE()+self.control.LOWER_CASE()+['_']
        self.selection      = particular_str_selection

    def CLASS_INIT(self, main_string: str):

        self.master         = self.master[ 0 ]
        self.master, _e_    = self.control.DELETE_SPACE( self.master )
        self.error          = None
        self.left           = 0
        self.right          = 0
        self.key            = None
        self.string         = ''
        self.class_name     = None
        self.args           = None
        self.class_inherite = None
        self.count          = 0
        self.class_info     = {

            'arguments'             : None,
            'class_name'            : None,
            'functions'             : [],
            'sub_classes'           : [],
            'function_names'        : [],
            'class_inheritance'     : None,
            'init_function'         : None

        }

        for i, str_ in enumerate( self.master ):
            self.left, self.right = self.left + str_.count( '(' ), self.right + str_.count( ')' )
            if self.left != self.right:
                if self.left < 2:
                    if self.class_name != None:
                        if self.count == 0:
                            self.key == True

                        else:
                            self.error  = ERRORS( self.line ).ERROR0( main_string )
                            break

                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break

                else:
                    self.error = ERRORS( self.line ).ERROR0( main_string )
                    break

            elif self.left == self.right and str_ == ')':
                self.key   = False
                self.count += 1

            elif self.left == self.right and str_ != ')':
                self.key = None

            if self.key == True:
                self.string += str_

            elif self.key == False:
                self.string  += str_
                self.inside                 = self.string[ 1 : -1 ]
                self.inside, self.error     = self.control.DELETE_SPACE( self.inside )

                if self.error is None:
                    self.all_class_inheritances, self.error = self.selection.SELECTION(self.inside, self.inside,
                                                            self.data_base, self.line).CHAR_SELECTION( ',' )

                    if self.error is None:
                        self.store  = []
                        for _class_ in self.all_class_inheritances:
                            self.name, self.error   = self.control.CHECK_NAME( _class_ )

                            if self.error is None:
                                if self.name == 'object':
                                    if self.store :
                                        self.error = ERRORS( self.line ).ERROR0( self.string )
                                        break
                                    else:
                                        self.store.append( self.name )
                                else:
                                    if self.store:
                                        if self.store[ -1 ] != 'object':
                                            self.store.append( self.name )
                                        else:
                                            self.error = ERRORS(self.line).ERROR0(self.string)
                                            break
                                    else:
                                        self.store.append(self.name)

                            else:
                                self.error = ERRORS(self.line).ERROR1( _class_ )
                                break

                        if self.error is None:

                            self.args                               = self.string
                            self.class_inherite                     = self.store
                            self.class_info['arguments']            = self.args
                            self.class_info['class_inheritance']    = self.class_inherite

                        else:
                            self.error = self.error
                            break

                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break

                else:
                    self.class_inherite                     = 'object'
                    self.args                               = self.string
                    self.class_info['arguments']            = self.args
                    self.class_info['class_inheritance']    = self.class_inherite
                    self.error                              = None

                self.string             = ''
                self.left               = 0
                self.right              = 0

            else:
                if self.args == None:
                    self.string += str_
                    if i == len( self.master ) - 1:
                        self.string, self.error = self.control.DELETE_SPACE( self.string )
                        self.name, self.error   = self.control.CHECK_NAME( self.string )

                        if self.error is None:
                            self.class_name                 = self.name
                            self.class_info['class_name']   = self.class_name

                        else:
                            self.error = ERRORS( self.line ).ERROR1( self.string )
                            break

                    else:
                        try:
                            if self.master[ i + 1] == '(':
                                self.string, self.error = self.control.DELETE_SPACE( self.string )
                                self.name, self.error   = self.control.CHECK_NAME( self.string )

                                if self.error is None:
                                    self.class_name                 = self.name
                                    self.class_info['class_name']   = self.class_name
                                    self.string                     = ''

                                else:
                                    self.error = ERRORS( self.line ).ERROR1( self.string )
                                    break

                            else:
                                pass

                        except IndexError:
                            pass

                else:
                    self.error = ERRORS( self.line ).ERROR0( main_string )
                    break

        if self.error is None:
            if self.class_info['class_name'] in ['function', 'func']:
                self.error = ERRORS( self.line ).ERROR1( self.class_info['class_name'] )
            else:
                pass

        else:
            self.error = self.error

        return self.class_info, self.error

class ERRORS:
    def __init__(self, line: int):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        self._str_ = '{}type {}help( {}class_name{} ) {} for more informations. '.format(we, te, ke, te, we)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : {}class name {}ERROR '.format(ne, 'NameError', ke, ae) + error

        return self.error
