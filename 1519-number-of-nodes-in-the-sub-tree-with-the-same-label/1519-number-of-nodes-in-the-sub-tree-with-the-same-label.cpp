class Solution {
public:
    void dfs(vector<vector<int>> &adj,vector<bool> &visited,vector<int> &ans,string &labels,int node,vector<int> &count){
        visited[node]=true;
        for(auto neighbour:adj[node]){
            if(!visited[neighbour]){
                vector<int> temp(26,0);
                dfs(adj,visited,ans,labels,neighbour,temp);
                for(int i=0;i<26;i++){
                    count[i]+=temp[i];
                }
            }
        }
        count[labels[node]-'a']++;
        ans[node]=count[labels[node]-'a'];
    }
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<vector<int>> adj(n);
        for(int i=0;i<edges.size();i++){
            int u=edges[i][0];
            int v=edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<bool> visited(n,false);
        vector<int> ans(n);
        vector<int> count(26,0);
        dfs(adj,visited,ans,labels,0,count);
        return ans;
    }
};