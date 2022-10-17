#include <iostream>
#include <vector>

using namespace std;

bool birdFly(vector<int>& nums) 
{ 
    int i, minjump = 0; 
    for(i = nums.size()-2; i >= 0; i--)
    { 
        minjump++; 
        if(nums[i] >= minjump) 			 
            minjump = 0; 
        
    } 
    if(minjump == 0) 		 
        return true; 
    else 		 
        return false; 
    
}

int main()
{
    int n;
    cin>>n;
    vector<int>v;
    
    for(int i = 0; i<n; i++)
    {
        int a;
        cin>>a;
        v.push_back(a);
    }
    
    cout<<birdFly(v);
    

    return 0;
}