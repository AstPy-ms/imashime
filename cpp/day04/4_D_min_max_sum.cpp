#include<iostream>

using namespace std;

int main(){

    long min, max, sum=0;
    long input_num;
    unsigned int n;

    cin >> n;

    for(int i=0;i<n;i++){
        cin >> input_num;
        sum += input_num;
        if(i == 0){
            min = input_num;
            max = input_num;
        }else{
            if(min > input_num){
                min = input_num;
            }
            if(max < input_num){
                max = input_num;
            }
        }
    }

    cout << min << " " << max << " " << sum << endl;

    return 0;

}