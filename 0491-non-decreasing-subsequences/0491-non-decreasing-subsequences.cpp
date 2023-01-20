class Solution {
public:
    void solve(vector<int> nums,int index,vector<int> &arr,set<vector<int>> &ans){
        if(index==nums.size()){
            if(arr.size()>=2){
                ans.insert(arr);
            }
            return ;
        }
        //Not Take
        solve(nums,index+1,arr,ans);
        //Take
        bool take=true;
        if(arr.size()>0 && arr[arr.size()-1]>nums[index]){
            take=false;
        }
        if(take){
            arr.push_back(nums[index]);
            solve(nums,index+1,arr,ans);
            arr.pop_back();
        }
    }
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> temp;
        vector<int> arr;
        solve(nums,0,arr,temp);
        vector<vector<int>> ans;
        for(auto i:temp){
            ans.push_back(i);
        }
        return ans;
    }
};