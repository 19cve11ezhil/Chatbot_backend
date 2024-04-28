import random


def random_string():
    rand_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    lst_count = len(rand_list)
    rand_item = random.randrange(lst_count)

    return rand_list[rand_item]