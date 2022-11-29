#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int m=n*n;
    int count=0;
    
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(i%n==0){
                count=i;
            }
            if(j<=i && j>=count)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
            
            
        }
        printf("\n");
    }
    

    return 0;
}
