class Solution {
public:
    int climbStairs(int n) {
        // vector<int> step(n+1,0);
        // if(n==1){
        //     return 1;
        // }
        // step[1]=1;
        // step[2]=2;
        // for(int i=3;i<=n;i++){
        //     step[i]=step[i-1]+step[i-2];
        // }
        // return step[n];
        
        //Space optimizations
        if(n==1){
            return 1;
        }
        int second_last=1,last=2,curr=last;
        for(int i=3;i<=n;i++){
            curr=last+second_last;
            second_last=last;
            last=curr;
        }
        return last;
    }
};