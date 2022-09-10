
    def __init__(self,
                master      : any,
                data_base   : dict, 
                line        : int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyse                = control_string.STRING_ANALYSE(data_base=self.data_base, line=self.line)

    def COMMENT(self, tabulation : int = 1, c : str = ''):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = [ ]

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'comment' ]
        self.max                    = 100
        self.locked                 = False
        self.comment_storage        = []
        self.comment_name           = None

        ############################################################################

        self.color          = bm.fg.rbg(255,0,255)
        self.input          = '{}cmt:{}'.format(self.color, bm.init.reset)
        self.length         = len(self.input)
        self.index          = self.length
        self.sub_length     = len('{}{}'.format( self.color, bm.init.reset))
        self.tab            = 1
        self.Input          = ''
        self.Index          = 0
        self.col            = []
        self.if_line        = self.line
        
        ############################################################################
        self.c                      = bm.fg.rbg(153, 153, 255)
        self.previous_c             = c
        self.mainString             = ''
        self.mainIndex              = 0
        self.loop                   = []
        ############################################################################
        
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True :
            
            try:
                self.char = bm.read().readchar()
                
                if self.char  not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1

                elif self.char in {10, 13}:  # enter
                    self.if_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                    self.clear_input = self.mainString

                    if self.clear_input:
                        ####################################################################
                        _, self._, self.err = self.analyse.BUILD_CON(string=self.clear_input,tabulation=self.tabulation)
                        if self.err is None:
                            if (self._ -1 )>= 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.c).final(locked=True)
                            else:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()
                        else: self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()

                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))

                        ######################################################################
                        
                        self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.clear_input, tabulation=self.tabulation)
                        
                        if self.error is None:
                            self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                            if self.active_tab is True :
                                if self.error is None:
                                    if self.locked is False:
                                        self.get_block, self.value, self.error = internalCmt.INTERNAL_BLOCKS(  normal_string=self.normal_string,
                                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation + 1)
                                    
                                        if self.error  is None:
                                            self.comment_storage.append( self.value )

                                            if   self.get_block == 'empty'  :
                                                if self.space <= self.max: 
                                                    self.loop.append((self.normal_string, True)) 
                                                    self.space += 1
                                                else:
                                                    self.error = ce.ERRORS( self.line ).ERROR4()
                                                    break
                                            elif self.get_block == 'any'    :
                                                self.store_value.append( self.normal_string )
                                                self.space = 0
                                                self.loop.append((self.normal_string, True))
                                            else:
                                                self.error = ce.ERRORS( self.line ).ERROR4()
                                                break
                                        else:  break
                                    else:
                                        self.error = ce.ERRORS( self.line ).ERROR4()
                                        break
                                else: break
                            else:
                                self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                                if self.error is None:
                                    if   self.get_block == 'end:'     :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append((self.normal_string, False))
                                            break
                                        else:
                                            self.error = ce.ERRORS( self.line ).ERROR2( )
                                            break
                                    elif self.get_block == 'save:'    :
                                        if self.locked is False:
                                            self.locked = True
                                            self.comment_name = self.value
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = ce.ERRORS( self.line ).ERROR3()
                                            break
                                    elif self.get_block == 'empty'    :
                                        if self.space <= self.max: 
                                            self.loop.append((self.normal_string, False))
                                            self.space += 1
                                        else:
                                            self.error = ce.ERRORS( self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = ce.ERRORS( self.line ).ERROR4()
                                        break
                                else:  break
                        else:
                            if self.tabulation == 1:  break
                            else:
                                self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                                self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                                                    data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                                if self.error is None:
                                    if   self.get_block == 'end:'    :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append((self.normal_string, False))
                                            break
                                        else:
                                            self.error = ce.ERRORS( self.line ).ERROR2( )
                                            break
                                    elif self.get_block == 'save:'   :
                                        if self.locked is False :
                                            self.locked = True
                                            self.comment_name = self.value
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = ce.ERRORS( self.line ).ERROR3()
                                            break
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.max: 
                                            self.loop.append((self.normal_string, False))
                                            self.space += 1
                                        else:
                                            self.error = ce.ERRORS(  self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = ce.ERRORS( self.line ).ERROR4()
                                        break
                                else:  break
                    else:
                        if self.space <= self.max:
                            self.space += 1
                            self.loop.append((self.normal_string, False))
                        else:
                            self.error = ce.ERRORS(self.if_line).ERROR4()
                            break
                    
                    self.input      = '{}cmt:{}'.format(self.color, bm.init.reset)
                    self.index      = self.length
                    self.mainString = ''
                    self.mainIndex  = 0
                
                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 1
                    
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()
                    
            except IndexError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.error = ce.ERRORS(self.if_line).ERROR4()
                break

            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                self.error = ce.ERRORS(self.if_line).ERROR4()
                break

        #############################################################################

        return self.loop, self.error