#include<iostream>

using namespace std;

int main(){

    int S;
    int h=0, m=0, s;

    cin >> S;

    while(S >= 3600){
        S -= 3600;
        h++;
    }
    
    while(S >= 60){
        S -= 60;
        m++;
    }
    
    s = S;

    cout << h << ":" << m << ":" << s << endl;

    return 0;

}