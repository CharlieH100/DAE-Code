#This program is a survey to check if the user qualifies for college classes at
#PTECH Norwalk


#This asks the user for their name and is the start o this program
name = input("What's your name? ")
print("Welcome to my survey " + name)
print("This survey is going to determin if you are eligible to P-TECH college classes! ")
print("")

#This score is a counter for how many requirements the user has met
score = 0

#This function adds 1 to the score and initializes it 
def add_point(score):
    score += 1
    return score 

#This if/else section asks the user for their PSAT score
PSAT = int(input("Enter your PSAT score: "))
#then checks if its above a certain threshold and adds a point if true
if PSAT < 1000:
    print("The minimum score is 1000 for the PSAT")
    print("")
else:
    score = add_point(score)  # Call the add_point function to increase the score
    print("Great!")
    print("")

# Asks for the users gpa
GPA = float(input("Enter your GPA (e.g., 2.3): "))  # Use float to handle decimal values
#if the user's gpa meets the threshhold, it adds a point to score
if GPA < 3.0:
    print("The minimum GPA is 3.0")
    print("")
else:
    score = add_point(score)
    print("Congrats!")
    print("")
#Asks the user a true or false question 
math_and_english_grade = input("Do you have at least a 'B' in your English + Math class? (true/false): ")
# Check if the user's response is 'yes' (case-insensitive) and adds a point if so
if math_and_english_grade.lower() == "true":
    print("Keep it up!!!")
    score = add_point(score)
    print("")
else:
    print("Keep trying!!!")
    print("")

#List of college classes
college_classes = ["Web Dev 1", "Freshman Seminar","XML Spreadsheet", "Art 1", "College art", "Math but with more funky numbers"]

#This function prints out the results if they user is qualified
#This depends on the score count and gives two different outcomes
def results():
  print("Your score is: " + str(score) + " out of 3.")
  print("")
  #This prints if the user did not qualify as they met less than 2 of the requirements
  if score < 2:
        print("because your score is less than 2")
        print ("it means that you are not eligible for college classes...")
        print("womp womp")
        print("")
  #This prints if the user meets at least 2 of the requirements
  else:
    print("Congrats!!!")
    print("You qualify for college classes!!")
    print("")
    print("Available college classes:")
    #This loops through the college_classes list and prints each course in the list
    for course in college_classes:
        print(course)

#this calls out the function to print our the final results
results()