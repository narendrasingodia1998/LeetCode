class Solution {
public:
    int minDeletions(string s) {
        unordered_map<char,int> m;
        for(int i=0;i<s.length();i++){
            m[s[i]]++;
        }
        vector<int> arr;
        for(auto i:m){
            arr.push_back(i.second);
        }
        sort(arr.begin(),arr.end());
        //set<int> s;
        int ans=0,last=INT_MAX;
        for(int i=arr.size()-1;i>=0;i--){
            if(arr[i]>=last){
                ans+=arr[i]-last+1;
                arr[i]=last-1;
                last--;
                if(last==0){
                    last=1;
                }
            }
            else{
                last=arr[i];
            }
        }
        return ans;
    }
};