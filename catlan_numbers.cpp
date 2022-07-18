#include <iostream>

using namespace std;

int main()
{
    int n,i;
    int cat(int);
    cin>>n;
    for(i=0;i<n;i++)
    {
        cout<<cat(i)<<" ";
    }

    return 0;
}
int cat(int n){
    int i,res=0;
    if(n==0||n==1)
    {
        return 1;
    }
    
    for(i=0;i<n;i++)
    {
        res+=cat(i)*cat(n-1-i);
    }
    return res;
}
