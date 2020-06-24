#include<cstdio>
#include<cmath>

#define MAX_STUDENTS 1000

int main(){

    while(1){

        unsigned int n, i, score, scores_data[MAX_STUDENTS] = {0}, sum = 0;
        double alpha = 0, average;

        scanf("%d", &n);

        if(n == 0) break;

        for( i = 0; i < n; i++ ){
            scanf("%d", &score);
            sum += score;
            scores_data[i] = score;
        }

        average = (double)sum / n;

        for( i = 0; i < n; i++ ){
            alpha += pow(scores_data[i] - average, 2);
        }

        alpha /= n;
        
        printf("%.8lf\n", sqrt(alpha));

    }

    return 0;

}