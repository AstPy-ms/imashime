#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

struct card {
    char mark;
    int value;
};

void bubbleSort(card A[], const int n){

    int flag = 1;
    int i, j;

    for(i=0;flag;i++){
        flag = 0;

        for(j=n-1;i<j;j--){
            if( A[j].value < A[j-1].value ){
                swap(A[j], A[j-1]);
                flag = 1;
            }
        }
    }
}

void selectionSort(card A[], const int n){

    int i, j;

    for(i=0;i<n;i++){
        int min = i;
        for(j=i;j<n;j++)
            if(A[j].value < A[min].value)
                min = j;
        if(i != min){
            swap(A[i], A[min]);
        }
    }
}

int main(){

    int n, i, j;

    scanf("%d%*c", &n);
    
    card A[n], B[n];
    
    for(i=0;i<n;i++){
        scanf("%c%d%*c", &A[i].mark, &A[i].value);
        B[i] = A[i];
    }

    bubbleSort(A, n);
    selectionSort(B, n);

    for(i=0;i<n;i++){
        if(i > 0){
            printf(" ");
        }
        printf("%c%d", A[i].mark, A[i].value);
    }

    printf("\n");
    printf("Stable\n");

    int flag = 1;
    for(i=0;i<n;i++){
        if(i > 0){
            printf(" ");
        }
        printf("%c%d", B[i].mark, B[i].value);
        if( !(B[i].mark == A[i].mark && B[i].value == A[i].value) ){
            flag = 0;
        }
    }

    printf("\n");
    
    if(flag){
        printf("Stable\n");
    }else{
        printf("Not stable\n");
    }

    return 0;
}