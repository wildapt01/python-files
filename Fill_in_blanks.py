
# Reverse Mad_libs game -
# Stage 2 Project in Python 2.7.10- IPND
#
# Notes: The module Random is imported to generate a
# 	new game with different words.
# 	The module String is imported to allow the striping of
# 	punctuation in the random_word function.

import random
import string

# Level selection. Starts the game based on the selected level.


def welcome():
    level_input = raw_input("""Welcome to a game of Reverse Mad-Libs \n
		Please type the desired level
		(Easy, Medium, Hard or Very hard): """
                            )
    blanks = valid_input(level_input)
    game_on(blanks)

# Verify the input string is correct and return
# a number of blanks based on level selected.


def valid_input(a):
    dict_level = {"easy": 4, "medium": 5,
                  "hard": 6, "very hard": 7
                  }
    entry = a.lower()  # Deals with upper case first letter
    blanks = 0
    if entry not in dict_level.keys():
        print "\n \n This is not a level!\n \n"
        welcome()
    else:
        blanks = dict_level.get(entry)
        return blanks

# Select the words to be blanked and their positions
# from text, populates the dictionnary word_dict,
# the position being the key.
# The number of words is based on the selected level.


def random_words(some_text, n):
    # builds the list and removes punctuation
    # And no, it is not mine but it is a cool line of code.
    text_list = [a.strip(string.punctuation)
                 for a in some_text.split()
                 ]
    word_list = []
    word_dict = {}
    i = 0
    while i < n:
        word = random.choice(text_list)
        # eliminates duplicates and builds the dictionnary.
        if word not in word_list and len(word) > 3:
            word_list.append(word)
            word_index = text_list.index(word)
            word_dict[word_index] = word
            i += 1
        else:
            pass
    return word_dict

# Takes a dictionnary some_dict and output the list
# word_list of its values sorted by its keys, ascending.


def ascend(some_dict):
    k_list = sorted(some_dict)
    word_list = []
    for k in k_list:
        word_list.append(some_dict.get(k))
    return word_list

# Creates string blankd_text from string text
# based on dificulty level and list of words to be found.


def blankd(string_text, word_list, blanks):
    blankd_text = string_text
    i = 0
    while i < blanks:
        times = int(blanks / 2)
        for a in word_list:
            num_blank = blanking(i)
            blankd_text = blankd_text.replace(
                a, num_blank, times
            )
            i += 1
    return blankd_text

# Transforms a integer in a string
# made of "__", the number then "__"


def blanking(num):
    a = "__" + str(num + 1) + "__"
    return a

# Turns an integer num in a string which is
# the text of the prompt, based on the rank of
# the word to be found.


def prompt(num):
    prompt_string = "\n What should go in number " + str(num) + "? "
    return prompt_string

# Replaces the relevant blanked word with the proper
# word in a text block.


def updated(some_text, n, some_string):
    blank = blanking(n)
    new_text = some_text.replace(blank, some_string)
    return new_text

# Acknowledges the victory and offers a new game,
# branching to the welcome function.


def you_win():
    print "\n Well done! You won."
    yes_no = raw_input("\n Would you like to play again (Yes/No)? ")
    if yes_no[0].lower() == "y":
        welcome()
    else:
        pass

# Starts the game based on the selected level. The text block
# is the local variable text. When the last word is found,
# the function you_win is called.


def game_on(blank_num):
    text = """Peanuts grow best in light, sandy loam soil with some acidity. Their capacity to fix nitrogen means that,
providing they nodulate properly, peanuts benefit little or not at all from nitrogen fertilizer, and they improve
soil fertility. Therefore, they are valuable in crop rotations. Also, the yield of the peanut crop itself is
increased in rotations, through reduced diseases, pests and weeds. Peanut plants continue to produce flowers
when pods are developing, therefore even when they are ready for harvest, some pods are immature. The timing of
harvest is an important decision to maximize yield. If it is too early, too many pods will be unripe. If too late,
the pods will snap off at the stalk, and will remain in the soil.
	"""
    word_list = ascend(random_words(text, blank_num))
    modified_text = blankd(text, word_list, blank_num)
    print "\n \n", modified_text, "\n"
    i = 1
    while i <= blank_num:
        answer = raw_input(prompt(i))
        if answer == word_list[i - 1]:
            modified_text = updated(modified_text, (i - 1), answer)
            print "\n", modified_text
            i += 1
        else:
            pass
    you_win()


welcome()
