#include<iostream>

using namespace std;

int main(){

    unsigned int n, i, j;

    cin >> n;

    for( i = 1; i <= n; i++ ){

        unsigned int x = i;

        // 3で割れる
        if( x % 3 == 0 ){
            cout << " " << i;
        }else{
            while ( x > 0 ){
                if ( x % 10 == 3){
                    cout << " " << i;
                    break;
                }
                x /= 10;
            }
        }
    }

    cout << endl;

    return 0;

}