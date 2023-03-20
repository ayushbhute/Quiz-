print ("welcome to QUIZ")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
  quit()   

print ("Lets go on : ")
score = 0

answer= input("1. What does WWW stands for?  ")
if answer.lower()== "world wide web":
  print ("well done")
  score +=1
else:
    print ("oops! incorrect")


answer= input("2. What does IOT stands for?  ")
if answer.lower()== "internet of things":
  print ("well done")
  score +=1
else:
    print ("oops! incorrect")


answer= input("3. What does ML stands for?  ")
if answer.lower()== "machine learning":
  print ("well done")
  score +=1
else:
    print ("oops! incorrect")


answer= input("4. What does EC stands for?  ")
if answer.lower()== "electronics communication ":
  print ("well done")
  score +=1
else:
    print ("oops! incorrect")


answer= input("5. What does CS stands for?  ")
if answer.lower()== "computer science":
  print ("well done")
  score +=1
else:
    print ("oops! incorrect")

print ("your score is = " + str((score)/5 *100) + "%")
