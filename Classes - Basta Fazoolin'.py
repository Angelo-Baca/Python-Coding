#Step 19
class Business:
#Step 20
  def __init__(self, name, Franchise):
    self.name = name
    self.Franchise = Franchise




#Step 12
class Franchise:
#Step 13
  def __init__(self, address, menus):
    self.menus = menus
    self.address = address
#Step 15
  def __repr__(self):
    return self.address

#Step 16
  def available_menus(self, time):
    available_menu = []
    for menu in self.menu:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menu

#Step 1 
class Menu():

#Step 2
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#Step 7
  def __repr__(self):
    return self.name + " menu is available from " + str(self.start_time) +" to " + str(self.end_time)

#Step 8 and 9
  def calculate_bill(self, purchased_items):
    purchased_items = []
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#Step 3    
brunch_items =  {
      'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

#Step 4
earlybird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
earlybird_menu = Menu("Early Bird", earlybird_items, 1500, 1800)

#Step 5 
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

#Step 6
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 2100)

print(brunch_menu)
#Error for calculate bill, does not return proper value
'''print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))
print(earlybird_menu.calculate_bill(['vegan mushroom ravioli', 'salumeria plate']))
'''
menus = [kids_menu, brunch_menu, earlybird_menu, dinner_menu]

#Step 14
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)
#Error message - needs debug - print(flagship_store.available_menus(1200))

#Step 21
basta = Business('Basta Fazoolin with my Heart', [flagship_store, new_installment])

#Step 22
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('Take a Arepa', arepas_items, 1000, 2000)
#Step 23
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])
#Step 24
arepa = Business("Take a' Arepa", [arepas_place])
#Step 25 code does not work "Business object has no attribute Franchise"
print(arepa.Franschise[0])
