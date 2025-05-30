// Write a program to print the  multiplication table of of a number n

#include <stdio.h>

int main(){
    int n1,i;
    printf("Enter the number: ");
    scanf("%d",&n1);
    for (i=1;i<=10;i++)
    printf("%d X %d = %d\n",i,n1,i*n1);
    return 0;
}