
#Part A: Functions for Mathematical functions
print("****************************")
print("           ADDITION")
print("****************************")
def addition():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        total = num1 + num2

        return total
    except ValueError:
        return "Please Enter Valid Number."

result = addition()
print("The Sum is: ", result)
print("")
print("****************************")
print("          SUBTRACTION")
print("****************************")
def subtraction():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        difference = num1 - num2

        return difference
    except ValueError:
        return "Please Enter Valid Number."

result = subtraction()
print("The Difference is: ", result)
print("")
print("****************************")
print("         Multiplication")
print("****************************")
def Multiplication():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        answer = num1 * num2

        return answer
    except ValueError:
        return "Please Enter Valid Number."

result = Multiplication()
print("The answer is: ", result)
print("")
print("****************************")
print("         Division")
print("****************************")
def Division():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        answer = num1 / num2

        return answer
    except ValueError:
        return "Please Enter Valid Number."

result = Division()
print("The answer is: ", result)
print("")
print("")

#part B: working with Lists

num_list = [30, 255, 55, 60, 12]

def add_number(num):
    num_list.append(num)
def remove_number(num):
    try:
        num_list.remove(num)
    except ValueError:
        return "Error: Number Not Found."

def find_average():
    if len(num_list) == 0:
        return "Error: The list is empty."
    return sum(num_list) / len(num_list)

def find_maximum():
    if len(num_list) == 0:
        return "Error: The list is Empty."
    return max(num_list)

def find_minimum():
    if len(num_list) == 0:
        return "Error: The list is empty."
    return min(num_list)

add_number(3)
remove_number(55)
average = find_average()
maximum = find_maximum()
minimum = find_minimum()

print("Update num_list: ", num_list)
print("Average: ", average)
print("Maximum: ", maximum)
print("Minimum: ", minimum)

#Part C: Working with Dictionaries
student_scores = {
    "Thabani": 85,
    "Furman": 80,
    "Bonkhe": 92,
    "Lele": 98,
    "David": 60
}
def add_student(name, score):
    student_scores[name] = score

def update_student_score(name, score):
    if name in student_scores:
        student_scores[name] = score
    else:
        return "Error: Student not found "

def remove_student(name):
    if name in student_scores:
        del student_scores[name]
    else:
        return "Error: Student not found."

def retrieve_student_score(name):
    return student_scores.get(name, "Error: Student not found.")

def calculate_average_score():
    if len(student_scores) == 0:
        return "Error: No students in the class."
    return sum(student_scores.values()) / len(student_scores)

def find_highest_score():
    if len(student_scores) == 0:
        return "Error: No student in the class."
    highest_student = max(student_scores, key=student_scores.get)
    return highest_student, student_scores[highest_student]


add_student("Simulindele", 98)
update_student_score("Furman", 100)
remove_student("David")
average = calculate_average_score()
highest_student, highest_score = find_highest_score()

print("Updated student_Scores: ", student_scores)
print("Average Score: ",average)
print("Highest score: ",highest_student,"With a score of : ", highest_score)

    




































































































































