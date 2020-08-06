#include<stdio.h>
#include<limits.h>

int max(int x,  int y)
{
	return x>y?x:y;
}

int RodCut_Recurssion(int *len, int *price, int n)
{
	if (n==0)
	return 0;
	
	int max_pro = INT_MIN;
	
	for(int i=1; i<=n; i++)
	{
		int res = price[i-1] + RodCut_Recurssion(len, price, n-i);
		
		if (res > max_pro)
		max_pro = res;
	}
	
	return max_pro;
}

int RodCut_DP(int *len, int *price, int n)
{
	int profit[n+1];
	profit[0] = 0;
	
	for(int i=1; i<= n; i++)
	{
		//profit[i] = INT_MIN
		int res = INT_MIN;
		
		for(int j=0; j<i; j++)
		{
			res = max(res, price[j] + profit[i-j-1]);
		}
		profit[i] = res;
	}
	return profit[n];
}

int main()
{
	int len[] = {1, 2, 3, 4, 5, 6, 7};
	int price[] = {1, 5, 8, 9, 10, 17, 20};
	int n = 4;
	
	printf("\n------------********---------------\n");
    
    printf("Using recurssion :- \n");
    int res_r = RodCut_Recurssion(len, price, n);
    printf("Maxmimum Profit :   %d", res_r);
    
    printf("\n------------********---------------\n");
    
    printf("Using dynamic programming :- \n");
    int res_dp = RodCut_DP(len, price, n);
    printf("Maxmimum Profit :   %d", res_dp);
    
    printf("\n------------********---------------\n");
	    
    return 0;
	
}
