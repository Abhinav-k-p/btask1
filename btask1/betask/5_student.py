score_input = input("Enter the student's score: ")


if score_input.isdigit():
    score = int(score_input)

    if 90 <= score <= 100:
        print("A+")
    elif 80 <= score < 90:
        print("A")
    elif 70 <= score < 80:
        print("B+")
    elif 60 <= score < 70:
        print("B")
    elif 50 <= score < 60:
        print("C")
    elif 0 <= score < 50:
        print("Failed")
    else:
        print("Invalid")
else:
    print("Invalid: Enter a valid integer score.")