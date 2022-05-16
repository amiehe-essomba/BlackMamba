from script import control_string

class STDIN:

    def __init__(self, data_base:dict, line:int):
        self.data_base          = data_base
        self.line               = line
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def STDIN(self, color: dict, tab: int, _type_:str = '...'):

        self.string_concatenate = str( input('{}{} {}'.format(color[ '0' ], _type_, color[ '1' ])) )
        self.normal_string      = self.string_concatenate

        self.string_concatenate, self.tab_activate, self.error = self.analyse.BUILD_CON( self.string_concatenate, tab )
        self.normal_string      = self.analyse.BUILD_NON_CON( self.normal_string, tab )

        return self.string_concatenate, self.normal_string, self.tab_activate, self.error

    def NORMAL_STDIN(self, color: dict, type = '... '):
        self.string_concatenate = str( input( '{}{}{}'.format( color[ '0' ], type, color[ '1' ] ) ) )

        return self.string_concatenate