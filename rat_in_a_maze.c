
#include <stdio.h>
int isSafe(int [5][5],int
,int,int);
int main()
{
    
    int rat[5][5]={
        {1,0,1,0,1},
        {1,1,1,1,1},
        {0,1,0,1,0},
        {1,0,0,1,1},
        {1,1,1,0,1}
    };
    int sol[5][5];
    
    int ratMaze(int[5][5],int,int,int,int[5][5]);
   for(int i=0;i<5;i++)
   {
       for(int j=0;j<5;j++)
       {
        printf("%d ",rat[i][j]);
       }
       printf("\n");
   }
   for(int i=0;i<5;i++)
   {
       for(int j=0;j<5;j++)
       {
           sol[i][j]=0;
       }
   }
    printf("\nratMaze is \n");
 
    if(ratMaze(rat,0,0,5,sol)){
     for(int i=0;i<5;i++)
     {
         for(int j=0;j<5;j++)
         {
          printf("%d ",sol[i][j]);
         }
      printf("\n");
     }
 }
    return 0;
}
int isSafe(int rat[5][5],int x,int y, int n)
{
    if(x<n&&y<n&&rat[x][y]==1)
    {
        return 1;
    }
    return 0;
}
int ratMaze(int rat[5][5],int x,int y,int n,int sol[5][5])
{
    if(x==n-1&&y==n-1)
    {
        sol[x][y]=1;
        return 1;
    }
    if(isSafe(rat,x,y,n))
    {
        sol[x][y]=1;
        if(ratMaze(rat,x+1,y,n,sol))
        {
            return 1;
        }
        if(ratMaze(rat,x,y+1,n,sol))
        {
            return 1;
        }
        sol[x][y]=0;
        return 0;
        
    }
    return 0;
}
