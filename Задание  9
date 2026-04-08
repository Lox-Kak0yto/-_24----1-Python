def read_strings_and_sort():
    strings = []
    
    n = int(input("Введите количество строк: "))
    
    for i in range(n):
        s = input(f"Введите строку {i+1}: ")
        strings.append(s)
    
    strings.sort(key=len)
    
    print("\nСтроки, упорядоченные по длине:")
    for s in strings:
        print(f"'{s}' (длина: {len(s)})")
    
    return strings

read_strings_and_sort()
