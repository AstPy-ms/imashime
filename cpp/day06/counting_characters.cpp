#include<cstdio>

int main(){

    char ch;
    unsigned int i = 0, alp_list[26] = {0};

    while( scanf("%c", &ch) != EOF ){
        if('a' <= ch && ch <= 'z'){
            alp_list[ ch - 'a' ] += 1;
        }else if('A' <= ch && ch <= 'Z'){
            alp_list[ ch + 32 - 'a'] += 1;
        }
    }

    for(i = 0; i < 26; i++){
        printf("%c : %d\n", i+'a', alp_list[i]);
    }

    return 0;

}