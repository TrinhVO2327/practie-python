import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask_questions():
    answers = {}
    for key, value in questions.items():
        answer = input(value + " ")
        if answer.lower() in ["yes", "y"]:
            answers[key] = True
        else:
            answers[key] = False
    return answers

def make_drink(answers):
    drink = []
    for key, value in answers.items():
        if value:
            drink.append(random.choice(ingredients[key]))
    return drink

def main():
    print("Let's make a custom drink for ye!")
    answers = ask_questions()
    drink = make_drink(answers)
    print("Here's your drink! It contains:")
    for ingredient in drink:
        print("- " + ingredient)

if __name__ == "__main__":
    main()
