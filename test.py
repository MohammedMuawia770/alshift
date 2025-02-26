number_list = ['aba', 'xyz', 'aba', '1221']

def count_string(list):
    count = 0
    for word in list:
        if len(word) > 1 and word[0] == word[-1]:

            count+=1

    return count

        

result = count_string(number_list)
print(result)