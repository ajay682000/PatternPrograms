#include<stdio.h>
int main()
{
    int i,j,n;
    char str[20];
    scanf("%s %n",&str, &n);
    for(i=0;i<n;i++){
        for(j=0;j<i;j++){
            printf(" ");
        }
    printf("%c \n", str[i]);
    }
    return 0;
}



// For compiling write cc filename.c
// For executing ./a.out