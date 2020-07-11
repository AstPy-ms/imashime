/*

配列使わずに入力できちゃった例。
多分こっち推奨

*/

#include<iostream>

int main(){

    // a:縦, b:横
    int a, b;

    // スペース区切りの入力はこれでいいらしい
    std::cin >> a;
    std:: cin >> b;

    // 出力
    std::cout << a*b << " " <<  2*a + 2*b << std::endl;

    return 0;

}