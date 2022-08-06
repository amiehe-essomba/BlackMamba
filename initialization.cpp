# include <stdio.h>
# include < math.h>
# include < stdio.h>

# define masterIter = 50

double def( int n ):
	double a = 0.0
	double b = 0.0
	int i

	for (i=0; i<=n; i++){
		a = a + b
		b = a
	}
	
	return a
