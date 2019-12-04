from collections import Counter
passwords = []

def validatePassword(num):
    num = str(num)
    duplicates = [i for i,j in Counter(num).items() if j>1]
    for index, digit in enumerate(num):
        if index > 0:
            prevNum = num[index - 1]
            if not (digit == prevNum or digit > prevNum) or len(duplicates) < 1:
                return []
    return([num])


for num in range(235741, 706948):
    r = validatePassword(num)
    passwords += r

print(len(passwords))
def part2filter(password):
    C = Counter(password)
    if 2 in C.values():
        return True
    return False

part2 = 0
for password in passwords:
    if part2filter(password):
        part2 += 1

print(part2)
