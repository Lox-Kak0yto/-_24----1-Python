import re

def find_dates_in_text(text):
    months = {
        "января": 1, "февраля": 2, "марта": 3, "апреля": 4,
        "мая": 5, "июня": 6, "июля": 7, "августа": 8,
        "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12
        }
    
    pattern = r"(\d{1,2})\s+([а-я]+)\s+(\d{4})"
    
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    valid_dates = []
    
    for day, month_name, year in matches:
        day = int(day)
        year = int(year)
        month_name = month_name.lower()
        
        if month_name in months:
            month = months[month_name]
            
            if is_valid_date(day, month, year):
                valid_dates.append(f"{day} {month_name} {year}")
    
    return valid_dates
def is_valid_date(day, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    return False
