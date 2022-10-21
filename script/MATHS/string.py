class STRING:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base

    def STRING(self):
        self.value          = None

        try:  self.value    = str( self.master[1: -1 ])
        except ValueError: pass

        return self.value