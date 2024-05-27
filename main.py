# input statements
salary = float(input("Enter employee salary: "))
salary = 1250.0
numDependents = float(input("Enter the number of dependents: "))
numDependents = 2

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = numDependents * (salary * 0.025)
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
