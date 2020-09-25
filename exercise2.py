annual_salary= int(input("Please enter your current annual salary: "))
monthly_salary = (annual_salary/12)
print('monthly_salary:', + monthly_salary)
department_code = (input("please enter your depeartment code: "))
A = 0.072
B = 0.068
C = 0.063

if department_code=="A":
    print('new_salary:',monthly_salary * A + monthly_salary)
elif department_code =="B":
    print('new_salary:',monthly_salary * B + monthly_salary)
elif department_code=="C":
    print('new salary:', monthly_salary * C + monthly_salary)
