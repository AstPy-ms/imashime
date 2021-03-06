#include<iostream>

using namespace std;


void printArray(int list[100], int n){

    int i;

    for(i=0;i<n;i++){
        if(i == 0){
            cout << list[i];
        }else{
            cout << " " << list[i];
        }
    }

    cout << endl;

}


void insertionSort (int A[100], int n) {

    int i, j, v;

    for (i=1;i<n;i++) {
        v = A[i];
        j = i - 1;

        while (j >= 0 && A[j] > v){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = v;
        printArray(A, n);
    }

}


int main(){

    int i, n;
    int A[100] = {0};

    cin >> n;

    for(i=0;i<n;i++){
        cin >> A[i];
    }

    printArray(A, n);

    insertionSort(A, n);

    return 0;
}