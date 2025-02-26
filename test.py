number_list = [10,2,30,40,-1,670,670,80,90,10]

def largest_number(numbers):
    x = numbers[0]
   
    for i in numbers:
        if x > i:
            x = i
        

    return x
        

result = largest_number(number_list)
print(result)