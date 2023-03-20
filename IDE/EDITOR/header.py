import sys
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from IDE.EDITOR                     import test
from script.STDIN.LinuxSTDIN        import ascii
from time  							import sleep

def header(string : str = 'Windows Version', terminal = 'orion terminal'):
    #Linux
	w = bm.fg.rbg(255,255,255)
	bold = bm.init.bold
	blink = bm.init.blink
	re = bm.init.reset
	g = bm.fg.rbg(0, 255, 0)
	c = bm.fg.rbg(0, 255, 255)
	y = bm.fg.rbg(255, 255, 0)
	ma = bm.fg.rbg(255, 0, 255)
	r = bm.fg.rbg(255, 0, 0)
	under = bm.init.underline
	size = list(test.get_win_ter())
	size[0] = int( size[0] / 2.0)

	n = 50
	m=int(n/2.0)
	a = chr(9607) * n
	b = chr(9608)
	e = " " * (n-2)
	dot = chr(9899)
	copyright=chr(169)
	ws = 10
	push = " " * ws# * ((size[0] - int(n/2))-20)
	numeric = [chr(j) for j in range(9461, 9471)]
	shaka   = [chr(i) for i in range(9800, 9812)]

	top = f"{a}"
	mid = f"{b}{e}{b}"
	bot = b+chr(9607)*(n-2)+b
	box = [f'{shaka[3]} BLACK MAMBA {shaka[3]}', 'Version 23.03.11']

	l1 = m-int( len(box[0])/2.0 )
	l2 = m-len(string)+len(terminal)-11
	l3 = m-len('-version 23.03.11-')+len('MIT License')+3
	l4 = m-len("For more informations run:")

	sec1 = bold+w+'[ '+g+string+ w+' ]'+ r+" and "+w+'[ '+c+terminal+w+' ]'+re
	sec2 = bold+ma+'-Version 23.03.11.- '+w+chr(169)+c +' MIT License'+re
	sec3 = bold+w+f"{chr(9989)} For more informations,run:"+re
	sec4 = bold+w+f"{chr(9654)} help( " + r+"arg"+w+" )"+re
	sec5 = bold+w+f"{chr(9654)} License( )"+re
	sec6 = bold+w+f"{chr(9989)} Author:"+re
	sec7 = bold+w+f"{chr(9654)} Iréné Amiehe-Essomba"+re
	sec8 = bold+w+f"{chr(9989)} Github:"+re
	sec9 = bold+y+f"{chr(9654)} {under}https://github.com/amiehe-essomba"+re + " "+chr(9997)+re
	ww	 = ws-3
	_s_ = chr(9608)#9618 9577
	x = ascii.frame(True)
	s1, s11 = x['dl']+x['dr']+"   "+x['dl']+x['dr'], len("    ")+4
	s2, s22 = x['v']+x['v']+"   "+x['v']*2, len("    ")+4
	s3, s33, s333 = x['dl']+x['h']*2+x['m1']+x['m1']+x['h']*3+x['m1']+x['m1']+x['h']*2+x['dr'], len("    ")+1," "*ww
	s4, s44, s444 = x['v']+_s_*11+x['v'],len("    ")+1," "*ww
	s5, s55, s555 = x['dl']+x['dr']+x['v']+_s_*11+x['v']+x['dl']+x['dr'],len("   ")," "*ww
	s6, s66, s666 = x['v']*2+x['v']+_s_*11+x['v']+x['v']*2,len("   ")," "*ww
	s7, s77, s777 = x['v']*2+x['v']+_s_*9+blink+r+chr(9829)+re+_s_+x['v']+x['v']*2,len("   ")," "*ww
	s8, s88, s888 = x['ul']+x['h']+x['m1']+x['h']*2+x['m2']+x['m2']+x['h']*3+x['m2']+x['m2']+\
	x['h']*2+x['m1']+x['h']+x['ur'], len("   ")," "*ww
	s9, s99, s999 = " "*4+x['dl']+x['m1']*2+x['h']*3+x['m1']*2+x['dr'],len("   ")," "*ww
	s10, s100, s1000 = " "*4+x['v']+ " "*2+y+x['dl']+chr(9473)+x['dr']+re+" "*2+x['v'],len("    ")," "*ww
	s12, s111, s1111 = " "*4+x['v']+ " "+blink+y+chr(9679)+re+" "+y+chr(9475)+re+" "+ blink+y+chr(9679)+re+" "+x['v'],len("    ")," "*ww
	s13, s222, s2222 = " "*4+x['ul']+x['h']*3+x['m2']+x['h']*3+x['ur'],len("    ")," "*7
	s14, s333a, s3333a = " "*4+x['ul']+x['h']*3+blink+y+x['m1']+re+x['h']*3+x['ur'],len("    ")," "*ww
	s15, s555a, s5555a = " "*4+" "*4+" "+" "*4,len("    ")," "*ww
	
	print("  "+" "*14+push+top)
	print("  "+" "*14+push+mid)
	print(s5555a+s15+" "*s555a+"  "+b+bold+y+ " "*(l1-2)+bold+box[0]+re+" "*(l1-3)+b+"  "+s15)
	if terminal.split()[0] == 'orion' : print(s3333a+s14+" "*s333a+"  "+b+ " "*(l2-11) +sec1+" "*(l2-9)+b+"  "+s14)
	else:  print(s3333a+s14+" "*s333a+"  "+b+ " "*(l2-15) +sec1+" "*(l2-15)+b+"  "+s14)
	print(s2222+s13+" "*s222+ "  "+b+ " "*(l3-14)+sec2+" " * (l3-13)+b+"  "+s13)
	print(s1111+s12+" "*s111+"  "+b+" "*(l1-2)+ " "*len(box[0])+" "*(l1-1)+b+"  "+s12)
	print(s1000+s10+" "*s100+"  "+b+" "+sec3+ " "*18+b, " "+s10)
	print(s999+s9+" "*s99+"   "+b+"    "+sec4+ " "*31+b+"  "+s9)
	print(s888+s8+" "*(s88-1)+b+"    "+sec5+ " "*32+b, " "+s8)
	print(s777+s7+" "*(s77-1)+b+" "*(l1-2)+ " "*len(box[0])+" "*(l1-1)+b+ "  "+s7)
	print(s666+s6+" "*(s66-1)+b+" "+sec6+ " "*37+b+"  "+s6)
	print(s555+s5+" "*(s55-1)+b+"    "+sec7+ " "*22+b+"  "+s5)
	print("  "+s444+s4+" "*(s44-1)+b+" "*(l1-2)+ " "*len(box[0])+" "*(l1-1)+b+"    "+s4)
	print("  "+s333+s3+" "*(s33-1)+b+" "+sec8+ " "*37+b+"    "+s3)
	print("  "+push+s2+" "*(s22-1)+b+"    "+sec9+ " "*7+b, "      "+s2)
	print("  "+push+s2+" "*(s22-1)+b+" "*(l1-2)+ " "*len(box[0])+" "*(l1-1)+b+"       "+s2)
	print("  "+push+s1+" "*(s11-1)+bot+"       "+s1)
	print("\n")

	
	
	
	
	
	
	
	