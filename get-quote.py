from code import interact
import random

# ask user if they want to insert quotes or see quotes 
def start():
  answer = input("Would you like to add a quote? y/n \t").lower().strip()

  print()

  if answer == "y":
    insert()
  elif answer == "n":
    print("Now printing 3 random quotes...")
    primary()
  else:
    print("Not really sure what that means... So, I'll print some quotes :)")
    primary()


# get quotes and print them 
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1

  # print 3 different random numbers 
  randoms = random.sample(range(0,last), 3)
  
  print()

  for num in randoms:
    print(quotes[num], end="")

  #rnd = random.randint(0,last)
  #print(quotes[rnd])


# add quote to file 
def insert():
  answer = input("What words of wisdom do you have?  ")

  f = open("quotes.txt", 'a')
  f.write("\n" + answer)
  f.close()

  print("All done!\n")
  start()


if __name__== "__main__":
  start()
