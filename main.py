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
        print (added_word.upper() + " has been added to the dictionary. ")
    return added_word.sort()



def remove_word():
    removed_word = ""
    removed_word = input("Type the word you want to removed: ")
    print (removed_word.upper() + " has been removed from the dictionary")



def txt_to_list():
    file = open("word_list.txt", "r+")
    txt = file.read()
    words = txt.split("\n")
    return words


def list_to_txt():
    print("text")


def main():
    w = txt_to_list()
    print(w)
    user_edit_choice = str(input("Would you like to edit this dictionary? (Y/N) ").lower())
    if user_edit_choice == 'y' or user_edit_choice == 'yes':
        user_edit_choice = int(input("Would you like to add or remove a word? (1/2) "))
        if user_edit_choice == 1:
            w = add_word(w)
        elif user_edit_choice == 2:
            remove_word()
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
    print("Here is the current dictionary!")
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
