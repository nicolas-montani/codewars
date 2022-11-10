'''
Description :

Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

def snail(s):
    length = len(s)
    n = length - 1
    slist = []
    m = n-1
    
    print(length)
    for line in s : 
        print(s)
    
    #if it's odd 
    if len(s[0]) == 0:
        return slist
    
    elif length%2 != 0 : 
    
        #round count
        for i in range(0,n-1) :
            
            #print(f'i:{i}')
            #go tough first row
            for r in range(i,n-i) : 
                slist.append(s[i][r])
                
            #print(f'first it : from s[{i}][{i}] to s[{i}][{n-i}]')

            #go trough last column
            for c in range(i,n-i): 
                slist.append(s[c][n-i])
                
            #print(f'first it : from s[{i}][{n-i}] to s[{n-i}][{n-i}]')
            
            #go trough last row
            for r in range(n-i,i,-1):
                slist.append(s[n-i][r])          
                
            #print(f'first it : from s[{n-i}][{n-i}] to s[{n-i}][{i}]')
            
            #go trough last column
            for c in range(n-i,i,-1):
                slist.append(s[c][i])
                
            #print(f'first it : from s[{n-i}][{i}] to s[{n-i-1}][{i}]')
            
        
        #print(slist)
        
    elif length%2 == 0 : 
        
        #round count
        for i in range(0,n) :
            
            #print(f'i:{i}')
            #go tough first row
            for r in range(i,n-i) : 
                slist.append(s[i][r])
                
            #print(f'first it : from s[{i}][{i}] to s[{i}][{n-i}]')

            #go trough last column
            for c in range(i,n-i): 
                slist.append(s[c][n-i])
                
            #print(f'first it : from s[{i}][{n-i}] to s[{n-i}][{n-i}]')
            
            #go trough last row
            for r in range(n-i,i,-1):
                slist.append(s[n-i][r])          
                
            #print(f'first it : from s[{n-i}][{n-i}] to s[{n-i}][{i}]')
            
            #go trough last column
            for c in range(n-i,i,-1):
                slist.append(s[c][i])
                
            
        
    
    if length%2 != 0 or n == 0:
        
        slist.append(s[n//2][n//2])
        
    return(slist)