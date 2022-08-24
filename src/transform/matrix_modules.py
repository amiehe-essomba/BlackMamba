from src.transform import error as er

class MATRIX:
    def __init__(self, master : list, nrow : int , ncol : int, reverse: bool, line: int):
        self.master     = master
        self.nrow       = nrow
        self.ncol       = ncol
        self.reverse    = reverse
        self.line       = line

    def MATRIX(self, axis: any, ctype: str='sum'):
        self.step       = 0
        self.newList    = []
        self.prev       = []
        self.error      = None
        self.type       = [type(int()), type(float()), type(bool())]

        if self.master:
            if self.nrow > 0:
                if self.ncol > 0:
                    if self.nrow * self.ncol == len( self.master):
                        if self.reverse is False:
                            self.step = self.ncol
                            self.prev.append( 0 )
                            if axis is None:
                                for i in range(self.nrow):
                                    self.prev.append( self.ncol * (i+1) )
                                    self.ms = self.master[self.prev[i]: self.prev[i + 1]]
                                    self.newList.append(self.ms)
                            else:
                                for i in range(self.nrow):
                                    try:
                                        self.prev.append( self.ncol * (i+1) )
                                        self.ms = self.master[ self.prev[ i ]: self.prev[ i+1 ]][axis]
                                        self.newList.append( self.ms )
                                    except IndexError:
                                        self.error = er.ERRORS( self.line ).ERROR33(ss='ncol')
                                        break
                        else:
                            if axis is None:
                                for i in range(self.nrow):
                                    self.ss     = []
                                    self.w      = 0
                                    for j in range( self.ncol ):
                                        self.w = self.nrow * j + i
                                        self.ss.append(self.master[ self.w ])
                                    self.newList.append( self.ss )
                            else:
                                for i in range(self.nrow):
                                    self.ss     = []
                                    self.w      = 0
                                    for j in range( self.ncol ):
                                        self.w = self.nrow * j + i
                                        self.ss.append(self.master[ self.w ])

                                    try: self.newList.append( self.ss[axis] )
                                    except IndexError :
                                        self.error = er.ERRORS(self.line).ERROR33(ss='ncol')
                                        break
                    else:
                        if self.nrow * self.ncol > len( self.master) : self.error = er.ERRORS( self.line ).ERROR31('>')
                        else : self.error = er.ERRORS( self.line ).ERROR31('<')
                elif self.ncol == -1:
                    if len( self.master ) == self.nrow:
                        if self.reverse is False:
                            if axis is None: self.newList.append( self.master )
                            else:
                                try:  self.newList.append( self.master[axis] )
                                except IndexError: self.error = er.ERRORS( self.line ).ERROR33(ss='length( master )')
                        else: self.error = er.ERRORS( self.line ).ERROR32( 'ncol')
                    else:
                        if self.nrow > len( self.master) : self.error = er.ERRORS( self.line ).ERROR31('>')
                        else : self.error = er.ERRORS( self.line ).ERROR31('<')
                else: self.error = er.ERRORS( self.line ).ERROR29( string = 'ncol')
            elif self.nrow == -1:
                if self.ncol > 0:
                    if self.ncol == len( self.master):
                        if self.reverse is False:
                            if axis is None:
                                for s in self.master:
                                    self.newList.append([s])
                            else:
                                try:  self.newList.append([self.master[axis]])
                                except IndexError: self.error = er.ERRORS( self.line ).ERROR33(ss='length( master )')
                        else: self.error = er.ERRORS( self.line ).ERROR32( 'nrow')
                    else:
                        if self.ncol > len( self.master) : self.error = er.ERRORS( self.line ).ERROR31('>')
                        else : self.error = er.ERRORS( self.line ).ERROR31('<')
                else: self.error = er.ERRORS( self.line ).ERROR29( string = 'nrow')
            else: self.error = er.ERRORS( self.line ).ERROR30( string = 'nrow')
        else: self.error = er.ERRORS( self.line ).ERROR28()

        return  self.newList, self.error