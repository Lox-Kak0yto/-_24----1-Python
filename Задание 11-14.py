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
    

def sort_by_vowel_consonant_combinations(strings):
    vowels = set('аеёиоуыэюяaeiou')
    consonants = set('бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz')
    
    def count_combinations(text):
        text_lower = text.lower()
        vc_count = 0  # гласная-согласная
        cv_count = 0  # согласная-гласная
        
        for i in range(len(text_lower) - 1):
            first = text_lower[i]
            second = text_lower[i + 1]
            
            if first in vowels and second in consonants:
                vc_count += 1
            elif first in consonants and second in vowels:
                cv_count += 1
        
        return vc_count - cv_count
    
    strings.sort(key=count_combinations)
    return strings

    
    def sort_by_mirror_triples(strings):
    def count_mirror_triples(text):
        count = 0
        for i in range(len(text) - 2):
            if text[i] == text[i + 2]:
                count += 1
        return count
    
    def average_mirror_triples(text):
        if len(text) < 3:
            return 0
        triple_count = count_mirror_triples(text)
        total_triples = len(text) - 2
        return triple_count / total_triples if total_triples > 0 else 0
    
    strings.sort(key=average_mirror_triples)
    return strings

strings = ["Привет мир", "Python", "Ааа Ббб", "Тест"]
result = sort_by_consonant_vowel_difference(strings)
print(result)

strings = ["abc", "xyz", "123", "Hello"]
result = sort_by_ascii_deviation(strings)
print(result)

strings = ["abc", "aba", "hello", "world"]
result = sort_by_vowel_consonant_combinations(strings)
print(result)

strings = ["ada", "abc", "ababa", "hello", "xaxbx"]
result = sort_by_mirror_triples(strings)
print(result)
