students_scores = [180, 124, 165, 173, 189, 169, 146]
maximum = students_scores[0]
for score in students_scores:
    if score > maximum:
        maximum = score
print(maximum)
