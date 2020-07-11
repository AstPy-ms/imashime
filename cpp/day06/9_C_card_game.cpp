#include<iostream>
#include<string>

#define MAX_LENGTH 100

using namespace std;

int main(){

    unsigned int n, i, score[2] = {0};
    string taro, hanako;

    cin >> n;

    for( i = 0; i < n; i++ ){
        
        cin >> taro >> hanako;
        
        unsigned int flag = 0;

        if(taro == hanako){
            score[0]++;
            score[1]++;
        }else{

            unsigned int j = 0;

            while( taro[j] != '\0' || hanako[j] != '\0'){
                if( taro[j] > hanako[j] ){
                    score[0] += 3;
                    flag = 1;
                    break;
                }else if( taro[j] < hanako[j] ){
                    score[1] += 3;
                    flag = 1;
                    break;
                }
                j++;
            }

            if(flag == 0){
                if( taro.length() > hanako.length() ){
                    score[0] += 3;
                }
                else{
                    score[1] += 3;
                }
            }
        }

    }

    cout << score[0] << " " << score[1] << endl;

    return 0;

}