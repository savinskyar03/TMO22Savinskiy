# фунция
def students_per_item(students, teams):
    if teams == 0:
        return "На ноль делить нельзя"
    return students / teams

# проверка
assert students_per_item(24, 4) == 6.0
assert students_per_item(18, 0) == "На ноль делить нельзя"
assert students_per_item(55, 5) == 11.0


# cортировка черещз Lambda
words = ["день", "экзамен", "каникулы"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)