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
            for(i=0;i<h;i++){
                for(j=0;j<w;j++){
                    cout << "#";
                }
                cout << endl;
            }
            cout << endl;
        }
    }

    return 0;

}