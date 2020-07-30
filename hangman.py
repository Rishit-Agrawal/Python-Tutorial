#HANGMAN PROJECT

# Hangman-
#You have to guess the word
#You can guess a letter or a complete word
#If you guess the letter correctly, the program will tell you all the locations of the letter in the word.
#You will be given 5 attempts to guess the word

import random 

def getWord():
   words = ['banana', 'computer', 'mango']
   return random.choice(words) 


#store the word to guess
word = getWord()

# any number of turns can be used here
turns=5

#store length of word
lengthOfWord = len(word)

#store all the letters guessed by user so far
lettersGuessed=[]

#store how partial word look like from correct guessed letters so far
partialCorrectWord="*"*lengthOfWord
   

#tell if user has won
win = False

while (turns > 0):

   #first show user what letters he has guessed so far and how partial guessed word looks like
   print("so far you have guessed: "+str(lettersGuessed))
   print("so far partial word guessed: " + partialCorrectWord)

   #take input from user
   guess=input("\nwhat is your guess: ")

   if (guess in lettersGuessed):
       print("this letter/word is already guessed")
       continue      
   
   lettersGuessed.append(guess)
   turns = turns - 1
   
   #check if user has guessed the complete word in a single go
   if len(guess) > 1:
       if guess == word:
           win = True
           break
       else:
            print("wrong guess")
            continue
            
   #check if user has guessed a correct letter
   if (guess not in word):
       print("wrong guess")
       continue
   

   print(guess+" is correct")
   
   #partial word using correct guessed letters so far
   for n in range(0,lengthOfWord):
        if(word[n]==guess):
            partialCorrectWord = partialCorrectWord[:n] + guess + partialCorrectWord[n+1:]


   #check if user has guessed all the letters
   if(partialCorrectWord==word):
       win = True
       break         
           
    
if (win == False):
    print("you are out of attempts- sorry you loose")
    print("the word was: "+str(word))
else:
    print("you win")
    print("the word was: "+str(word))
        
