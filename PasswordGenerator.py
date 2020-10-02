import random
import string

def generate_password(length=18, upper = 2, digits = 2, symbol = 2, symbol_only =['-','_','!','%']):
    # At lest how manu upper, number and symbol 
    #randomly select ascii character lower
    _lower = [random.choice(string.ascii_lowercase) for _ in range(length-upper-digits-symbol)]
    _upper = [random.choice(string.ascii_uppercase) for _ in range(upper)]
    _number = [random.choice(string.digits) for _ in range(digits)]
    i = 1
    _symbol = []
    if symbol_only:
        while i <= symbol:
            _s = random.choice(string.punctuation) 
            if _s in symbol_only :
                _symbol.append(_s)
                i += 1
    else:
        _symbol = [random.choice(string.punctuation) for _ in range(symbol)]
    _password = _lower + _upper + _number + _symbol       
    return ''.join(random.sample(_password, len(_password)))
