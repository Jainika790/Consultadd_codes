#include <iostream>
using namespace std;
int main()
{
cout<<"Q1"<<endl;
    string s="aaaaabbbbcccd";
    string str="";
    int n= s.length();
    for(int i =0;i<n-1;i++){
        if(s[i]!=s[i+1])
             str+=s[i];
             
           
    }
    str.push_back(s[n-1]);  
    cout<<str<<"\n";
    return 0;
}
