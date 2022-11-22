class Solution {
public:
    int words(string temp){
        int i=0,n=temp.length(),count=0;
        for(int i=0;i<n;i++){
            if(temp[i]==' '){
                count++;
            }
        }
        return count+1;
    }
    int mostWordsFound(vector<string>& sentences) {
        int ans=0;
        for(int i=0;i<sentences.size();i++){
            ans=max(ans,words(sentences[i]));
        }
        return ans;
    }
};