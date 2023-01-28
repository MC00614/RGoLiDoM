#include <stdio.h>
int main(){
    int s;
    int S=0;
    for(int i=1;i<=5;i++){
        scanf("%d",&s);
        getchar();
        S=S+s;
    }
    printf("%d",S);
    
    return 0;
}