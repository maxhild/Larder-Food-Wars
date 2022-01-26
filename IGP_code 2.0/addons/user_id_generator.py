import string
import random

class User_ID_Creator:

    def generate_string(self, digits):
        gen_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=digits))
        return gen_string

    def generate_integer(self, digits):

        x = [random.randint(0, 9) for p in range(0, digits)]
        str_x = [str(x) for x in x]
        up_x = "".join(str_x)
        gen_int = int(up_x)
        return gen_int

    def generate_password(self, user_id_int, user_id_string):

            first_dig = int(str(user_id_int)[:1])

            if user_id_int + first_dig > 2:
                first_dig = str(first_dig)
                password_str = str(user_id_int) + user_id_string
                password_lst = list(password_str)
                random.shuffle(password_lst)
                password_lst.insert(0, first_dig)
                fin_password = "".join(password_lst)
                return fin_password

def users_id():
    digits = 5
    user_id = User_ID_Creator()
    user_id.generate_string(digits)
    user_id.generate_integer(digits)
    return user_id.generate_password(user_id.generate_integer(digits), user_id.generate_string(digits))
