number_list = [10,20,30,40,500,60,70,80,90,10]

def larger(number):
    max = number[0]
    
    for i in number:
        if i > max:
            max = i

    return max


print(larger(number_list))

