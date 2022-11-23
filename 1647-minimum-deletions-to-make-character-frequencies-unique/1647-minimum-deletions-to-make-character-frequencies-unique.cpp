class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26,0);
        //unordered_map<char,int> m;
        for(int i=0;i<s.length();i++){
            freq[s[i]-'a']++;
        }
        sort(freq.begin(),freq.end());
        int ans=0;
        for(int i=24;i>=0;i--){
            if(freq[i]==0){
                return ans;
            }
            if(freq[i]>=freq[i+1]){
                if(freq[i+1]==0){
                    ans+=freq[i];
                    freq[i]=0;
                }
                else{
                    ans+=freq[i]-freq[i+1]+1;
                    freq[i]=freq[i+1]-1;
                }
            }
        }
        return ans;
    }
};