#include<stdio.h>

int main(){

    unsigned int n, i, data;

    scanf("%d", &n);

    unsigned int reverse_list[n];

    for( i = n; i > 0; i--){
        scanf("%d", &data);
        reverse_list[i-1] = data;
    }

    for( i = 0; i < n; i++){
        printf("%d", reverse_list[i]);
        if ( i != n-1){
            printf(" ");
        }
    }

    printf("\n");

    return 0;

}