def calculate_bonus(salary):
    if salary >= 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    return bonus

def is_high_salary(salary):
    return salary >= 30000

