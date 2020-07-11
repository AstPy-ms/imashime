#include<iostream>
#include<string>
#include<cctype>

using namespace std;

int main(){

    unsigned int i, counter = 0;
    string serching_word, word_in_sentence;

    cin >> serching_word;

    while(1){

        cin >> word_in_sentence;

        if (word_in_sentence == "END_OF_TEXT") break;

        for( i = 0; i < word_in_sentence.length(); i++){
            if( 'A' <= word_in_sentence[i] && word_in_sentence[i] <= 'Z' ){
                word_in_sentence[i] += 32;
            }
        }

        if( word_in_sentence == serching_word ){
            counter++;
        }

    }

    cout << counter << endl;

    return 0;

}