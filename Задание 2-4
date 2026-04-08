import re
def count_russian_chars(s):
    count = 0
    for char in s:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я' or char == 'ё' or char == 'Ё':
            count += 1
    return count


def is_lowercase_latin_palindrome(s):
    lowercase_latin = []
    for char in s:
        if 'a' <= char <= 'z':
            lowercase_latin.append(char)
    
        return lowercase_latin == lowercase_latin[::-1]


def find_dates(text):
    pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    
    dates = re.findall(pattern, text)
    return dates
