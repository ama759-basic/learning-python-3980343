# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x = x +1

# answer = input("Stop?")
# while answer != "Y":
#   print(answer)
#   answer = input("Stop?")

# define a for loop
# days = "MTWTFSS"
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
days = "MTWTFSS"
for d in days:
  # if (d == "W"): break
  if (d == "T"): continue
  print(d)


# using the enumerate() function to get an index and an item
for i,d in enumerate(days): print(i,d)