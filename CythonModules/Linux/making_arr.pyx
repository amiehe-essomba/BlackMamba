from colorama 			    			import Fore, Style
from CythonModules.Linux 				import fileError as fe 
from script.STDIN.LinuxSTDIN 	        import bm_configure as bm

cdef DIFF( str string1, str string2 ):
	cdef :
		str _str_
		str result
		str rest
		

	if not string1: result = string2 
	else:
		if not string2: result = string1
		else:
			result 	= ''
			rest 	= ''
			for _str_ in string1:
				if _str_ not in string2: result += _str_ 
				else: pass 
			
			result +='|' 
			
			for _str_ in string2:
				if _str_ not in string1: rest += _str_
				else: pass

			result +=  rest

	return result 



cdef class Arithmetic:
	cdef public list  listOfValue
	cdef public int   line
	cdef: 
		int 	i
		str 	error 	
		list   	type1 
		list 	type2
		list 	final
	
	def __init__(self, listOfValue, line = 0 ) : 
		self.listOfValue		= listOfValue
		self.line			= line

	
	cpdef AddListFloat( self , float  Index, str ob_type = 'list')						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	+= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error 


	cpdef AddListInt ( self, int Index , str ob_type = 'list')							:

		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	+= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error 

	cpdef AddListCPLX( self, complex Index , str ob_type = 'list')						:

		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	+= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error 
	
	cpdef AddListBool( self, bint Index , str ob_type = 'list')							:

		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	+= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef AddListString( self, str Index, bint inv = False, str ob_type = 'list' )		:

		error = ''
		
		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ]   += Index
					else:
						self.listOfValue[ i ]   = Index + self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error
		
	cpdef AddListList( self, list Index, bint inv = False, str ob_type = 'list' ) 		: 
	
		error   = ''

		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					try:
						if inv is False:
							self.listOfValue[ i ]   += Index[ i ]
						else:
							self.listOfValue[ i ]   = Index[ i ] + self.listOfValue[ i ] 
					except TypeError:
						error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
						break
					else: pass
			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else : return tuple( self.listOfValue[ : ] ), error
		else: return None, error
	
	cpdef SousListFloat( self , float Index, bint inv = False, str ob_type = 'list')	:
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	-= Index
					else:
						self.listOfValue[ i ] 	= Index - self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef SousListCPLX( self ,complex Index, bint inv = False, str ob_type = 'list')	:

		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	-= Index
					else:
						self.listOfValue[ i ] 	= Index - self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef SousListBool( self, bint Index, bint inv = False, str ob_type = 'list')		:

		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	-= Index
					else:
						self.listOfValue[ i ] 	= Index - self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef SousListInt( self , int Index, bint inv = False, str ob_type = 'list')		:
		
		error	= ''
		
		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	-= Index
					else:
						self.listOfValue[ i ] 	= Index - self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef SousListString( self , str Index, bint inv = False, str ob_type = 'list')		:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ) :
				if type( self.listOfValue[ i ] ) == type( str() ) :
					if inv is False:
						self.listOfValue[ i ] 	= DIFF( self.listOfValue[ i ] , Index )
					else:
						self.listOfValue[ i ] 	= DIFF( Index , self.listOfValue[ i ] )
				else:	
					error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
					break
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef SousListList( self , list Index, bint inv = False, str ob_type = 'list')		:
		
		error	= ''
		type1 	= [ type( bool() ), type( float() ), type( int() ), type( complex() )]
		type2 	= [ type( str() ) ]
		final 	= []

		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					if type(self.listOfValue[ i ]) in type1  and type(Index[ i ]) in type1 :
						if inv is False:
							final.append( (self.listOfValue[ i ] - Index[ i ]) )
						else:
							final.append( (self.listOfValue[ i ] - Index[ i ]) )
					elif type(self.listOfValue[ i ]) in type2  and type(Index[ i ]) in type2 :
						if inv is False:
							final.append( DIFF( self.listOfValue[ i ] , Index[ i ] ) )
						else:
							final.append( DIFF( Index[ i ], self.listOfValue[ i ] ) )
					else:
						error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
						break

			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return final, error
			else: return tuple( final ), error
		else: return None, error
	
	cpdef MulListFloat( self , float  Index, str ob_type = 'list')						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	*= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef MulListInt( self , int  Index, str ob_type = 'list')							:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	*= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef MulListBool( self , bint Index, str ob_type = 'list')							:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	*= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef MulListCPLX( self , complex Index, str ob_type = 'list')						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	*= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error  = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef MulListString( self , str Index, str ob_type = 'list' )						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
				
					self.listOfValue[ i ] 	*= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef MulListList( self , list Index, bint inv = False, str ob_type = 'list')		:
		
		error	= ''
	
		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					try:
						self.listOfValue[ i ] *= Index[ i ]
					except TypeError:
						error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
						break

			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )

		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error
	
	cpdef DivListFloat( self , float Index, str ob_type = 'list')						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	/= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR5( )
					break

				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef DivListInt( self , int Index, str ob_type = 'list')							:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	/= Index
					self.listOfValue[ i ]	= int( self.listOfValue[ i ] )
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR5( )
					break

				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef DivListBool( self , bint Index, str ob_type = 'list')							:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	/= Index
					self.listOfValue[ i ] = int( self.listOfValue[ i ] )
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR5( )
					break

				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef DivListCPLX( self , complex Index, str ob_type = 'list')						:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					self.listOfValue[ i ] 	/= Index
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR5( )
					break

				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef DivListLits( self , list Index, str ob_type = 'list')							:
		
		error	= ''

		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					try:
						self.listOfValue[ i ] 	/= Index[ i ]
					except TypeError:
						error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
						break
					except ZeroDivisionError:
						error = ERRORS( self.line ).ERROR5( )
						break
					else: pass
			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )
		
		if not error: 
			error = None 
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error

	cpdef SquareListFloat( self , float  Index, str ob_type = 'list', bint inv = False)	:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	**= Index
					else:
						self.listOfValue[ i ] = Index ** self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef SquareListInt( self , int  Index, str ob_type = 'list', bint inv = False)		:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	**= Index
					else:
						self.listOfValue[ i ] = Index ** self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef SquareListBool( self , bint Index, str ob_type = 'list', bint inv = False)	:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	**= Index
					else:
						self.listOfValue[ i ] = Index ** self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef SquareListCPLX( self , complex Index, str ob_type = 'list', bint inv = False)	:
		
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] 	**= Index 
					else:
						self.listOfValue[ i ] = Index ** self.listOfValue[ i ]
				except TypeError:
					error = ERRORS( self.line ).ERROR1(self.listOfValue[ i ], Index )
					break
				else: pass
		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error  = None
			if ob_type == 'list' : return  self.listOfValue[ : ], error 
			else: return  tuple( self.listOfValue[ : ] ), error

		else: return  None, error
	
	cpdef SquareListList( self , list Index, bint inv = False, str ob_type = 'list')	:
		
		error	= ''
	
		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					try:
						if inv is False:
							self.listOfValue[ i ] **= Index[ i ]
						else:
							self.listOfValue[ i ] = Index[ i ] ** self.listOfValue[ i ]
					except TypeError:
						error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
						break

			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )

		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error

	cpdef ModListFloat( self , float Index, bint inv = False, str ob_type = 'list')		:
		cdef:
			list partial_type = [ type( int() ), type( float() ), type( bool() ) ]
			_type_ob1_, _type_ob2_
		error	= ''

		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] %= Index
					else:
						self.listOfValue[ i ] = Index % self.listOfValue[ i ]
				except TypeError:

					if inv is False:
						_type_ob1_ = type( self.listOfValue[ i ] )
						_type_ob2_ = type( Index )
					else:
						_type_ob2_ = type( self.listOfValue[ i ] )
						_type_ob1_ = type( Index )

					if _type_ob1_ == type( complex() ):
						if _type_ob2_ == type( complex() ):
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
						elif _type_ob2_ in partial_type:
							if inv is False:
								self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index )
							else:
								self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
					else:
						if _type_ob2_ == type( complex() ):
							if _type_ob1_ in partial_type:
								if inv is False:
									self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index  )
								else:
									self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
							else:
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
								break
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break

				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR4()
					break

		else: error = ERRORS( self.line ).ERROR3( ob_type )

		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error
	
	cpdef ModListInt( self , int Index, bint inv = False, str ob_type = 'list')			:
		cdef:
			list partial_type = [ type( int() ), type( float() ), type( bool() ) ]
			_type_ob1_, _type_ob2_
		error	= ''
	
		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] %= Index
					else:
						self.listOfValue[ i ] = Index % self.listOfValue[ i ]
				except TypeError:

					if inv is False:
						_type_ob1_ = type( self.listOfValue[ i ] )
						_type_ob2_ = type( Index )
					else:
						_type_ob2_ = type( self.listOfValue[ i ] )
						_type_ob1_ = type( Index )

					if _type_ob1_ == type( complex() ):
						if _type_ob2_ == type( complex() ):
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
						elif _type_ob2_ in partial_type:
							if inv is False:
								self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index )
							else:
								self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
					else:
						if _type_ob2_ == type( complex() ):
							if _type_ob1_ in partial_type:
								if inv is False:
									self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index  )
								else:
									self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
							else:
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
								break
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break

				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR4()
					break

		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error
	
	cpdef ModListBool( self , bint Index, bint inv = False, str ob_type = 'list')		:
		cdef:
			list partial_type = [ type( int() ), type( float() ), type( bool() ) ]
			_type_ob1_, _type_ob2_
		error	= ''
	
		if self.listOfValue:
			for i in range( len( self.listOfValue ) ):
				try:
					if inv is False:
						self.listOfValue[ i ] %= Index
					else:
						self.listOfValue[ i ] = Index % self.listOfValue[ i ]
				except TypeError:

					if inv is False:
						_type_ob1_ = type( self.listOfValue[ i ] )
						_type_ob2_ = type( Index )
					else:
						_type_ob2_ = type( self.listOfValue[ i ] )
						_type_ob1_ = type( Index )

					if _type_ob1_ == type( complex() ):
						if _type_ob2_ == type( complex() ):
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
						elif _type_ob2_ in partial_type:
							if inv is False:
								self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index )
							else:
								self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break
					else:
						if _type_ob2_ == type( complex() ):
							if _type_ob1_ in partial_type:
								if inv is False:
									self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index  )
								else:
									self.listOfValue[ i ] = CPLX( Index ).CPLX(  self.listOfValue[ i ] )
							else:
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
								break
						else:
							error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index )
							break

				except ZeroDivisionError:
					error = ERRORS( self.line ).ERROR4()
					break

		else: error = ERRORS( self.line ).ERROR3( ob_type )
		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error
	
	cpdef ModListList( self , list Index, bint inv = False, str ob_type = 'list')		:
		cdef:
			list partial_type = [ type( int() ), type( float() ), type( bool() ) ]
			_type_ob1_, _type_ob2_
		error	= ''
	
		if len( self.listOfValue ) == len( Index ):
			if self.listOfValue:
				for i in range( len( self.listOfValue ) ):
					try:
						if inv is False:
							self.listOfValue[ i ] %= Index[ i ]
						else:
							self.listOfValue[ i ] = Index[ i ] % self.listOfValue[ i ]
					except TypeError:

						if inv is False:
							_type_ob1_ = type( self.listOfValue[ i ] )
							_type_ob2_ = type( Index[ i ] )
						else:
							_type_ob2_ = type( self.listOfValue[ i ] )
							_type_ob1_ = type( Index[ i ] )

						if _type_ob1_ == type( complex() ):
							if _type_ob2_ == type( complex() ):
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
								break
							elif _type_ob2_ in partial_type:
								if inv is False:
									self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index[ i ]  )
								else:
									self.listOfValue[ i ] = CPLX( Index[ i ] ).CPLX(  self.listOfValue[ i ] )
							else:
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
								break
						else:
							if _type_ob2_ == type( complex() ):
								if _type_ob1_ in partial_type:
									if inv is False:
										self.listOfValue[ i ] = CPLX( self.listOfValue[ i ] ).CPLX( Index[ i ]  )
									else:
										self.listOfValue[ i ] = CPLX( Index[ i ] ).CPLX(  self.listOfValue[ i ] )
								else:
									error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
									break
							else:
								error = ERRORS( self.line ).ERROR1( self.listOfValue[ i ], Index[ i ] )
								break

					except ZeroDivisionError:
						error = ERRORS( self.line ).ERROR4()
						break

			else: error = ERRORS( self.line ).ERROR3( ob_type )
		else: error = ERRORS( self.line ).ERROR2( ob_type )

		
		if not error: 
			error = None
			if ob_type == 'list' : return self.listOfValue[ : ], error
			else: return tuple( self.listOfValue[ : ] ), error
		else: return None, error


cdef class CPLX		:
	cdef :
		public complex 	object1
		public str		 	_string_
		public sous, op

	def __init__( self, object1 )		:
		self.object1 		= object1
		self._string_ 		= str( self.object1 )
		self.op 			= ''
		self.sous 			= ''

	cdef complex CPLX(self, obj2 )      :
		cdef :
			float 		real 
			float 		img 
			str 		imag 
			complex	 	result 
			str 		string 

		if   '-' in self._string_ 	: self.op = '-'
		elif '+' in self._string_	: self.op = '+'
		else : self.op = None

		try:
			if '-' == self._string_[ 1 ]	: self.sous = '-'
			else : self.sous = None
		except IndexError: pass

		real   = self.object1.real % obj2
		img    = self.object1.imag % obj2

		if self.op is None:
			imag 	= str( self.img ) + 'j'
			result 	= complex( self.imag )
		else:
			string = ''
			if self.sous is None:	string = str( real ) + self.op + str( img ) + 'j'
			else:	string = self.sous + str( real ) + self.op + str( img ) + 'j'

			result = complex( string )

		return result

cdef class ERRORS	:
	cdef public int line 

	cdef:
		str 	error 	
		str  	magenta	
		str  	green
		str  	white
		str  	red	
		str  	yellow
		str  	cyan
		str  	blue
		str 	blue_l
		str 	yellow_l
		str 	white_l
		str 	green_l
		str 	cyan_l
		str		red_l
		str  	reset

	def __init__( self, line ):
		self.line 			= line 
		self.red			= bm.fg.red
		self.magenta 		= bm.fg.magenta
		self.green			= bm.fg.green
		self.white			= bm.fg.white
		self.yellow			= bm.fg.yellow
		self.cyan			= bm.fg.cyan
		self.blue			= bm.fg.blue
		self.blue_l			= bm.fg.blue_L
		self.yellow_l		= bm.fg.yellow_L
		self.white_l		= bm.fg.white_L
		self.cyan_l			= bm.fg.cyan_L 
		self.green_l		= bm.fg.green_L
		self.red_l 			= bm.fg.red_L
		self.reset			= bm.init.reset

	cdef str ERROR1( self , typ1, typ2)			:
	
		typ11 = ERRORS( self.line ).CONVERSION( typ1 )
		typ22 = ERRORS( self.line ).CONVERSION( typ2 )
		

		typ1, typ2  = ERRORS( self.line ).TYPE( typ1, typ2)

		error = '{}unsupported operand between {}<< {}{} : {} >> {} and {}<< {}{} : {} >>. {}line: {}{}'.format(self.yellow_l, self.white_l, typ11, self.white_l, typ1,
		                        self.yellow_l, self.white_l, typ22, self.white_l, typ2, self.white_l, self.yellow_l, self.line )
		error = fe.FileErrors( 'ArithmeticError' ).Errors() + error 

		return error + self.reset 
	
	cdef str ERROR2( self, str ob_type )			:
		error = '{}line : {}{}'.format(self.white_l, self.yellow_l, self.line)
		error = fe.FileErrors( 'ValueError' ).Errors() + '{}{}s {}have not the same {}size. '.format( self.magenta, 
											ob_type, self.green, self.cyan) + error

		return error + self.reset
	
	cdef str ERROR3( self , str ob_type)			:
		error = '{}line : {}{}'.format( self.white_l, self.yellow_l, self.line )
		error = fe.FileErrors( 'ValueError' ).Errors() + '{}EMPTY {}{}. '.format(self.yellow_l, self.blue_l, ob_type) + error
		
		return error + self.reset

	cdef str ERROR4( self )							:
		error = '{}modulo by zero. {}line: {}{}'.format( self.yellow_l, self.white_l, self.yellow_l, self.line)
		error = fe.FileErrors( 'ZeroDivisionError' ).Errors() + error

		return error + self.reset

	cdef str ERROR5( self )							:
		error = '{}division by zero. {}line: {}{}'.format( self.yellow_l, self.white_l, self.yellow_l, self.line)
		error = fe.FileErrors( 'ZeroDivisionError' ).Errors() + error

		return error + self.reset

	cdef str CONVERSION( self, master_init ):
		cdef str _return_
        
		if   type( master_init ) == type( int() )       :   _return_ = '{}{}integer(){}'.format(self.blue, self.red, self.blue)
		elif type( master_init ) == type( float() )     :   _return_ = '{}{}float(){}'.format(self.blue, self.green_l, self.blue)
		elif type( master_init ) == type( bool() )      :   _return_ = '{}{}boolean(){}'.format(self.blue, self.cyan, self.blue)
		elif type( master_init ) == type( complex() )   :   _return_ = '{}{}complex(){}'.format(self.blue, self.cyan_l, self.blue)
		elif type( master_init ) == type( tuple() )     :   _return_ = '{}{}tuple(){}'.format(self.blue, self.blue_l, self.blue)
		elif type( master_init ) == type( dict() )      :   _return_ = '{}{}dictionary(){}'.format( self.blue, self.magenta, self.blue)
		elif type( master_init ) == type( str() )       :   _return_ = '{}{}string(){}'.format(self.blue, self.blue, self.blue)
		elif type( master_init ) == type( range( 1 ) )  :   _return_ = '{}{}range(){}'.format(self.blue, self.green, self.blue)
		elif type( master_init ) == type( None )        :   _return_ = '{}{}none(){}'.format(self.blue, self.red_l, self.blue)
		elif type( master_init ) == type( list() )      :   _return_ = '{}{}list(){}'.format(self.blue, self.yellow_l, self.blue)

		return _return_ + self.reset 

	cdef TYPE(self, object1 , object2 ):
		cdef:
			result1 
			result2 
        
		result1 = ''
		result2 = ''

		if type( object1 ) in [ type( list() ), type( tuple()) ]:
			if len( object1 ) < 4 : result1 = object1
			else: 
				if type( object1 ) in [ type( list() ) ]: 
					result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
				else:
					result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
		elif type( object1 ) == type( str() ):
			if object1:
				if len( object1 ) < 6: pass 
				else:
					result1 = object1[ : 2] + ' ... ' + object1[ -2 : ]
			else: pass
		else: result1 = object1
        
		if type( object2 ) in [ type( list() ), type( tuple()) ]:
			if len( object2 ) < 4 : result2 = object2
			else: 
				if type( object2 ) in [ type( list() ) ]:
					result2 = f'[{object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]}]'
				else:
					result2 = f'({object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]})'
		elif type( object2 ) == type( str() ):
			if object2:
				if len( object2 ) < 6: pass 
				else:
					result2 = object2[ : 2 ] + ' ... ' + object2[ -2 : ]
			else: pass
		else: result2 = object2
				
		return result1, result2
