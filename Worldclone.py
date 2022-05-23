import random

def processGuess(theAnswer, theGuess):
  position = 0
  clue = ""
  for letter in theGuess:
    if letter == theAnswer[position]:
      clue += "G"
    elif letter in theAnswer:
      clue += "Y"
    else:
      clue += "*"
    position += 1
  print(clue)
  return clue == "GGGGG" 

#load words and store them a list
word_list = ["happy","awake","blush","focal","vocal","evade","naval","serve","model","camle","grade","quiet","quite","bench","major","minor","fresh","crust","stool","colon","marry","react","pride","staff","paper"]


#pick a word
answer = random.choice(word_list)
#print(answer)
poss = random.randint(0, 4)

print("NOTE-:\n Y - if your letter is present in the correct word but not at right position\n G - if your letter is on the right position in the correct word \n * - if letter is not exist ")
print("\n************BEST OF LUCK GAME STARTED *************\n")
num_of_guesses = 0
guessed_correctly = False
chances = 10
while num_of_guesses < 10 and not guessed_correctly:
  #get guess from user
  print("You have", chances ," chances to win the game")
  print("HINT -:position ",poss+1, " of this word is ",answer[poss] )
  guess = input("Input your 5-letter word and press enter: ")
  print("Your guesse is : ", guess)
  num_of_guesses += 1
  chances -= 1 

  #process guess
  guessed_correctly = processGuess(answer, guess)

#display end of game message
if guessed_correctly:
  print("Congratulations! You guessed the correct word in", num_of_guesses, "times!")
else:
  print("You have used up your guesses...the correct word is", answer)