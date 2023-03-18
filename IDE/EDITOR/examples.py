from script.STDIN.LinuxSTDIN        import bm_configure as bm

class details:
    def __init__(self, idd ):
        self.max_       = len(' unless "r" in ["r", "a", "e"]:         ')
        self.test       = []
        self.idd        = idd
        self.ww         = bm.init.bold+bm.fg.white
        self.b          = bm.init.bold
        
    def aa(self):
        if   self.idd == 0:
            self.test_id    = [
                len(' my_list = [] '),
                len(' my_list.add( "Apple" ) '), 
                len(' [].add( my_list ) '),2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' my_list = []', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' my_list.add( "Apple" )', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' [].add( my_list )', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[5])+' +'
                ]
        elif self.idd == 1:
            self.test_id    = [
                len(' name = func() -> any: '),
                len(' #For returning any ouputs '), 
                len(' #that you want. '),2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' name = func() -> any:', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' #For returning any ouputs', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' #that you want.', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[5])+' +'
                ]
        elif self.idd == 2:
            self.test_id    = [
                len(' #Particulally use for loading '),
                len(' #a module as an alias. '), 
                len(' load module matrix as md '),2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + self.b+bm.words(' #Particulally use for loading', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + self.b+bm.words(' #a module as an alias.', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + self.b+bm.words(' load module matrix as md', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + self.b+bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[5])+' +'
                ]
            
        return [self.test, self.max_]
    
    def bb(self):
        self.c = self.b+bm.fg.rbg(153, 153, 255)
        if   self.idd == 0:
            self.test_id    = [
                len(' #For creating multi-line '),
                len(' #comment use <begin> function '), 
                len(' begin:  '), len('   Hi there! '), len('   I am Black Mamba '), 
                len('   and you who are you? '), len(' end: '), 2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' #For creating multi-line', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' #comment use <begin> function', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[7])+' +',
                "     +" + bm.words(' begin: ', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words('   Hi there!', self.c).final()+' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.words('   I am Black Mamba', self.c).final()+' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.words('   and you who are you?', self.c).final()+' '*(self.max_-self.test_id[5])+' +',
                "     +" + bm.words(' end:', self.ww).final()+' '*(self.max_-self.test_id[6])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[7])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[8])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[9])+' +'
                ]
        elif self.idd == 1:
            self.test_id    = [
                len(' bool(1), bool(1.0) '),
                len(' name = bool("1.0") '), 
                len(' name = func(a : bool=True): '),2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' bool(1), bool(1.0)', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' name = bool("1.0")', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' name = func(a : bool=True):', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[5])+' +'
                ]
        elif self.idd == 2:
            self.test_id    = [
                len(' #Returning boolean Type. '),
                len(' iris = func()->boolean: '), 
                len(' def iris( a : bool)->boolean: '),2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + self.b+bm.words(' #Returning boolean Type.', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + self.b+bm.words(' iris = func()->boolean:', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + self.b+bm.words(' def iris( a : bool)->boolean:', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + self.b+bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[5])+' +'
                ]      
        elif self.idd == 3:
            self.test_id    = [
            len(' #Breaking loop while and for '),
            len(' for i in [0:10]: '), 
            len('   if i > 5: '), len('     break '), len('   end: '), len(' end: '), 2,
            len(' Learn more on my github page.  '),
            len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + self.b+bm.words(' #Breaking loop while and for', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + self.b+bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[6])+' +',
                "     +" + self.b+bm.words(' for i in [0:10]:', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + self.b+bm.words('   if i > 5:', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + self.b+bm.words('     break', self.ww).final()+' '*(self.max_-self.test_id[3])+' +',
                "     +" + self.b+bm.words('   end:', self.ww).final()+' '*(self.max_-self.test_id[4])+' +',
                "     +" + self.b+bm.words(' end:', self.ww).final()+' '*(self.max_-self.test_id[5])+' +',
                "     +" + self.b+bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[6])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[7])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[8])+' +'
                ]
        else: pass 

        return [self.test, self.max_]
    
    def u(self):
        
        if self.key == 'unless':
            self.test_id    = [
                len(' unless ? 1 == ? 1.0: '),
                self.max_, len(' if True == False:     '),
                len(' unless None: '), len(' if 1 != 2:     '),2,
                len(' unless "r" in ["r", "a", "e"]: '),
                len('   print * True '),
                len(' end: '), 2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' unless ? 1 == ? 1.0:', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' unless "r" in ["r", "a", "e"]:        ', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' unless True == False:', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words(' unless None:', self.ww).final()+' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.words(' unless 1 != 2:', self.ww).final()+' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[5])+' +',
                "     +" + bm.words(' unless "r" in ["r", "a", "e"]:', self.ww).final()+ ' '*(self.max_-self.test_id[6])+' +',
                "     +" + bm.words('   print * True', self.ww).final()+ ' '*(self.max_-self.test_id[7])+' +',
                "     +" + bm.words(' end:', self.ww).final()+ ' '*(self.max_-self.test_id[8])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[9])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[10])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[11])+' +'
                ]
        elif self.key == 'if':
            self.max_       = len(' if "r" in ["r", "a", "e"]:         ')
            self.test_id    = [
                len(' if ? 1 == ? 1.0: '),
                self.max_, len(' if True == False:     '),
                len(' if None: '), len(' if 1 != 2:     '),2,
                len(' if True % 2 == 0: '),
                len('   print * True '),
                len(' else: '),
                len('   print * False '),
                len(' end: '), 2,
                len(' Learn more on my github page.  '),
                len(' https://github.com/amiehe-essomba ')
                ]
            self.test       = [
                "     +" + bm.words(' if ? 1 == ? 1.0:', self.ww).final()+' '*(self.max_-self.test_id[0])+' +',
                "     +" + bm.words(' if "r" in ["r", "a", "e"]:        ', self.ww).final()+' '*(self.max_-self.test_id[1])+' +',
                "     +" + bm.words(' if True == False:', self.ww).final()+' '*(self.max_-self.test_id[2])+' +',
                "     +" + bm.words(' if None:', self.ww).final()+' '*(self.max_-self.test_id[3])+' +',
                "     +" + bm.words(' if 1 != 2:', self.ww).final()+' '*(self.max_-self.test_id[4])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[5])+' +',
                "     +" + bm.words(' if True % 2 == 0:', self.ww).final()+ ' '*(self.max_-self.test_id[6])+' +',
                "     +" + bm.words('   print * True', self.ww).final()+ ' '*(self.max_-self.test_id[7])+' +',
                "     +" + bm.words(' else:', self.ww).final()+ ' '*(self.max_-self.test_id[8])+' +',
                "     +" + bm.words('   print * True', self.ww).final()+ ' '*(self.max_-self.test_id[9])+' +',
                "     +" + bm.words(' end:', self.ww).final()+ ' '*(self.max_-self.test_id[10])+' +',
                "     +" + bm.words(' ', self.ww).final()+ ' '*(self.max_-self.test_id[11])+' +',
                "     +" + bm.init.underline+bm.words(' Learn more on my github page. ', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[12])+' +',
                "     +" + bm.init.underline+bm.words(' https://github.com/amiehe-essomba', self.ww).final(locked=True)+ ' '*(self.max_-self.test_id[13])+' +'
                ]

        return self.test, self.max_