#include <bits/stdc++.h> 
vector < int > sqsorted(vector < int > & arr) {
    // Write your code here.
    vector<int>ans;
   
    for(int i=0;i<arr.size();i++){
        int temp=pow(arr[i],2);
        ans.push_back(temp);
    }
    sort(ans.begin(),ans.end());
    
    return ans;
}