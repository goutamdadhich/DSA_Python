#include<stdio.h>
#include<limits.h>

int min(int x, int y)
{
	return x<y?x:y;
}

int FindMin_Recurssion(int *C, int n, int amt)
{
	if(amt == 0)
	return 0;
	
	if(amt < 0)
	return INT_MAX;
	
	int count, res;
	
	count = INT_MAX;
	
	for(int i=0; i<n; i++)
	{
		res = FindMin_Recurssion(C, n, amt-C[i]);
		
		if (res != INT_MAX)
		count = min(count, res+1);
	}
	
	
	
	return count;
}


int FindMin_DP(int *C, int n, int amt)
{
	int arr[amt+1];
	arr[0] = 0;
	
	for(int i = 1; i<=amt; i++)
	{
		arr[i] = INT_MAX;
		int res = INT_MAX;
		
		for(int j = 0; j<n; j++)
		{
			if (i - C[j] >= 0)
			res = arr[i - C[j]];
			
			if (res != INT_MAX)
			arr[i] = min(arr[i], res+1);
				
		}
	}
	
	return arr[amt];
}


int main()
{
    int C[] = {2,3,5,7};
    int amt = 15;
    int n;
    n = sizeof(C)/sizeof(C[0]);
    
    printf("\n------------********---------------\n");
    
    printf("Using recurssion :- \n");
    int res_r = FindMin_Recurssion(C, n, amt);
    printf("Minimum coins required :   %d", res_r);
    
    printf("\n------------********---------------\n");
    
    printf("Using dynamic programming :- \n");
    int res_dp = FindMin_DP(C, n, amt);
    printf("Minimum coins required :   %d", res_dp);
    
    printf("\n------------********---------------\n");
	    
    return 0;
}
