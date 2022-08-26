import termios, sys, fcntl, tty, os
import re 
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from script.LEXER.FUNCTION          import main
from script                         import control_string
from script.PARXER                  import parxer_assembly
from script.DATA_BASE               import data_base as db

#New Linux IDE

def readchar():
    fd              = sys.stdin.fileno()
    old_settings    = termios.tcgetattr( fd )

    try:
        tty.setraw( sys.stdin )
        ch = ord( sys.stdin.read( 1 ) )
        
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings )
        
    if ch == '0x03':
        raise KeyboardInterrupt

    return ch 

def syntax_highlight( name : str ):
    stripped = name.rstrip()
    return stripped + bm.bg.blue_L + " " * ( len( name ) - len( stripped ) ) + bm.init.reset 

def ansi_remove_chars( name : str ):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    return ansi_escape.sub ('', name)

def show( name : str ):
    try:
        float_name = float( name )
        print_name = '\n{}[ {}result{} ] : {}{}{}\n'.format( bm.fg.magenta_M, bm.fg.red_L, bm.fg.magenta_M, bm.fg.green_L, float_name, bm.init.reset)
        print( print_name)

    except:
        print_name = '\n\n{}[ {}result{} ] : {}{}\n'.format( bm.fg.magenta_M, bm.fg.red_L, bm.fg.magenta_M, bm.init.reset, name)
        print( print_name)

class STRING:   
    def __init__(self, DataBase : dict, line : int) :
        self.DataBase       = DataBase
        self.line           = line 
        self.analyze        = control_string.STRING_ANALYSE( self.DataBase, self.line )
    def STRING( self, string : str, tabulation : int = 0):
        self.string_concatenate, self.tab_active, self.error = self.analyze.BUILD_CON( string, tabulation)
        self.normal_string  = self.analyze.BUILD_NON_CON( string, tabulation )


        return self.string_concatenate, self.normal_string, self.tab_active, self.error

class terminal:
    def __init__( self, DataBase: dict, line: int):
        self.DataBase       = DataBase
        self.line           = line 

    def black_mamba( self ):
        os.system( 'clear' )
        bm.head().head()

        while True :
            self.input              = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) # ''
            self.previous_next_line = []
            self.delete_chars       = []
            self.cursor_position    = 0
            self.line_increment     = 0
            self.tabular_index      = 0
            self.length             = len( self.input )
            self.sub_length         = len( '{}{}'.format(bm.fg.yellow_L, bm.init.reset) )
            self.index              = self.length
            self.size               = len('>>> ')
            self.error              = None 

            while True:
                
                self.char           = readchar()
                
                if self.char == 1: # clean line
                    bm.clear.clear
                    self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                    self.index = self.length

                elif self.char == 3: #keyboard
                    self._keyboard_ = bm.bg.green_L+bm.fg.red_L+"KeyboardInterrupt"+bm.init.reset
                    print( self._keyboard_ )
                
                elif self.char == 4: # ending of line (ctrl+A)
                    self.index = len( self.input )
                    self.input = self.input

                elif self.char == 9: # tabular
                    self.tabular    = '    '
                    self.input   = self.input[ : self.index ] + self.tabular + self.input[ self.index : ] 
                    self.index += 4
                
                elif self.char == 26: # EOF
                    self._end_of_file_ = bm.bg.red_L+bm.fg.white_L+"EOFError"+bm.init.reset
                    print( self._end_of_file_ )
                    return

                elif 32 <= self.char <= 126: 
                    
                    self.input   = self.input[ : self.index ] + chr( self.char ) + self.input[ self.index : ] 
                    self.index  += 1
                
                elif self.char in {10, 13}: # enter
                    self.clear_input = self.input[ self.length : ]
                    print('')
                    #self.con_str, self.normal_str, self.active_tab, self.error = STRING( self.DataBase, self.line ).STRING( self.clear_input )
                   
                    if self.error is None :
                        if self.clear_input:
                            self.lexer, self.normal_string, self.error = main.MAIN( self.clear_input, self.DataBase, self.line ).MAIN()
                            
                            if self.error is None:
                                if self.lexer is not None:
                                    self.num, self.key, self.error = parxer_assembly.ASSEMBLY( self.lexer, self.DataBase,
                                                                    self.line).GLOBAL_ASSEMBLY( self.normal_string )
                                    
                                    self.previous_next_line.append( self.input ) 
                                    
                                    if self.error is None:
                                        #show( self.clear_input ) 
                                        #self.previous_next_line.append( self.input )   
                                        self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                                        self.index           = self.length
                                    else:
                                        print( '{}\n'.format(self.error) )
                                        self.error = None 
                                        self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                                        self.index           = self.length
                                else:
                                    self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                                    self.index           = self.length
                            else:
                                print( '{}\n'.format(self.error) )
                                self.error = None 
                                self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                                self.index           = self.length
                        else:
                            self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                            self.index           = self.length
                    else:
                        print( '{}\n'.format(self.error) )
                        self.error = None 
                        self.input           = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                        self.index           = self.length
                    
                elif self.char == 12: # clear screen
                    os.system('clear')
                    self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset) 
                    self.index = self.length

                elif self.char == 17: # starting of line (ctrl+Q)
                    self.index = self.length
                    self.input = self.input

                
                elif self.char == 27:
                    self.next1, self.next2 = ord( sys.stdin.read( 1 )), ord( sys.stdin.read( 1 ))

                    if self.next1 == 91:
                        if self.next2 == 68:
                            if self.index >= (self.sub_length + self.size + 1):
                                self.index  = max(0, self.index - 1)
                            else:
                                self.index = self.index 
                        
                        elif self.next2 == 67:
                            self.index = min( len( self.input ) , self.index + 1 )
                        
                        elif self.next2 == 65: #up
                            if self.previous_next_line:
                                try:
                                    self.line_increment -= 1
                                    self.input = self.previous_next_line[ self.line_increment ]
                                except IndexError:
                                    self.input = self.input
                            else:
                                self.input = self.input
                            
                            self.index = len( self.input )

                        elif self.next2 == 66:  #down
                            if self.previous_next_line:
                                try:
                                    self.line_increment += 1
                                    self.input = self.previous_next_line[ self.line_increment ]
                                except IndexError:
                                    self.input = self.input
                                
                            else:
                                self.input = self.input
                            self.index = len( self.input )
                        else:
                            pass
                
                elif self.char == 127:
                    if self.index >= (self.sub_length + self.size + 1):
                        self.input = self.input[ : self.index -1 ] + self.input[ self.index : ]
                        self.index -= 1
                    else:
                        self.input = self.input 
                        self.index = self.index 

                sys.stdout.write( bm.move_cursor.LEFT( pos = 1000 ) )
                sys.stdout.write( bm.clear.clearline )
                sys.stdout.write( syntax_highlight( self.input ) ) 
                sys.stdout.write( bm.move_cursor.LEFT( 1000 ) )

                if self.index > 0:
                    sys.stdout.write( bm.move_cursor.RIGHT( self.index - self.sub_length ) )
                else:
                    pass 

                sys.stdout.flush()
            
if __name__ == '__main__':
    data_base = db.DATA_BASE().STORAGE()
    terminal(data_base,  1).black_mamba()
