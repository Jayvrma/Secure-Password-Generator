import random
import string

length_of_password = random.randint(12, 16)
# upper lower number symbol
number_of_cases = [3, 3, 3, 3]


def calculating(cases):
    if sum(cases) < length_of_password:
        x = random.randint(0, 3)
        match x:
            case 0:
                cases[0] += 1
            case 1:
                cases[1] += 1
            case 2:
                cases[2] += 1
            case 3:
                cases[3] += 1
        return calculating(cases)
    else:
        return cases


calculating(number_of_cases)


def list(type, target_num, count, password_list):
    if count >= target_num:
        return password_list
    match type:
        case 0:
            password_list.append(random.choice(string.ascii_uppercase))
        case 1:
            password_list.append(random.choice(string.ascii_lowercase))
        case 2:
            password_list.append(random.choice(string.digits))
        case 3:
            password_list.append(random.choice(string.punctuation))
    return list(type, target_num, count + 1, password_list)


full_pass = (
    list(0, number_of_cases[0], 0, [])
    + list(1, number_of_cases[1], 0, [])
    + list(2, number_of_cases[2], 0, [])
    + list(3, number_of_cases[3], 0, [])
)
random.shuffle(full_pass)

print("".join(full_pass))
