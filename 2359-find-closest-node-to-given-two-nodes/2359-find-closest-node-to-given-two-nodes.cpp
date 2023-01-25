class Solution {
public:
    void bfs(int node,vector<int>& edges,vector<int>& distance){
        int n=edges.size();
        vector<bool> visited(n,false);
        int level=0;
        while(node!=-1&&visited[node]==false){
            distance[node]=level;
            level++;
            visited[node]=true;
            node=edges[node];
        }
    }
    void print(vector<int> arr){
        for(auto i:arr){
            cout<<i<<" ";
        }cout<<endl;
    }
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n=edges.size();
        vector<int> distance1(n,INT_MAX),distance2(n,INT_MAX);
        bfs(node1,edges,distance1);
        bfs(node2,edges,distance2);
        int ans=-1,dis=INT_MAX;
        for(int i=0;i<n;i++){
            int temp=max(distance1[i],distance2[i]);
            if(dis>temp){
                dis=temp;
                ans=i;
            }
        }
        //print(distance1);
        //print(distance2);
        return ans;
    }
};