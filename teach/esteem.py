def main():

    def ask_positive_question(statement):
        print(statement)

        answer = input("    Enter D, d, a, or A: ")

        score = 0

        if answer == "D":
            score = 0
        elif answer == "d":
            score = 1
        elif answer == "a":
            score = 2
        elif answer == "A":
            score = 3
        else:
            print("Error. Invalid input.")

        return score

    def ask_negative_question(statement):
        print(statement)

        answer = input("    Enter D, d, a, or A: ")

        score = 0

        if answer == "D":
            score = 3
        elif answer == "d":
            score = 2
        elif answer == "a":
            score = 1
        elif answer == "A":
            score = 0
        else:
            print("Error. Invalid input.")

        return score

    print("\nThis program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")

    print("\nD means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")

    score = 0

    score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an equal plane with others."
    )
    score += ask_positive_question("2. I feel that I have a number of good qualities.")
    score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure."
    )
    score += ask_positive_question(
        "4. I am able to do things as well as most other people."
    )
    score += ask_negative_question("5. I feel I do not have much to be proud of.")
    score += ask_positive_question("6. I take a positive attitude toward myself.")
    score += ask_positive_question("7. On the whole, I am satisfied with myself.")
    score += ask_negative_question("8. I wish I could have more respect for myself.")
    score += ask_negative_question("9. I certainly feel useless at times.")
    score += ask_negative_question("10. At times I think I am no good at all.")

    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.\n")


if __name__ == "__main__":
    main()
