from salary_utils import calculate_monthly_salary
from matching_engine import match_users_by_salary

class UserProfile:
    def __init__(self, name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income

    def __repr__(self):
        return f"{self.name} - ${self.monthly_income}/month"

# Sample user creation from paystub
paystubs = {
    "Alice": [3000, 3200, 3100, 3050],  # weekly pay for 1 month
    "Bob": [4000, 4000, 4000, 4000],
    "Charlie": [2500, 2600, 2700, 2800]
}

users = []
for name, stubs in paystubs.items():
    monthly = calculate_monthly_salary(stubs)
    users.append(UserProfile(name, monthly))

# Match based on income range
matches = match_users_by_salary(users, "Alice", 2900, 3300)
print("Matches for Alice:")
for match in matches:
    print(match)
