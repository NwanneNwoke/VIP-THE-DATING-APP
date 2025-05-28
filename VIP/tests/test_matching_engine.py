from VIP.matching_engine import match_users_by_salary

class MockUser:
    def __init__(self, name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income

def test_match_users_by_salary():
    users = [MockUser("A", 3000), MockUser("B", 3200), MockUser("C", 4000)]
    matches = match_users_by_salary(users, "A", 2900, 3300)
    assert len(matches) == 1 and matches[0].name == "B"
