# PasswordGenerator
[![PyPI version](https://img.shields.io/badge/PYPI-V%202.1.0-blue.svg)](https://github.com/cove9988/PasswordGenerator)
[![Build Status](https://travis-ci.org/cove9988/PasswordGenerator.svg?branch=master)](https://github.com/cove9988/PasswordGenerator)
[![Updates](https://pyup.io/repos/github/cove9988/PasswordGenerator/shield.svg)](https://github.com/cove9988/PasswordGenerator)

Working on a project recently, which requires generating random secured passwords for users, sounds simple? Yeah, me too, I quickly rolled out my first version, a random password generator, then found out not happy with how to control password length, how many uppercases, digitals, symbols apply in a password. Worked out the second version, guess what? Not happy again, with some char sets like, o 0 O, I 1 l, which are a bit visually aggressive in password. Also some applications accept limited symbols.

So I did a bit of research on this topic, a heap of libraries available there, but either too complex to configure or too simple like my old one.

Coding a library for the community? Let's do it....then, I realized that I have to refactor my code, because you don't want to present you sh*t code to the public. In a library, every line of code should be accountable and elegant. Not mention that you need to have a good comprehensive document with examples. And version control, change log , setup, deployment are all must. A lot of work ahead.


### Password Generator

based on [Perfect Paper Passwords](https://www.grc.com/ppp.html)

>High security multifactor authentication password generator.

### standard passcode set
This is the standard and conservative PPP set of 64 characters. It was chosen to remove characters that might be confused with one another. Using 4-characters per passcode, 16,777,216 passcodes are possible for very good one time password security

passcode_set = '!#%+23456789=?@ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

#### example: 
use standard set to create password length = 10, with 3 uppercases, 3 digits and 1 symbol 
```
from pyPasswordGenerator import password as ps
# standard set
set = 's' 
ps.generator(length = 10, upper = 3, digits =3, symbol = 0, set =set  )
>>>'5v5njx9BAN'
```

### visually aggressive passcode set
This is a much more "visually aggressive" (somewhat more interesting 
and certainly much stronger) 88-character alphabet which supports 
the generation of 59,969,536 possible 4-character passcodes:

passcode_set = '''!"#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~'''

#### example
use standard set to create password length = 8, with 2 uppercases, 2 digits and 2 symbol 
```
from pyPasswordGenerator import password as ps
# visually aggressive set
set = 'v' 
ps.generator(length = 8, upper = 2, digits =2, symbol = 2, set =set  )
>>>'sX65%A^g'
```

use won set to limit symbol with only !#@

#### use your set create password length = 12, with 4 uppercases, 2 digits and 2 symbols 
```
from pyPasswordGenerator import password as ps

# my own password set
set = '!#23456789@ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
ps.generator(length = 11, upper = 4, digits =2, symbol = 2, set =set  )
>>>'@F8Wa#jRn6S'
```

### Definition
| Parameter    | Default             | Description 
| :------ | :------------------ | :--------- 
| length | 8   | Length of Password, if length = 10 then xdat3a9$dg
| upper | 2   | How many upper case charactors, if upper =4 GdAT3a9$Dg
| digits | 2   |How many digits, if digits = 1 GdAT3ad$Dg
| symbol | 0  | How many symbol if symbol=4 G#A!3a9$D!
| passcode_set | s|v|{your own set}   | 

### installation
```
pip install pyPasswordGenerator
```
