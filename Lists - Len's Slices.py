# Your code below:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#cost of slice
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print("The total number of two dollars slices is: ", num_two_dollar_slices, "\n")

# number of options
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!\n")

#2D list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"], [2.5, "peppers"]]

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

three_cheapest = pizza_and_prices[:2]
print("\n")
print(three_cheapest)

