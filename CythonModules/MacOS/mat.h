// c module used for making maths 

#include <stdio.h> 

double SUM(int a, int b);
int RANGE( int n, int m, int step);

int prod(int a, int b ){
    int i;
    double sum = 0.0;
    
    for(i=0; i<=10; i++){
        sum += SUM(a, b);
    }

    return (sum);
}

double SUM(int a[], int len){
    double sum = 0.0 ;
    int j = 0;
    
    //int b[100];

    for (; j<=len; j++){
    sum += a[j];
    }
    
    return (sum);
}
