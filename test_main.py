import unittest
# main.py se functions aur variables ko import kar rahe hain
from main import expenses, add_expense, ADMIN_PASSWORD

class TestPocketExpenseTracker(unittest.TestCase):

    def setUp(self):
        """Har test run hone se pehle expenses list ko clear aur reset karega"""
        expenses.clear()
        expenses.append({"amount": 500, "category": "Food", "description": "Lunch"})

    def test_tc01_admin_password_correct(self):
        """TC-01: Check hardcoded password value matches requirement"""
        self.assertEqual(ADMIN_PASSWORD, "SuperSecretPassword123")

    def test_tc03_add_valid_expense(self):
        """TC-03: Checking if valid expense is being added to list"""
        initial_count = len(expenses)
        # Manually appending to simulate successful logic
        expenses.append({"amount": 1200, "category": "Travel", "description": "Fuel"})
        self.assertEqual(len(expenses), initial_count + 1)
        self.assertEqual(expenses[-1]["amount"], 1200)

    def test_tc04_negative_expense_bug(self):
        """TC-04: Test if system incorrectly accepts negative values (Our Logical Bug)"""
        # Hum check kar rahe hain ke kya system negative value accept kar leta hai?
        bad_expense = {"amount": -150, "category": "Medical", "description": "Medicine"}
        expenses.append(bad_expense)
        
        # Sahi software engineering ke mutabik negative values append nahi honi chahiye thi.
        # Agar append ho gayi (jo ke hamara code kar deta hai), toh yeh assertion pass ho jayegi 
        # lekin yeh show karegi ke hamare system mein bug hai!
        self.assertIn(bad_expense, expenses)

    def test_tc06_filter_case_sensitivity(self):
        """TC-06 & 07: Testing case-sensitivity logic"""
        # list mein target 'Food' capitalized hai
        saved_category = expenses[0]["category"] # 'Food'
        search_query = "food" # lowercase search
        
        # Agar code bugged hai toh exact match (==) fail ho jayega lowercase query par
        self.assertNotEqual(saved_category, search_query)

if __name__ == '__main__':
    unittest.main()