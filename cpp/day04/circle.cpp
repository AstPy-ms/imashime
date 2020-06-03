#include<stdio.h>
#define PI 3.141592653589

int main(){

    double radius;

    scanf("%lf", &radius);
    printf("%.6lf %.6lf\n", radius*radius*PI, radius*2.0*PI);

    return 0;

}