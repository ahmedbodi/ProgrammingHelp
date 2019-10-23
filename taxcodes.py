employeeGrossSalary = float(raw_input("Enter Gross Salary: "))
print("Employee Gross Salary is: %s" % employeeGrossSalary)

employeeTaxCode = raw_input("Enter Tax Code: ")
print("Employee Tax Code is: %s" % employeeTaxCode)

employeePension = employeeGrossSalary * 0.05
print("Employee Pension is %s" % employeePension)

employersPension = employeeGrossSalary * 0.075
print("Employers Pension is %s" % employeePension)

totalPension = employeePension + employersPension
print("Total Pension is %s" % totalPension)

employeeGrossAfterPension = employeeGrossSalary - totalPension
print("Employee Gross Salary is %s" % employeeGrossAfterPension)

employeePersonalAllowance = 0

if employeeTaxCode.endswith('Z'):
    employeePersonalAllowance += 1000

employeePersonalAllowance += int(employeeTaxCode[0:3]) * 10

print("Employee Personal Allowance is %s" % employeePersonalAllowance)
