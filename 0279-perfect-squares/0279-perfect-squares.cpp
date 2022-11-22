class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1,0);
        //dp[i] means least number of prefect square number that sum to n
        //Base Case
        dp[0]=0;
        for(int j=1;j<=n;j++){
            int temp=INT_MAX;
            for(int i=1;i*i<=j;i++){
                temp=min(temp,1+dp[j-i*i]);
            }
            dp[j]=temp;
        }
        return dp[n];
    }
};