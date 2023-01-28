#include <stdio.h>
int main()
{
    int t;
    int T = 0;
    for (int i=1;i<=4;i++)
    {
        scanf("%d", &t);
        getchar();
        T = T+t;
    }
    printf("%d\n", T/60);
    printf("%d", T-60*(T/60));
    return 0;
}