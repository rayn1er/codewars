# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    a, b, c = arr[0], arr[1], arr[2]
    
    if a == b:
        common_value = a
    else:
        common_value = a if a == c else b
    

    for num in arr:
        if num != common_value:
            return num