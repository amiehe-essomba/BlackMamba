from CythonModules.Windows.LEXER.if_else        import structure 

cdef:
    unsigned long idd = 0
    str string , err
    list val 
    
if __name__ == '__main__':
    while True:
        idd += 1
        string = input(">>> :")
        if string:
            val, err = structure.IF_ELSE(string, string, {}, idd).STRUCTURE(1)
            print(val, err)
        else: pass 