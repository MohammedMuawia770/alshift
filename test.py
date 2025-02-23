number_list = [10,20,30,40,50,60,70,80,90,100]
# get list's size
x = len(number_list)
i = 0
# iterate list till i is smaller than x
while i < x:
    # check if number is greater than 50
    if number_list[i] > 50:
        # delete current index from list
        del number_list[i]
        # reduce the list size
        x = x -1
    else:
        # move to next item
        i+=1

print(number_list)
