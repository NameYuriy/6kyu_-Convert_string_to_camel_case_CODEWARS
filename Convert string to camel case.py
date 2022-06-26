def to_camel_case(text):
    s = text.replace('_', ' ')
    s = s.replace('-', ' ')
    s = s.split(' ')
    for i in range(1, len(s)):
        s[i] = s[i].capitalize()
    s = ''.join(s)
    return s