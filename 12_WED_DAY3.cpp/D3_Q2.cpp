int findDuplicate(vector<int> &arr) 
{
    // Write your code here
    int ans=0;
    for(auto i:arr){
        ans=ans^i;
    }
    for(int i=1;i<arr.size();i++){
        ans=ans^i;
    }
    return ans;
    
	
}
