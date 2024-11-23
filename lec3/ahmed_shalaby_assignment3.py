def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    s = s.lower()
    for letter in s:
        if letter in 'aeiou':
            vowels += 1
        elif ord(letter) in range(97, 123):
            consonants += 1

    return(vowels, consonants)

print(count_vowels_consonants("Hello World"))