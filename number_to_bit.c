#include <stdio.h>

int main()
{
    int n,n1,rem,res=0,i=0;
    int a[100];
    
    scanf("%d",&n);
    n1=n;
    while(n)
    {
        rem=n%2;
        n/=2;
        a[i]=rem+res*10;
        i++;
    }
    
    for(int j=i-1;j>=0;j--)
    {
        printf("%d",a[j]);
        
    }
 
    
    return 0;
}
