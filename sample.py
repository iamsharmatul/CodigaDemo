"""
Provides lenght of string function
"""

def find_lenght_of_string(string: str) -> int:
    '''
        finds the length of the string
    '''

    if not string:
        return 0
    str_input = f'{string}'
    _str_length = len(str_input)
    return _str_length

# Some random code to check the codiga is working or not
def make_complex(*args):
    x, y = args
    return dict(**locals())

SAMPLE_STRING = 'hello world'
find_lenght_of_string(SAMPLE_STRING)
