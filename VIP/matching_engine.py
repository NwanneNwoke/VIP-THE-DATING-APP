def match_users_by_salary(users, target_name, min_salary, max_salary):
    target_user = next((u for u in users if u.name == target_name), None)
    if not target_user:
        return []

    matches = []
    for user in users:
        if user.name == target_user.name:
            continue
        if min_salary <= user.monthly_income <= max_salary:
            matches.append(user)
    return matches
