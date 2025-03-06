def calculate_sss_deduction():
    return 1200

def calculate_philhealth_deduction(salary):
    return (salary * 0.05) / 2

def calculate_pagibig_deduction():
    return 100

def calculate_tax_deduction():
    return 1875

def calculate_total_deductions(salary):
    sss = calculate_sss_deduction()
    philhealth = calculate_philhealth_deduction(salary)
    pagibig = calculate_pagibig_deduction()
    tax = calculate_tax_deduction()
    return sss + philhealth + pagibig + tax

def calculate_net_salary(salary):
    total_deductions = calculate_total_deductions(salary)
    return salary - total_deductions

def main():
    salary = float(input("Enter your monthly salary: "))
    net_salary = calculate_net_salary(salary)

    print("Gross Salary:", salary)
    print("SSS Deduction:", calculate_sss_deduction())
    print("PhilHealth Deduction:", calculate_philhealth_deduction(salary))
    print("Pag-IBIG Deduction:", calculate_pagibig_deduction())
    print("Tax Deduction:", calculate_tax_deduction())
    print("Total Deductions:", calculate_total_deductions(salary))
    print("Net Salary:", net_salary)

if __name__ == "__main__":
    main()