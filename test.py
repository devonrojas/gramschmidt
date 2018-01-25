import inquirer

questions = [
    inquirer.List('type',
                    message="What form is your basis in?",
                    choices=['Vectors', 'Polynomials'],
                    ),
]

answers = inquirer.prompt(questions)

for key in answers:
    choice = answers[key]
    if choice is 'Vectors':
        print "You selected Vectors"
    else:
        print "You didn't select Vectors"
