#include<iostream>

using namespace std;

int main(){

    // テストの点数は、中間試験の点数 m、期末試験の点数 f、再試験の点数 r で構成されています。 

    int m, f, r;
    unsigned int total;

    while(1){

        cin >> m >> f >> r;

        if( m == -1 && f == -1 && r == -1){
            break;
        }

        total = m + f;

        if( m == -1 || f == -1){
            cout << 'F' << endl;
        }else if(total < 30){
            cout << 'F' << endl;
        }else if(total < 50){
            if( r < 50){
                cout << 'D' << endl;
            }else{
                cout << 'C' << endl;
            }
        }else if(total < 65){
            cout << 'C' << endl;
        }else if(total < 80){
            cout << 'B' << endl;
        }else{
            cout << 'A' << endl;
        }

    }

    return 0;
    
}