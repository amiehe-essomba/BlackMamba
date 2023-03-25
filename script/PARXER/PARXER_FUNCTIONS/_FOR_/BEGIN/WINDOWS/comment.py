from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmtError as ce
from statement.comment                                  import externalCmt, internalCmt

class COMMENT:
    def __init__(self,
            master         : str,
            data_base      : dict,
            line           : int,
            history        : list,
            store_value    : list,
            space          : int,
            save_block     : bool,
            comment_storage: list
            ) -> None:
        # main string
        self.master             = master
        # current line in the IDE
        self.line               = line
        # data base
        self.data_base          = data_base
        # history of command
        self.history            = history
        # canceling def when any command was not typed
        self.store_value        = store_value
        # counting empty line
        self.space              = space
        # save comment
        self.locked             = save_block
        # contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.comment_storage    = comment_storage

    def LINE(self,
           loop         : list,
           tabulation   : int = 1,
           ) -> tuple:
        """
        :param bool_value:
        :param tabulation:
        :param _type_:  {default value = 'conditional'}
        :return:
        """

        ################################################################################################
        self.if_line        = 0     # counting
        self.error          = None  # error
        self.string         = ''    # concatented string
        self.normal_string  = ''    # normal string
        self.end            = ''    # canceling deff
        ################################################################################################
        self.active_tab     = None  # activating indentation
        self.tabulation     = tabulation  # counting indentation
        self.max_emtyLine   = 100   # max line for empty line
        self.loop           = loop  # storing values
        self.begin_cancel   = False # canceling while loop
        ################################################################################################

        for i in range(1):
            # concatening string and extraction of string concatenated , tabulation for and indensation and error
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master, tabulation=self.tabulation)

            if self.error is None:
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                if self.active_tab is True:
                    if self.error is None:
                        if self.locked is False:
                            self.get_block, self.value, self.error = internalCmt.INTERNAL_BLOCKS( normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation + 1)

                            if self.error is None:
                                self.comment_storage.append(self.value)
                                if   self.get_block == 'empty' :
                                    if self.space <= self.max_emtyLine:
                                        self.loop.append((self.normal_string, True))
                                        self.space += 1
                                    else:
                                        self.error = ce.ERRORS(self.line).ERROR4()
                                        break
                                elif self.get_block == 'any'   :
                                    self.store_value.append(self.normal_string)
                                    self.space = 0
                                    self.loop.append((self.normal_string, True))
                                else:
                                    self.error = ce.ERRORS(self.line).ERROR4()
                                    break
                            else: break
                        else:
                            self.error = ce.ERRORS(self.line).ERROR4()
                            break
                    else:  break
                else:
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(  normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                    if self.error is None:
                        if   self.get_block == 'end:':
                            if self.store_value:
                                del self.store_value[:]
                                del self.history[:]
                                self.loop.append((self.normal_string, False))
                                self.begin_cancel = True
                                break
                            else:
                                self.error = ce.ERRORS(self.line).ERROR2()
                                break
                        elif self.get_block == 'save:':
                            if self.locked is False:
                                self.locked = True
                                self.comment_name = self.value
                                self.loop.append((self.normal_string, False))
                            else:
                                self.error = ce.ERRORS(self.line).ERROR3()
                                break
                        elif self.get_block == 'empty':
                            if self.space <= self.max_emtyLine:
                                self.loop.append((self.normal_string, False))
                                self.space += 1
                            else:
                                self.error = ce.ERRORS(self.line).ERROR4()
                                break
                        else:
                            self.error = ce.ERRORS(self.line).ERROR4()
                            break
                    else:  break
            else:
                if self.tabulation == 1:  break
                else:
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS( normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                    if self.error is None:
                        if   self.get_block == 'end:' :
                            if self.store_value:
                                del self.store_value[:]
                                del self.history[:]
                                self.loop.append((self.normal_string, False))
                                self.begin_cancel = True
                                break
                            else:
                                self.error = ce.ERRORS(self.line).ERROR2()
                                break
                        elif self.get_block == 'save:':
                            if self.locked is False:
                                self.locked = True
                                self.comment_name = self.value
                                self.loop.append((self.normal_string, False))
                            else:
                                self.error = ce.ERRORS(self.line).ERROR3()
                                break
                        elif self.get_block == 'empty':
                            if self.space <= self.max_emtyLine:
                                self.loop.append((self.normal_string, False))
                                self.space += 1
                            else:
                                self.error = ce.ERRORS(self.line).ERROR4()
                                break
                        else:
                            self.error = ce.ERRORS(self.line).ERROR4()
                            break
                    else:  break

        return self.loop, self.begin_cancel, self.locked, self.error