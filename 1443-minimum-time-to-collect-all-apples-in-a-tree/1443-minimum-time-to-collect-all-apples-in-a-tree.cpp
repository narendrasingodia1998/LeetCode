class Solution {
public:
    bool dfs(vector<vector<int>> &adj,vector<int> &visited,vector<bool> &hasApple,int node,int &ans){
        visited[node]=true;
        bool go=false;
        for(auto neighbour:adj[node]){
            if(visited[neighbour]==false){
                bool temp=dfs(adj,visited,hasApple,neighbour,ans);
                //cout<<node<<" "<<neighbour<<" "<<temp<<endl;
                if(temp){
                    ans+=2;
                }
                go=go|temp;
            }
        }
        if(hasApple[node]){
            return true;
        }
        return go;
    }
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> adj(n);
        for(auto i:edges){
            adj[i[0]].push_back(i[1]);
            adj[i[1]].push_back(i[0]);
        }
        // for(int i=0;i<adj.size();i++){
        //     cout<<i<<" : ";
        //     for(auto j:adj[i]){
        //         cout<<j<<" ";
        //     }cout<<endl;
        // }
        vector<int> visited(n,false);
        int ans=0;
        dfs(adj,visited,hasApple,0,ans);
        return ans;
    }
};