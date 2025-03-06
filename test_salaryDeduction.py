import unittest
from salaryDeduction import (
    calculate_sss_deduction,
    calculate_philhealth_deduction,
    calculate_pagibig_deduction,
    calculate_tax_deduction,
    calculate_total_deductions,
    calculate_net_salary,
)

class TestSalaryDeduction(unittest.TestCase):
    def test_calculate_sss_deduction(self):
        self.assertEqual(calculate_sss_deduction(), 1200)

    def test_calculate_philhealth_deduction(self):
        self.assertEqual(calculate_philhealth_deduction(50000), 1250.0)
        self.assertEqual(calculate_philhealth_deduction(0), 0.0)
        self.assertEqual(calculate_philhealth_deduction(1000000), 25000.0)

    def test_calculate_pagibig_deduction(self):
        self.assertEqual(calculate_pagibig_deduction(), 100)

    def test_calculate_tax_deduction(self):
        self.assertEqual(calculate_tax_deduction(), 1875)

    def test_calculate_total_deductions(self):
        self.assertEqual(calculate_total_deductions(50000), 4425.0)
        self.assertEqual(calculate_total_deductions(0), 3175.0)
        self.assertEqual(calculate_total_deductions(1000000), 28175.0)

    def test_calculate_net_salary(self):
        self.assertEqual(calculate_net_salary(50000), 45575.0)
        self.assertEqual(calculate_net_salary(0), -3175.0)
        self.assertEqual(calculate_net_salary(1000000), 971825.0)

if __name__ == "__main__":
    unittest.main()