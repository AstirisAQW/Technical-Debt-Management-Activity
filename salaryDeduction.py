def calculate_net_salary(salary):
    sss_deduction = 1200
    philhealth_deduction = (salary * 0.05) / 2
    pagibig_deduction = 100
    tax_deduction = 1875  # Assuming fixed value for simplicity

    total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    net_salary = salary - total_deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_deduction)
    print("PhilHealth Deduction:", philhealth_deduction)
    print("Pag-IBIG Deduction:", pagibig_deduction)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
calculate_net_salary(salary)