def sort_by_consonant_vowel_difference(strings):
    def count_vowels_consonants(text):
        vowels = set('аеёиоуыэюяaeiou')
        consonants = set('бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz')
        
        text_lower = text.lower()
        vowel_count = 0
        consonant_count = 0
        
        for char in text_lower:
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        
        return consonant_count - vowel_count
    
    strings.sort(key=count_vowels_consonants)
    return strings


def sort_by_ascii_deviation(strings):
    if not strings:
        return strings
    
    def get_ascii_avg(text):
        if not text:
            return 0
        total = sum(ord(char) for char in text)
        return total / len(text)
    
    first_avg = get_ascii_avg(strings[0])
    
    def deviation(text):
        avg = get_ascii_avg(text)
        return (avg - first_avg) ** 2
    
    strings.sort(key=deviation)
    return strings
