#include<iostream>

using namespace std;

int main(){

    /*
    cards[行][列]
    cards[0][j] -> スペードのj+1
    cards[1][j] -> ハートのj+1
    cards[2][j] -> クラブのj+1
    cards[3][j] -> ダイヤのj+1
    */

    char mark;
    unsigned int number, n, i, j;
    unsigned int cards[4][13] = {0};

    cin >> n;

    for( i = 0; i < n; i++ ){

        cin >> mark >> number;

        if ( mark == 'S'){
            cards[0][number-1] = 1;
        }else if ( mark == 'H'){
            cards[1][number-1] = 1;
        }else if( mark == 'C'){
            cards[2][number-1] = 1;
        }else{
            cards[3][number-1] = 1;
        }

    }

    /*
    for(i=0;i<4;i++){
        for(j=0;j<13;j++){
            cout << cards[i][j] << " ";
        }
        cout << endl;
    }

    0 1 1 1 1 1 1 1 1 1 1 1 1 
    1 1 0 1 1 1 0 1 1 1 1 1 1 
    1 1 1 1 1 1 1 1 1 1 1 0 1 
    1 1 1 1 1 1 1 0 1 1 1 1 1

    */

    for( i = 0; i < 4; i++ ){
        for( j = 0; j < 13; j++ ){
            if( cards[i][j] == 0){
                switch(i){
                    case 0:
                        cout << 'S' << " " << j+1 << endl;
                        break;
                    case 1:
                        cout << 'H' << " " << j+1 << endl;
                        break;
                    case 2:
                        cout << 'C' << " " << j+1 << endl;
                        break;
                    case 3:
                        cout << 'D' << " " << j+1 << endl;
                        break;
                }
            }
        }
    }

    return 0;

}