secret_number = int(input("Enter a secret number from 0 to 100: "))

if secret_number < 0 or secret_number > 100:
    print("Please enter a valid number from 0 to 100.")
else:
    lower_limit = 0
    upper_limit = 100
    guess_count = 0

    while True:
        computer_guess = (lower_limit + upper_limit) // 2
        print("Computer's guess:", computer_guess)

        user_response = input("Is the guess correct? (more/less/yes): ")

        if user_response == "more":
            lower_limit = computer_guess + 1
        elif user_response == "less":
            upper_limit = computer_guess - 1
        elif user_response == "yes":
            if computer_guess == secret_number:
                guess_count += 1
                print("Computer guessed the correct number:", secret_number)
                print("Guessed in", guess_count, "steps.")
            else:
                print("User is not honest.")
            break
        else:
            print("Invalid response. Please enter 'more', 'less', or 'yes'.")

        guess_count += 1
