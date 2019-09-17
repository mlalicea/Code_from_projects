import string
from random import randint, choice, choices, sample, shuffle

def password_specs(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    spec = randint(min_spec,(length - min_num - min_upper))
    num = randint(min_num,(length - spec - min_upper))
    upper = randint(min_upper,(length - spec - num))
    lower = length - spec - num - upper
    return[spec, num, upper, lower]

def password_gen(length = 14, spec_char = '@!&', repeat = True, min_spec = 0, min_num = 0, min_upper = 0):
    required = [min_upper, min_num, min_spec]
    if sum(required) <= length and repeat or len(spec_char) >= min_spec:
        specs = password_specs(length, min_spec, min_num, min_upper)
        if(repeat):
            password = choices(string.ascii_lowercase, k=specs[3]) + choices(string.ascii_uppercase, k=specs[2]) + choices(string.digits, k=specs[1]) + choices(spec_char, k=specs[0])
        else:
            ok = True
            while ok:
                specs = password_specs(length, min_spec, min_num, min_upper)
                if specs[0] <= len(spec_char) and specs[1] <= len(string.digits) and specs[2] <= len(string.ascii_uppercase) and specs[3] <= len(string.ascii_lowercase):
                    ok = False
            password = sample(string.ascii_lowercase, specs[3]) + sample(string.ascii_uppercase, specs[2]) + sample(string.digits, specs[1]) + sample(spec_char, specs[0])
        shuffle(password)
        pass_w = ''
        for i in password:
            pass_w += i
        return pass_w
    else:
        print('Invalid specifications!')


def check_password(password, length, min_spec, min_num, min_upper):
    if len(password) == length:
        numbers = []
        nums = '0123456789'
        for check_num in password:
            if check_num in nums:
                numbers += [check_num]
        if len(numbers) >= min_num:
            upper_letters = []
            uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for check_upper in password:
                if check_upper in uppers:
                    upper_letters += [check_upper]
            if len(upper_letters) >= min_upper:
                    special = []
                    lowers = 'abcdefghijklmnopqrstuvwxyz'
                    for check_spec in password:
                        if (check_spec not in nums and check_spec not in uppers and check_spec not in lowers):
                            special += [check_spec]
                    if len(special) >= min_spec:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False


def password_specs_max(length = 14, min_spec = 0, min_num = 0, min_upper = 0, max_spec = 1, max_num = 1, max_upper = 1):
    spec = randint(min_spec,(length - min_num - min_upper and max_spec))
    num = randint(min_num,(length - spec - min_upper and max_num))
    upper = randint(min_upper,(length - spec - num and max_upper))
    lower = length - spec - num - upper
    return[spec, num, upper, lower]

def password_gen_max(length = 14, spec_char = '@!&', repeat = True, min_spec = 0, min_num = 0, min_upper = 0, max_spec = 1, max_num = 1, max_upper = 1):
    required = [min_upper, min_num, min_spec]
    if sum(required) <= length and repeat or len(spec_char) >= min_spec:
        specs = password_specs_max(length, min_spec, min_num, min_upper, max_spec, max_num, max_upper)
        if(repeat):
            password = choices(string.ascii_lowercase, k=specs[3]) + choices(string.ascii_uppercase, k=specs[2]) + choices(string.digits, k=specs[1]) + choices(spec_char, k=specs[0])
        else:
            ok = True
            while ok:
                specs = password_specs_max(length, min_spec, min_num, min_upper, max_spec, max_num, max_upper)
                if specs[0] <= len(spec_char) and specs[1] <= len(string.digits) and specs[2] <= len(string.ascii_uppercase) and specs[3] <= len(string.ascii_lowercase):
                    ok = False
            password = sample(string.ascii_lowercase, specs[3]) + sample(string.ascii_uppercase, specs[2]) + sample(string.digits, specs[1]) + sample(spec_char, specs[0])
        shuffle(password)
        pass_w = ''
        for i in password:
            pass_w += i
        return pass_w
    else:
        print('Invalid specifications!')

def check_password_max(password, length, min_spec, min_num, min_upper, max_spec, max_num, max_upper):
    if len(password) == length:
        numbers = []
        nums = '0123456789'
        for check_num in password:
            if check_num in nums:
                numbers += [check_num]
        if len(numbers) >= min_num and len(numbers) <= max_num:
            upper_letters = []
            uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for check_upper in password:
                if check_upper in uppers:
                    upper_letters += [check_upper]
            if len(upper_letters) >= min_upper and len(upper_letters) <= max_upper:
                    special = []
                    lowers = 'abcdefghijklmnopqrstuvwxyz'
                    for check_spec in password:
                        if (check_spec not in nums and check_spec not in uppers and check_spec not in lowers):
                            special += [check_spec]
                    if len(special) >= min_spec and len(special) <= max_spec:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False
