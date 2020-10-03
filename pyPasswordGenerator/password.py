import random
import string

# https://www.grc.com/ppp.html

def generator(length=8, upper=2, digits=2, symbol=1, set= 's'):
    if set == 's':
        # This is the standard and conservative PPP set of 64 characters. 
        # It was chosen to remove characters that might be confused with one another. 
        # Using 4-characters per passcode, 16,777,216 passcodes are possible for very 
        # good one time password security
        passcode_set = '!#%+23456789=?@ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    elif set == 'v' :
        # This is a much more "visually aggressive" (somewhat more interesting 
        # and certainly much stronger) 88-character alphabet which supports 
        # the generation of 59,969,536 possible 4-character passcodes:
        passcode_set = '''!"#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~'''
    else: 
        passcode_set = set

    def _get_char(char_type, length, max= 100):
        i, l, ch = 1,0, []
        while i <= length:
            _s = random.choice(char_type)
            if _s in passcode_set:
                ch.append(_s)
                i += 1
            if l > max:
                print('Error:', 'exceeding max loop, cannot find valid passcode in set:', str(char_type))
                break
            l += 1
        return ch

    _lower = _get_char(string.ascii_lowercase, length-upper-digits-symbol)
    _upper = _get_char(string.ascii_uppercase, upper)
    _number = _get_char(string.digits, digits)
    _symbol = _get_char(string.punctuation, symbol)
    _password = _lower + _upper + _number + _symbol
    return ''.join(random.sample(_password, len(_password)))

if __name__ == "__main__":
    generator(length=8, upper=2, digits=2, symbol=0, set= 's')