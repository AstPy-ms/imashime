/*

気合でやった。
絶対にもっと賢いやり方があると思う。

*/

#include<iostream>

using namespace std;

int main(){

    int S;
    int h=0, m=0, s;

    // S[秒]を入力させる
    cin >> S;

    // Sが3600未満になるまで、Sから3600[秒]=1[時間]ずつ引き、hを1増やす。
    while(S >= 3600){
        S -= 3600;
        h++;
    }
    
    // m[分]も同様
    while(S >= 60){
        S -= 60;
        m++;
    }
    
    // 余った数字はs[秒]そのもの
    s = S;

    // 出力
    cout << h << ":" << m << ":" << s << endl;

    return 0;

}