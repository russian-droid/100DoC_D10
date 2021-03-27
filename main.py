#following Udemy course: 100 days of code by Angela Yu

#------------------------------days in month--------
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.")
        return True
      else:
        #print("Not leap year.")
        return False
    else:
      #print("Leap year.")
      return True
  else:
    #print("Not leap year.")
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days=month_days[month-1]
    year=is_leap(year)

    if year == True:
        if month == 2:
            days = 29
        else: 
            days=month_days[month-1]
    else:
        days
    
    return days
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

#add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  '+':add, #make sure in this case values are not saved as strings!
  '-':subtract,
  '*':multiply,
  '/':divide,
}

num1 = int(input('First number:\n'))

def calc_loop (num1):
  print('\nAvailable operations:')
  for symbol in operations:
      print (symbol)
  operation_symbol = input('Enter an operation from available above:\n')

  num2 = int(input('Next number:\n'))
  calc_function = operations[operation_symbol]
  answer = calc_function(num1, num2)
  print(f'\n{num1} {operation_symbol} {num2} = {answer}')

  return answer

#main loop
running = True #change it later in the loop to stop
while running: #same as: while running == True
    num1=calc_loop(num1)

    running_flag = input("Keep calculating with TOTAL?\n(enter 'n' for EXIT, or 'y' for yes)\n")
    if running_flag == 'n': #only 'n' is checked, any other button would give 'yes'
        running = False
        print('the end...')
