def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower().replace(" ", "")
    res1 = count_common_letters(combined_names, "true")
    res2 = count_common_letters(combined_names, "love")
    print(f"{res1}{res2}")

def count_common_letters(name, letters):
    return sum(name.count(letter) for letter in letters)

calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
