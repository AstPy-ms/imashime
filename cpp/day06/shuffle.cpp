#include<iostream>
#include<string>

using namespace std;

int main(){

    string cards;
    char tmp;
    unsigned int num_of_shuffle, i, j, top;
    
    while(1){

        cin >> cards;
        
        if( cards == "-") break;

        cin >> num_of_shuffle;

        for( i = 0; i < num_of_shuffle; i++ ){
            cin >> top;
            for( j = 0; j < top; j++){
                tmp = cards[0];
                cards.erase(cards.begin());
                cards.insert(cards.end(), tmp);
            }
        }

        cout << cards << endl;

    }

    return 0;

}