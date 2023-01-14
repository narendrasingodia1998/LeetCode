class Solution {
public:
    int findUParent(int node,vector<int> &parent){
        if(parent[node]==node){
            return node;
        }
        return parent[node]=findUParent(parent[node],parent);
    }
    void union_node(int node1,int node2,vector<int>& parent){
        int ulp_node1=findUParent(node1,parent);
        int ulp_node2=findUParent(node2,parent);
        if(ulp_node1!=ulp_node2){
            if(ulp_node1<ulp_node2){
                //Connect node2 to ulp_node1
                parent[ulp_node2]=ulp_node1;
            }
            else{
                parent[ulp_node1]=ulp_node2;
            }
        }
    }
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        vector<int> parent(26,0);
        for(int i=0;i<26;i++){
            parent[i]=i;
        }
        for(int i=0;i<s1.length();i++){
            union_node(s1[i]-'a',s2[i]-'a',parent);
        }
        string ans="";
        for(int i=0;i<baseStr.length();i++){
            ans+=findUParent(baseStr[i]-'a',parent)+'a';
        }
        return ans;
    }
};