
def calculate_bonus(salary):
    if salary >= 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    return bonus

def is_eligible_for_bonus(salary):
    if salary >= 50000:
        print(f"Eligble for bonus")
    else:
        print(f"Not Eligible for bonus")
    

