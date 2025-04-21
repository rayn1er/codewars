# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    
    list = []
    value = n

    for i in range(1,n+1):
        list.append(value)
        value-=1
        
    return list