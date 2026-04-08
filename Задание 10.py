def read_strings_and_sort_by_word_count():
    strings = []
    
    n = int(input("Введите количество строк: "))
    
    for i in range(n):
        s = input(f"Введите строку {i+1}: ")
        strings.append(s)
    
    def count_words(text):
        return len(text.split())
    
    strings.sort(key=count_words)
    
    print("\nСтроки, упорядоченные по количеству слов:")
    for s in strings:
        print(f"'{s}' (слов: {count_words(s)})")
    
    return strings

read_strings_and_sort_by_word_count()
