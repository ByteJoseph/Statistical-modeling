// write a program to find the largest of three numbers
#include <stdio.h>

int main(){
    int n1,n2,n3,lg;
    printf("Enter three numbers\n");
    scanf("%d%d%d",&n1,&n2,&n3);
    lg = n1;
    if (n2>lg)
    lg = n2;
    if (n3>lg)
    lg = n3;
    printf("largest = %d",lg);
    return 0;
}