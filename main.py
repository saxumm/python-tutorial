

name_of_unit = "hours"
calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}\n"


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number\n")
        else:
            print("you entered a negative number, please enter a valid positive number\n")
    except ValueError:
        print("your input is not a valid number.\n")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

    for num_of_days_element in user_input.split(","):
        if num_of_days_element == "exit":
            print("Thank you for using our program\n")
            user_input = "exit"
            break
        else:
            validate_and_execute()
