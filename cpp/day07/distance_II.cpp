#include<cstdio>
#include<cmath>

using namespace std;

double distance(double x[100], double y[100], unsigned int n, double p){

    if(p == INFINITY){

        double abs_list[100] = {0}, max = 0;
        unsigned int i;

        max = abs(x[0] - y[0]);

        for(i=1;i<n;i++){
            if(max < abs(x[i] - y[i])){
                max = abs(x[i] - y[i]);
            }
        }

        return max;

    }else{

        unsigned int i;
        double sum = 0;

        for(i=0;i<n;i++){
            sum += pow( abs(x[i] - y[i]), p);
        }

        return pow(sum, 1/p);
    
    }
}

int main(){

    unsigned int n, p;
    double vec_x[100] = {0}, vec_y[100] = {0};
    unsigned int i, j;
    double d;

    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%lf", &vec_x[i]);
    }
    for(i=0;i<n;i++){
        scanf("%lf", &vec_y[i]);
    }

    printf("%.6lf\n", distance(vec_x, vec_y, n, 1));
    printf("%.6lf\n", distance(vec_x, vec_y, n, 2));
    printf("%.6lf\n", distance(vec_x, vec_y, n, 3));
    printf("%.6lf\n", distance(vec_x, vec_y, n, INFINITY));

    return 0;

}