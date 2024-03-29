
from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import end
from script.STDIN.WinSTDIN                              import stdin
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmtError as ce
from script.PARXER                                      import numerical_value

ae = bm.fg.cyan_L
ve = bm.fg.rbg(0,0,0)
we = bm.fg.rbg(255,255,255)

class COMMENT_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyse                = control_string.STRING_ANALYSE(data_base=self.data_base, line=self.line)

    def COMMENT(self, tabulation : int = 0):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = [ ]
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'comment' ]
        self.color                  = ve
        self.max                    = 100
        self.locked                 = False
        self.comment_storage        = []
        self.comment_name           = None

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += 1

            try:
                if self.locked is False: pass
                else:  self.color = we

                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ae, '1': self.color }, self.tabulation, _type_='cmt:' )
                if self.error is None:
                    if self.active_tab is True:
                        if self.locked is False:
                            self.get_block, self.value, self.error = end.INTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                            if self.error  is None:
                                self.comment_storage.append( self.value )

                                if self.get_block == 'empty':
                                    if self.space <= self.max:  self.space += 1
                                    else:
                                        self.error = ce.ERRORS( self.line ).ERROR4()
                                        break
                                elif self.get_block == 'any':
                                    self.store_value.append( self.normal_string )
                                    self.space = 0
                                else:
                                    self.error = ce.ERRORS( self.line ).ERROR4()
                                    break
                            else:  break
                        else:
                            self.error = ce.ERRORS( self.line ).ERROR4()
                            break
                    else:
                        self.get_block, self.value, self.error = end.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'     :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    break
                                else:
                                    self.error = ce.ERRORS( self.line ).ERROR2( )
                                    break
                            elif self.get_block == 'save:'    :
                                if self.locked is False:
                                    self.locked = True
                                    self.comment_name = self.value

                                else:
                                    self.error = ce.ERRORS( self.line ).ERROR3()
                                    break
                            elif self.get_block == 'empty'    :
                                if self.space <= self.max: self.space += 1
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
                        self.get_block, self.value, self.error = end.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block == 'end:'      :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    break
                                else:
                                    self.error = ce.ERRORS( self.line ).ERROR2( )
                                    break
                            elif self.get_block == 'save:'   :
                                if self.locked is False :
                                    self.locked = True
                                    self.comment_name = self.value
                                else:
                                    self.error = ce.ERRORS( self.line ).ERROR3()
                                    break
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max: self.space += 1
                                else:
                                    self.error = ce.ERRORS(  self.line ).ERROR4()
                                    break
                            else:
                                self.error = ce.ERRORS( self.line ).ERROR4()
                                break
                        else:  break

            except EOFError:
                self.error = ce.ERRORS( self.line ).ERROR4()
                break

            except KeyboardInterrupt:
                self.error = ce.ERRORS( self.line ).ERROR4()
                break

        self.error = COMMENT_TRANSFORMS( self.comment_storage, self.data_base, self.error,
                                         self.comment_name ).TRANSTORMATION()

        #############################################################################

        return self.error

class COMMENT_LOOP_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
       
    def COMMENT(self, 
                tabulation  : int   = 0, 
                loop_list   : any   = None,
                keyPass     : bool  = False
                ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'comment' ]
        self.loop_list              = loop_list

        ############################################################################
        
        self.max_emtyLine           = 1000
        self.comment_storage        = []
        self.locked                 = False
        self.comment_name           = ''
        
        ############################################################################
        self.keyPass                = keyPass
        ############################################################################
        
        if self.keyPass is False:
            for j, _string_ in enumerate(self.loop_list):
                    
                self.if_line                        += 1
                self.line                           += 1
                
                self.normal_string, self.active_tab = _string_
                self.string                         = self.normal_string

                if self.active_tab is True:
                    self.get_block, self.value, self.error = end.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                    if self.error  is None:
                        if self.get_block == 'empty'      :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                            else:
                                self.error = ce.ERRORS( self.line ).ERROR4()
                                break

                        elif self.get_block == 'any'      :
                            self.store_value.append(self.normal_string)
                            self.space = 0
                            
                        if self.data_base[ 'pass' ] is None:
                            self.comment_storage.append( self.value )
                        else:pass
                    else:  break
                else:
                    self.get_block, self.value, self.error = end.EXTERNAL_BLOCKS( self.string,
                                self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                    if self.error is None:
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                break
                            else:
                                self.error = ce.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                break
                        
                        elif self.get_block == 'save:'  :
                            if self.locked is False:
                                self.locked = True
                                self.comment_name = self.value
                            else:
                                self.error = ce.ERRORS( self.line ).ERROR3()
                                break
                        
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine : self.space += 1
                            else:
                                self.error = ce.ERRORS( self.line ).ERROR4()
                                break
                    else: break
        
            self.error = COMMENT_TRANSFORMS( self.comment_storage, self.data_base, self.error,
                                         self.comment_name ).TRANSTORMATION()
        else: pass 
        
        return self.error

class COMMENT_TRANSFORMS:
    def __init__(self, 
                master      : list, 
                data_base   : dict, 
                error       : str, 
                name        : any 
                ):
        self.master         = master
        self.error          = error
        self.name           = name
        self.data_base      = data_base
        self.num_parxer     = numerical_value

    def TRANSTORMATION(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.error is None:
            self.long_chaine    = ""
            
            if self.master:
                for i, str_ in enumerate(self.master ):
                    if i < len( self.master ) - 1:
                        string = '{}\n'.format( str_ )
                        self.long_chaine += string
                    else:
                        string = "{}".format(str_)
                        self.long_chaine += string

                self.long_chaine = self.long_chaine.replace( '"', "'")
                self.long_chaine = '"'+str( self.long_chaine )+'"'
            else:  pass

            if self.name is None: pass
            else:
                self.vars       = self.data_base[ 'variables' ][ 'vars' ]
                self.values     = self.data_base[ 'variables' ][ 'values' ]
                self.func_name  = self.data_base['current_func']

                if self.name in self.vars:
                    self.idd = self.vars.index( self.name )
                    self.values[ self.idd ]     = self.long_chaine
                else:
                    self.vars.append( self.name )
                    self.values.append( self.long_chaine )

                self.data_base[ 'variables' ][ 'vars' ]     = self.vars
                self.data_base[ 'variables' ][ 'values' ]   = self.values

                if self.func_name is not None:
                    self.idd = self.self.data_base['func_names'].index( self.func_name )
                    self.self.data_base['functions'][self.idd]['function_info']['description'] = self.long_chaine
                else: pass
        else: pass

        return self.error
    
