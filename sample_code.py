def check_string_length(usr_input: str) -> int:
    if not usr_input:
        return 0
    str_input = f'{usr_input}'
    _str_length = len(str_input)
    return _str_length

if __name__ == '__main__':
    usr_input = 'Hello World'
    check_string_length(usr_input)
