class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> no_trust(n+1,0),to_other(n+1,0);
        //no_trust[i] means number people that trusts ith people
        //to_other[i] means number of people that ith person trust
        for(int i=0;i<trust.size();i++){
            to_other[trust[i][0]]++;
            no_trust[trust[i][1]]++;
        }
        for(int i=1;i<=n;i++){
            if(no_trust[i]==n-1&&to_other[i]==0){
                return i;
            }
        }
        return -1;
    }
};