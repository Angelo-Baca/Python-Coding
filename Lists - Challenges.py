'''This file contains challenges and code regarding list and list commands'''

'''A function that prints a list in a range of numbers and only prints every 3rd number'''
#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))
    

#Uncomment the line below when your function is done
print(every_three_nums(91))

'''A function that removes the middle element in a list'''
#Write your function here
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

''' A function that returns the most frequent item in a list'''
#Write your function here
def more_frequent_item(my_list, item1, item2):
  x = my_list.count(item1)
  y = my_list.count(item2)
  if x > y:
    return item1
  elif x < y:
    return item2
  else:
    return item1

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


'''A function that doubles the index values'''
#Write your function here
def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

'''A function that alters the middle element in the list'''
#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))