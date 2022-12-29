class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n=tasks.size();
        //vector<vector<int>> arr;
        for(int i=0;i<n;i++){
            tasks[i].push_back(i);
        }
        sort(tasks.begin(),tasks.end());
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>> > pq;
        long long int time =0,i=0;
        vector<int> ans;
        while(!pq.empty()||i<n){
            if(pq.empty()&&i<n){
                time=tasks[i][0];
                pq.push({tasks[i][1],tasks[i][2]});
                i++;
                while(i<n&&time>=tasks[i][0]){
                    pq.push({tasks[i][1],tasks[i][2]});
                    i++;
                }
            }
            //select min time 
            auto temp=pq.top();
            //cout<<time<<" "<<temp.first<<" "<<temp.second<<endl;
            pq.pop();
            time+=temp.first;
            ans.push_back(temp.second);
            //push
            while(i<n&&time>=tasks[i][0]){
                pq.push({tasks[i][1],tasks[i][2]});
                i++;
            }
        }
        return ans;
    }
};