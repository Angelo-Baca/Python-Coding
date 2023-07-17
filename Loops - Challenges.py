'''This file contains challenges regarding loops'''

'''A function that determines which of the two lists has the larger sum'''
#Write your function here
def larger_sum(lst1, lst2):
  sum1 = sum(lst1)
  sum2 = sum(lst2)
  if sum2 > sum1:
    return lst2
  else: 
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

'''A function that determines if the sum of a list is over 9000'''
#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

'''A function that determines which of the values is the max inside a list'''
#Write your function here
def max_num(nums):
  default = nums[0]
  count = 0
  for index in nums:
    if index > default:
      default = index
    count += 1
  return default

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

'''A function that returns the same values in a list'''
#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

'''A function that reverses a list'''
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))