#include<iostream>

using namespace std;

int main(){

    int former, latter;

    while(1){

        cin >> former >> latter;

        if(former == 0 && latter == 0){
            break;
        }else{
            if(former > latter){
                former = former + latter;
                latter = former - latter;
                former = former - latter;
            }
            cout << former << " " << latter << endl;
        }
    }

    return 0;

}