
#store the word to guess
word = "mango"

#store length of word
lengthOfWord = len(word)

#store max number of attempts allowed 
numOfAttempts=5

#store number of attempts taken so far
attempts=0

#store number of correct letters guessed so far 
numOfLetterGuessed=0

#store letters list guessed by user so far
lettersGuessed=[]

#store how partial word look like from correct guessed letters so far
partialword=["_"] * lengthOfWord

#store if user has
win = False


while (attempts < numOfAttempts):

   #first show user what letters he has guessed so far and how partial guessed word looks like
   print("so far you have guessed: "+str(lettersGuessed))
   print("so far partial word guessed: " + str(partialword))

   #take input from user
   guess=input("\nwhat is your guess: ")

   if (guess in lettersGuessed):
       print("this letter/word is already guessed")
       continue      
   else:
       lettersGuessed.append(guess)
       

   attempts = attempts + 1
   
   #check if user has guessed the complete word in a single go
   if len(guess) > 1:
       if guess == word:
           win = True
           break
       else:
            print("wrong guess")
            continue
            
   #check if user has guessed a correct letter
   if (guess in word):
       print(guess+" is correct")
       numOfLetterGuessed = numOfLetterGuessed + word.count(guess);
   else:
       print("wrong guess")


   #check if user has guessed all the letters
   if(numOfLetterGuessed==lengthOfWord):
       win = True
       break
        
   #partial word using correct guessed letters so far
   for n in range(0,lengthOfWord):
        if(word[n]==guess):
            partialword[n]=guess
           
    
if (win == False):
    print("you are out of attempts - you lost")
else:
    print("you win")
    print("the word was: "+str(word))
        
