#include<cstdio>
#include<cmath>
#include <bits/stdc++.h>

int main(){

    unsigned int a, b, angle;
    double S, L, h;

    scanf("%d%d%d", &a, &b, &angle);

    S = a * b * sin( M_PI * angle/180 ) / 2;
    L = a + b + sqrt( pow(a, 2) + pow(b, 2) - 2 * a * b * cos( M_PI * angle/180 ) );
    h = 2 * S / a;

    printf("%lf\n%lf\n%lf\n", S, L, h);

    return 0;

}