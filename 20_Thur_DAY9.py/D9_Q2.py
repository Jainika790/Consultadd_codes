#To fing leader in an array considering last element as leader 
#and other element who is equal or greater than the rightmost elements
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        arr=[]
        ans=0
        #Code here
        for i in range(N-1,-1,-1):
            
            if A[i]>=ans:
                arr.append(A[i])
                ans=A[i]
        ans=len(arr)-1
        return arr[::-1]
    print(leaders(0,[16,17,4,3,5,2],6))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends