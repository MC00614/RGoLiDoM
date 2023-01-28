#include <stdio.h>
int main() 
{
    int N,a,b;
    int A=0, B=0;
    scanf("%d",&N);
    
    for (int i=1;i<=N;i++) 
    {
        scanf("%d %d", &a, &b);
        getchar();
        if (a>b)
            A+=1;
        else if(a!=b)
            B+=1;
    }
    printf("%d %d",A,B);


    return 0;
}