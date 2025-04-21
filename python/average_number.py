def find_average(numbers):
    sum = 0
    if numbers == []:
        return 0
    else:
        
        for i in numbers:
            sum+= i
            
        return sum / len(numbers)
        
    

print(find_average([5,5,5,5,5]))
