import datetime

user_input = input("Enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)