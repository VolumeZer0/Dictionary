# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def add_word(wordlist):
    added_word = ""
    added_word = input("Type the word you want to add: ")
    added_word = added_word.lower()
    if(added_word in wordlist):
        print('This word is already in the list. ')
        return wordlist
    else:
        wordlist.append(added_word)
        print(added_word + " has been added to the dictionary. ")
        wordlist.sort()
        print(wordlist)
    return wordlist


def remove_word(wordlist):
    removed_word = ""
    removed_word = input("Type the word you want to removed: ")
    removed_word = removed_word.lower()
    if(removed_word in wordlist):
        wordlist.remove(removed_word)
        print(removed_word + " has been removed from the dictionary")
        print(wordlist)
    else:
        print("That word does not exist in the dictionary")
    return


def txt_to_list():
    file = open("word_list.txt", "r+")
    txt = file.read()
    words = txt.split("\n")
    return words


def list_to_txt(l):
    file = open("word_list.txt", "wb")
    x = ""
    for word in l:
        x += word + "\n"
    file.write(bytes(x, 'UTF-8'))
    file.close()
    return


def main():
    w = txt_to_list()
    print("Here is the current dictionary!")
    print(w)
    user_edit_choice = str(input("Would you like to edit this dictionary? (Y/N) ").lower())
    if user_edit_choice == 'y' or user_edit_choice == 'yes':
        user_edit_choice = int(input("Would you like to add or remove a word? (1/2) "))
        if user_edit_choice == 1:
            w = add_word(w)
            list_to_txt(w)

        elif user_edit_choice == 2:
            remove_word(w)
            list_to_txt(w)
        else:
            print("that is not a choice")
    elif user_edit_choice == 'n' or user_edit_choice == 'no':
        user_edit_choice = input("Would you like to search for a word? (Y/N) ").lower()
        if user_edit_choice == 'y' or user_edit_choice == 'yes':
            print("searching...")
        elif user_edit_choice == 'n' or user_edit_choice == 'no':
            print("Goodbye.")
        else:
            print('That is not an option. ')
    else:
        print("That isn't an option. ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    replay = ""
    game = "on"
    main()
    while game == "on":
        replay = input("Do you want play again? (Y/N) ").lower()
        if replay == "yes" or replay == "y":
            main()
            continue
        elif replay == "no" or replay == "n":
            print("Okay, Goodbye.")
            game = "off"
            break
        else:
            print("That was not an option. ")
            continue

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
