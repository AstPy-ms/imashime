#include<iostream>

#define MAX_ROW 100
#define MAX_COLUMN 100

using namespace std;

int main(){

    unsigned int r, c;
    unsigned int i, j;
    unsigned int sum = 0;   // 一番右下用
    unsigned int sheet[MAX_ROW + 1][MAX_COLUMN + 1] = {0};

    cin >> r >> c;

    for( i = 0; i < r; i++ ){
        for( j = 0; j < c; j++ ){
            cin >> sheet[i][j];
        }
    }

    for( i = 0; i < r; i++){
        for( j = 0; j < c; j++){
            sheet[i][c] += sheet[i][j];
            sheet[r][j] += sheet[i][j];
            sum += sheet[i][j];
        }
    }

    sheet[i][j] = sum;

	for( i = 0;i < r+1;i++){
		for( j = 0; j < c+1; j++){
			if(j == c){
				cout << sheet[i][j];
			}else{
                cout << sheet[i][j] << " ";
            }
		}
		cout << endl;
	}    

    return 0;

}