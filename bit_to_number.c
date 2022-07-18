/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
   long long int n,i=0,res=0,rem;
    scanf("%lld",&n);
    int square(int);
    while(n)
    {
        rem=n%10;
        res+=rem*square(i);
        n/=10;
        i++;
    }
    printf("%lld",res);
    

    return 0;
}
int square(int n)
{
    int res=1;
    if(n==0)
    {
        return 1;
    }
    else
    {
       for(int i=0;i<n;i++){
         res*=2;  
       }
    }
    return res;
}

