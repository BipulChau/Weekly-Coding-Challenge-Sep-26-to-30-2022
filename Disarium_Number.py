# Disarium Number (Python)
# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.

# Examples
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32
# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# is_disarium(544) ➞ False
# is_disarium(518) ➞ True
# is_disarium(466) ➞ False
# is_disarium(8) ➞ True
# Notes
# Position of the digit is 1-indexed.


def check_disarium_number(num):
    str_num = str(num)
    num2 = 0
    for i in range(len(str_num)):
        n = int(str_num[i])
        num2 += n ** (i + 1)
    if num == num2:
        return True
    return False


print(check_disarium_number(75))  # False
print(check_disarium_number(135))  # True
print(check_disarium_number(544))  # False
print(check_disarium_number(518))  # True
print(check_disarium_number(466))  # False
print(check_disarium_number(8))  # True
