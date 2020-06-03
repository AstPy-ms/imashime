#include<iostream>

using namespace std;

int main(){

    int h, w;
    int i, j;

    while(1){

        cin >> h >> w;

        if(h == 0 && w == 0){
            break;
        }else{
            for(i=1;i<=h;i++){
                for(j=1;j<=w;j++){
                    if(i == 1 || i == h || j == 1 || j == w){
                        cout << "#";
                    }else{
                        cout << ".";
                    }
                }
                cout << endl;
            }
            cout << endl;
        }
    }

    return 0;

}