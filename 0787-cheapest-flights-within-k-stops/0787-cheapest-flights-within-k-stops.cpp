class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        //creating adjacency list
        vector<vector<pair<int,int>>> adj(n);
        for(int i=0;i<flights.size();i++){
            int u=flights[i][0];
            int v=flights[i][1];
            int cost=flights[i][2];
            adj[u].push_back({v,cost});
        }
        //                  k     cost nodee
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> pq;
        vector<int> cost(n,INT_MAX);
        //vector<int> no_stop(n,-1);
        
        pq.push({-1,{0,src}});
        cost[src]=0;
        while(!pq.empty()){
            auto it=pq.top();
            int cost_node=it.second.first;
            int node=it.second.second;
            int stop=it.first;
            pq.pop();
            if(stop<k){
                for(auto neighbour:adj[node]){
                    int v=neighbour.first;
                    int cos=neighbour.second;
                    if(cost_node+cos<cost[v]){
                        cost[v]=cost_node+cos;
                        pq.push({stop+1,{cost[v],v}});
                    }
                }
            }
        }
        if(cost[dst]==INT_MAX){
            return -1;
        }
        return cost[dst];   
    }
};