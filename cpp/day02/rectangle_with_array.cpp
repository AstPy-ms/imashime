#include<iostream>
#include<string>

using namespace std;

int main(){
    
    string data[3];
    int i;

    for(i=0;i<2;i++){
        cin >> data[i];
    }

    int a = stoi(data[0]);
    int b = stoi(data[1]);

    cout << a*b << " " << a*2 + b*2 << endl;

    return 0;
    
}