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

SAMPLE_STRING = 'hello world'
find_lenght_of_string(SAMPLE_STRING)
