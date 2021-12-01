guess=10
user_ans= int(input("guess the number:  "))

diff= guess - user_ans
if diff > 5:
    print("you guessed too high")
if guess == user_ans:
    print("you win")
if guess != user_ans:
    print("you lose")
print("run  the program again ")
