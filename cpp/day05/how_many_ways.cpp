#include<stdio.h>

int main(){

    unsigned int n, x;
    unsigned int i, j, k;
    unsigned int counter = 0;

    while (1){

        scanf("%d%d", &n, &x);

        if( n == 0 && x == 0 ){
            break;
        }

        for( i = 1; i <= n; i++ ){
            for( j = 1; j < i; j++ ){
                for ( k = 1; k < j; k++ ){
                    if( i + j + k == x){
                        // printf("%d %d %d\n", i, j, k);
                        counter += 1;
                    }
                }
            }
        }

        printf("%d\n", counter);
        counter = 0;

    }

    return 0;
    
}