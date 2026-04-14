def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    vowels = "aeiou"
    count = 0
    for c in text.lower():
        if c in vowels:
            count += 1
    return count


def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    vowels = "aeiou"
    count = 0
    for c in text.lower():
        if c.isalpha() and c not in vowels:
            count += 1
    return count


def total_letters(text):
    return count_vowels(text) + count_consonants(text)


def vowel_percentage(text):
    total = total_letters(text)
    
    if total == 0:
        return 0.0
    
    vowels = count_vowels(text)
    percentage = (vowels / total) * 100
    
    return round(percentage, 1)


def analyze_text(text):
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)

    percentage_str = str(percentage)

    return f"V:{vowels} C:{consonants} T:{total} P:{percentage_str}%"
