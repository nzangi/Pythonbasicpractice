"""
1.write a program that asks a users some several questions
2. Ensure you have provided an answer for each question
3. Award points in each question and IF student fails provide him/her with a answer for question asked
4. Award the student marks using these method. if he scores during first trial give him/her 3 points, stage TWO give
him/her 2 points , stage 3 give him/her 1 point and if he/she fails the three trials give him/her 0 point.
5. if user enter a answer not in the list, display "Answer Not in the List"
6. calculate the total sum of the points tne student has scored and display the points for the student.
"""

# NB: how to make a list to lower using lower() TOMORROW
# def ask_questions(questions):
# this code tries to find the correct from user and according to which stage the user answer's he is
# rewarded his points and if he fails he is provided with answer.
# while True:
points = []
questions = ["What is your name of your country? ", "2. Which is your letter ? "]
answers = [['KENYA', 'UGANDA', 'RWANDA', 'BURUDI'], ['A', 'B', 'C', 'D']]

indexes = [1, 1]


def answer_question(question, answers, index):
    point = 0
    trials = 0
    running = True
    while running:
        print(question)
        for answer in answers:
            print('\t' + answer)
        answer = input(":")
        if answer == answers[index]:
            trials = trials + 1
            if trials == 1:
                point = 3
            elif trials == 2:
                point = 2
            else:
                point = 1
            print(f"The answer {answer} is correct, your score is {point} points\n")

            break
        else:
            trials = trials + 1
            print(f"{answer} is wrong answer, please trial again, {3 - trials} trials remaining")
            if trials >= 3:
                print(f"The correct answer for the question is {answers[index]}.\n")
                break
    return point


for question in questions:
    index = questions.index(question)
    total_points = answer_question(question, answers[index], indexes[index])
    points.append(total_points)

    print(f"Your Total points in the attempted questions is: {sum(points)} Points")

# country_city = input(print(f"What is your {country} city: "))
# county = input(print(f"What is your county in {country}: "))
# county_city = input(print(f"What is your {county} city in {country}: "))
# official_names = input(print(f"What is your official names in {country} republic: "))
# return country, country_city, county, county_city, official_names
