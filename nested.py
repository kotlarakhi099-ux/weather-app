calc_to_units=24
nm_of_units="hours"
def days_to_units(num_of_days):
    return f"{num_of_days}days are{num_of_days*calc_to_units}{nm_of_units}"
def execute():
    user_input=input("enter a no:")
    if user_input.isdigit():
        user_input_num=int(user_input)
        if user_input_num > 0:
          calc_value=days_to_units(user_input_num)
          print(calc_value)
        elif user_input_num==0:
           print("you entered zero")
        else:
           print("entered neg value")
    else:
        print("not a valid no")
execute()
