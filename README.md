# Salary Deduction Calculator

This is a simple Python program to calculate monthly salary deductions and net salary.

## Features:
- Calculates SSS, PhilHealth, Pag-IBIG, and tax deductions.
- Computes net salary after deductions.
- Includes input validation and error handling.

## Improvements Made:
1. Improved variable and function names for better readability.
2. Split the code into modular functions for better reusability and maintainability.
3. Added input validation and error handling to ensure the salary is a valid, non-negative number.

## Test Cases
    Test Case: Valid Salary Input
        Input: 50000 (monthly salary)
        Expected Output:
            Gross Salary: 50000.0
            SSS Deduction: 1200
            PhilHealth Deduction: 1250.0
            Pag-IBIG Deduction: 100
            Tax Deduction: 1875
            Total Deductions: 4425.0
            Net Salary: 45575.0

    Test Case: Zero Salary Input
        Input: 0 (monthly salary)
        Expected Output:
            Gross Salary: 0.0
            SSS Deduction: 1200
            PhilHealth Deduction: 0.0
            Pag-IBIG Deduction: 100
            Tax Deduction: 1875
            Total Deductions: 3175.0
            Net Salary: -3175.0
    

## Challenges Faced:
- Handling edge cases in input validation (e.g., negative values, non-numeric inputs).
- Ensuring modular functions are reusable and maintainable.

## How to Run:
1. Clone the repository.
2. Run the script using Python:
   ```bash
   python salary_calculator.py