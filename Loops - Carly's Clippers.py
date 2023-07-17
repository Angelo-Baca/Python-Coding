#base list of haircuts do not edit
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#corresponding prices to each cut, do not edit
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# The number of requested cuts for that style
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#how to get the total amount of profit earned last week 
total_price = 0
for price in prices:
  total_price = total_price + price   
print("The total price for haircuts last week was: ", total_price, "\n")

#how to get average cost of haircut
average_price = total_price / len(prices)
  
print("Average Haircut Price: \n",average_price, "\n")

#price adjustment list
new_prices =[price - 5 for price in prices]
print("These are our new prices:")
print(new_prices)

#revenue analysis
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("The total revenue generated last week was: ", total_revenue)

average_daily_revenue = total_revenue / 7
print("Daily average revenue is: ", average_daily_revenue)

#list compression to cuts only under $30
#Angelo Loop 
"""cuts_under_30 = [
  hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]: """

#Developer Loop 
cuts_under = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("\n")
print("Cuts under $30", cuts_under)
