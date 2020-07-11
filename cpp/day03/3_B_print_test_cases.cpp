#include<iostream>

using namespace std;

int main(){

    int input, i=1;

    while(1){

        cin >> input;
        
        if(input == 0){
            break;
        }else{
            cout << "Case " << i << ": " << input << endl;
        }

        i++;

    }

    return 0;

}