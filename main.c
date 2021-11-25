#include <stdio.h>
#include <stdlib.h>

typedef struct time {
    int h;
    int m;
    int s;
} time;

int main() {

    time *a, *b;

    a = (time*) malloc(sizeof(time));
    b = (time*) malloc(sizeof(time));

    printf("input a : ");
    scanf("%d %d %d", &a->h, &a->m, &a->s);
    
    printf("input b : ");
    scanf("%d %d %d", &b->h, &b->m, &b->s);

    a->s = a->h*60*60 + a->m*60 + a->s;
    b->s = b->h*60*60 + b->m*60 + b->s;

    int aa, bb;
    aa = a->s+b->s;
    bb = a->s-b->s;

    if(bb<0) bb += 24*3600;

    printf("%d %d %d\n", aa/3600, aa/60%60, aa%60);
    printf("%d %d %d\n", bb/3600, bb/60%60, bb%60);

    free(a);
    free(b);

    return 0;

}
