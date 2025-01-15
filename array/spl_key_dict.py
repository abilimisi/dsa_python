def finding_spl_keys(chr):
    vowels = "aeiouAEIOU"
    special_keys = "!@#$%^&*()-+=<>?/\\|{}[]~`\"';:,._"
    d = {'vowels': 0, 'special_keys': 0, 'nums': 0, 'non_vowels': 0, 'spaces': 0}

    for i in chr:
        if i in vowels:
            d['vowels'] += 1
        elif i.isdigit():
            d['nums'] += 1
        elif i in special_keys:
            d['special_keys'] += 1
        elif i.isalpha() and i not in vowels:
            d['non_vowels'] += 1
        elif i.isspace():
            d['spaces'] += 1
    return d

chr = input("Enter the line: ")
res = finding_spl_keys(chr)
print(res)
