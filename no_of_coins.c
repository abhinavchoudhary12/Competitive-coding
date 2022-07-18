
#include <stdio.h>

int main()
{
    int coin[100]={1,2,5,10,20,50,100,500,1000};
    int ar[100];
    int j=8,k,i=0,l;
    scanf("%d",&k);
    
    while(j>=0)
    {
        if(k>=coin[j]){
            
            ar[i]=coin[j];
            k-=coin[j];
            i++;
        }
        if(coin[j]>k)
        {
        j--;
        }
    }
    for(l=0;l<i;l++)
    {
    printf("%d ",ar[l]);
    
    }
    return 0;
}

