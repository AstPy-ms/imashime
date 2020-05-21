/*

C++でスペース区切りの入力に対する処理がわからなかったので、配列に代入して処理してみた例。
多分非推奨。

*/

#include<iostream>
#include<string>

using namespace std;

int main(){
    
    // 入力に対して配列で受け取りたいので、string(文字列型)の配列を用意。
    string data[2];
    // for文用の変数
    int i;

    // スペース区切りなのでfor文を回して入力させる
    for(i=0;i<2;i++){
        cin >> data[i];
    }

    // int(s整数型)に直した値をa, bに代入する
    // stoi -> string to int -> stringをintに変換する関数
    int a = stoi(data[0]);
    int b = stoi(data[1]);

    // 出力
    cout << a*b << " " << a*2 + b*2 << endl;

    return 0;
    
}