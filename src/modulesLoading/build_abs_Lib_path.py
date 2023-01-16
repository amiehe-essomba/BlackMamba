class Lib_Path:
    def __init__(self,
            root : str,
            sys: str = 'windows'
            ) -> None:

        # root path
        self.root       = root
        # system name
        self.sys        = sys

    def getPath(self):
        self.second_part = ''
       
        # get Windows path
        if   self.sys in [ 'windows' ]  : self.second_part = "\\Library"
        # get Linux path
        elif self.sys in [ 'linux' ]    : self.second_part = '/Library'
        # get Mac Os path
        elif self.sys in [ 'macOs' ]    : self.second_part = '/Library'

        # Library absolute path
        self.path = str(self.root) + str(self.second_part)

        return self.path

    def getFile_in_Path(self, file_name : str) -> str:
        self.path = Lib_Path( root=self.root, sys=self.sys).getPath()
        # get Windows file
        if self.sys in ['windows']:  self.path = self.path + f"\\{file_name}"
        # get Linux file
        elif self.sys in ['linux']: self.path = self.path + f"/{file_name}"
        # get Mac Os file
        elif self.sys in ['macOs']:  self.path = self.path + f"/{file_name}"

        return str(self.path)
