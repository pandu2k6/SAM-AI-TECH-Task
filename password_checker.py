import string


def check_password_strength(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must contain at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, feedback


def main():

    print("\n========================================")
    print("       PASSWORD STRENGTH CHECKER")
    print("========================================")

    password = input("\nEnter your password: ")

    strength, score, feedback = check_password_strength(password)

    print("\n========== PASSWORD ANALYSIS ==========")

    print("Password Length :", len(password))
    print("Security Score  :", str(score) + "/5")
    print("Password Status :", strength)

    if feedback:
        print("\nSuggestions to improve your password:")

        for suggestion in feedback:
            print("- " + suggestion)

    else:
        print("\nExcellent! Your password meets all requirements.")

    print("=======================================")

if __name__ == "__main__":
    main()
