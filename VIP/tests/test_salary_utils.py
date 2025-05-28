from VIP.salary_utils import calculate_monthly_salary

def test_calculate_monthly_salary():
    assert calculate_monthly_salary([1000, 1000, 1000, 1000]) == 4000
