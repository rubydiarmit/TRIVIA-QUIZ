 # trivia quiz

print("This is a quiz that tests your knowledge on Harry Styles")
'''

'''
name= input("Enter your name: ")
print("Hi there,", name, ".", "Are you ready to start the quiz?")
print("I will ask you 8 questions and give you 3 choices.")
print("Select which choice is the correct answer, A, B, or C.")
print("--------------------------------------")

# set the score of the quiz to 0
score = 0
score = int(score)

#question 1
print("")
print("Question 1: Where is Harry from?")
print("A: Doncaster, England")
print("B: Holmes Chapel, England")
print("C: Mullinger, Ireland")
print("")

Q1answer = "B" # the right answer to question 1
Q1response = input("Your answer: ")

if Q1response == "B" or Q1response == "b":
    print("Correct answer:", Q1answer)
    score = score+1
elif Q1response != "B" or Q1response != "b":
    print("Sorry, incorrect. The correct answer is: ", Q1answer)
    
print("Your current score is", score, "out of 8.")

#question 2
print("")
print("Question 2: What song did Harry sing for his X Factor audition?")
print("A: Isn't She Lovely - Stevie Wonder")
print("B: Ordinary People - John Legend")
print("C: Let Me Love You - Mario")
print("")

Q2answer = "A" # the right answer to question 2
Q2response = input("Your answer: ")

if Q2response == "A" or Q2response == "a":
    print("Correct answer:", Q2answer)
    score = score+1
elif Q2response != "A" or Q2response != "a":
    print("Sorry, incorrect. The correct answer is: ", Q2answer)

print("Your current score is", score, "out of 8.")

#question 3
print("")
print("Question 3: What boyband was Harry in?")
print("A: Backstreet Boys")
print("B: The Wanted")
print("C: One Direction")
print("")

Q3answer = "C" #the right answer to question 3
Q3response = input("Your answer: ")

if Q3response == "C" or Q3response == "c":
    print("Correct answer:", Q3answer)
    score = score+1
elif Q3response != "C" or Q3response != "c":
    print("Sorry, incorrect. The correct answer is: ", Q3answer)

print("Your current score is", score, "out of 8.")

#question 4
print("")
print("Question 4: What was the title of Harry's debut solo album?")
print("A: Harry Styles")
print("B: Sign of the Times")
print("C: Pink")
print("")

Q4answer = "A" #the right answer to question 4
Q4response = input("Your answer: ")

if Q4response == "A" or Q4response == "a":
    print("Correct answer:", Q4answer)
    score = score+1
elif Q4response != "A" or Q4response != "a":
    print("Sorry, incorrect. The correct answer is: ", Q4answer)

print("Your current score is", score, "out of 8.")

#question 5
print("")
print("What is Harry's middle name?")
print("A: James")
print("B: Liam")
print("C: Edward")
print("")

Q5answer = "C" #the right answer to question 5
Q5response = input("Your answer: ")

if Q5response == "C" or Q5response == "c":
    print("Correct answer:", Q5answer)
    score = score+1
elif Q5response != "C" or Q5response != "c":
    print("Sorry, incorrect. The correct answer is: ", Q5answer)

print("Your current score is", score, "out of 8.")

#question 6
print("")
print("Who is Harry's song Carolina about?")
print("A: A blind date he had.")
print("B: The singer Taylor Swift.")
print("C: The Victorias Secret model Camille Rowe")
print("")

Q6answer = "A" #the right answer to question 6
Q6response = input("Your answer: ")

if Q6response == "A" or Q6response == "a":
    print("Correct answer:", Q6answer)
    score = score+1
elif Q6response != "A" or Q6response != "a":
    print("Sorry, incorrect. The correct answer is: ", Q6answer)

print("Your current score is", score, "out of 8.")

#question 7
print("")
print("Harry famously covered this bands song called The Chain.")
print("A: Fleetwood Mac")
print("B: Pink Floyd")
print("C: Led Zeppelin")
print("")

Q7answer = "A" #the right answer to question 7
Q7response = input("Your answer: ")

if Q7response == "A" or Q7response == "a":
    print("Correct answer:", Q7answer)
    score = score+1
elif Q7response != "A" or Q7response != "a":
    print("Sorry, incorrect. The correct answer is: ", Q7answer)

print("Your current score is", score, "out of 8.")

#question 8
print("")
print("Where did Harry work before becoming famous?")
print("A: A Coffee Shop")
print("B: A Bakery")
print("C: His mothers office")
print("")

Q8answer = "B" #the right answer to quesiton 8
Q8response = input("Your answer: ")

if Q8response == "B" or Q8response == "b":
    print("Correct answer:", Q8answer)
    score = score+1
elif Q8response != "B" or Q8response != "b":
    print("Sorry, incorrect. The correct answer is: ", Q8answer)
          

print("--------------------------------------")
print("")
final_score = (score*100/8)
print("Your final score is", str(final_score), "percent.")


