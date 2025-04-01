# In here is the beigganing of the so call group 
import random 

# In here we are telling it to gennerte a random number in the range of 0 to 100
number=random.randint(0,100)
 
# In here is the beigganing of the so call group
print("Guess the magic number between 0 and 100")

# We use the equal is assign that to the memory call guess
guess=-1

# This is saying that they are going to repeat anything until is not equal 
while guess!=number
guess=int(input("|nEnter your guess:"))

if guess==number
print(f"Yes, the number is {number}")

elif guess>number:
print("your guess is too high")

else:
print("Your guess is too low")
