#include<stdio.h>

#define MAX_CHAR 1000

int main(){

    char num_as_char[MAX_CHAR + 1];
    unsigned int i = 0, sum = 0;

    while(1){

        scanf("%s", num_as_char);
        if(num_as_char[0] == '0') break;

        while (num_as_char[i] != '\0'){
            sum += num_as_char[i] - '0';
            i++;
        }

        printf("%d\n", sum);
        sum = 0;
        i = 0;
    
    }

    return 0;

}