# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#Part 1 and 2
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp
  
f100_in_celsius = f_to_c(100)

#Part 3 and 4
def c_to_f(c_temp):
  temp_f = (c_temp * (9/5)) + 32
  return temp_f

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#Part 5-7
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Part 8
c = 3*10**8
def get_energy(mass, c):
  return mass*(c*c)

#Output of part 8 test
bomb_energy = bomb_mass * (c*c)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#Part 11-13
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + "meters.")
