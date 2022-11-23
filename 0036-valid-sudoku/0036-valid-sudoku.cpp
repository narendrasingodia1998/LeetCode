class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //cheacking for row
        for(int i=0;i<9;i++){
            unordered_map<char,int> count;
            for(int j=0;j<9;j++){
                char ch=board[i][j];
                if(ch!='.'){
                    if(count[ch]!=0){
                        return false;
                    }
                    count[ch]=1;
                }
            }
        }
        //for column
        for(int i=0;i<9;i++){
            unordered_map<char,int> count;
            for(int j=0;j<9;j++){
                char ch=board[j][i];
                if(ch!='.'){
                    if(count[ch]!=0){
                        return false;
                    }
                    count[ch]=1;
                }
            }
        }
        //checking 
        for(int l=0;l<3;l++){
            for(int k=0;k<3;k++){
                unordered_map<char,int> count;
                for(int i=0+3*l;i<3+3*l;i++){
                    for(int j=0+k*3;j<3+3*k;j++){
                        char ch=board[i][j];
                        if(ch!='.'){
                            if(count[ch]!=0){
                                return false;
                            }
                            count[ch]=1;
                        }
                    }
                }
            }    
        }
        return true;
        
    }
};