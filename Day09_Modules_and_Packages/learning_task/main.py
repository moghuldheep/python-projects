import calculator as cal
from employee import calculate_bonus, is_eligible_for_bonus

addition_result = cal.add(5,10)

print(addition_result)

print(calculate_bonus(60000))
print(is_eligible_for_bonus(30000))
