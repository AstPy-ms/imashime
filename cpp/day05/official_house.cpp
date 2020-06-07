#include<iostream>

using namespace std;

// b棟 f階 の r番目 の部屋に v人 が追加で入居したことを示します

int main(){

    // i棟目のj階k号室
    unsigned int n;
    unsigned int i, j, k;
    unsigned int b, f, r;
    int v;
    unsigned int houses[4][3][10] = {0};

    cin >> n;

    for( i = 0; i < n; i++ ){
        cin >> b >> f >> r >> v;
        houses[b-1][f-1][r-1] += v;
    }

    // 表示
    for( i = 0; i < 4; i++ ){
        for( j = 0; j < 3; j++ ){
            for( k = 0; k < 10; k++ ){
                cout << " " <<houses[i][j][k];
            }
            cout << endl;
        }
        if( i != 3 ){
            for( j = 0; j < 20; j++){
                cout << "#";
            }
        }
        if( i != 3){
            cout << endl;
        }
    }

    return 0;

}