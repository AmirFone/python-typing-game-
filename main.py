import random

def gen_index(word_list): #this function is used to generate a random index from the word list
    size = len(word_list)
    used = set()
    curr = random.randint(0, size - 1)
    while curr in used or len(word_list[curr]) > 5:
        curr = random.randint(0, size - 1)
    used.add(curr)
    return curr
def core_engine(): #this function is used to run the core engine of the game
    word_list = creating_word_list()
    word_count = 0
    while True:
        index = gen_index(word_list)
        count = 1
        word = word_list[index]
        while count < 11:
            curr = input(
                F'\033[1;37m{count:<4} Enter the word \033[1;32m{word:>4}\033[1;37m :').strip()
            if curr == word:
                count += 1
            elif curr == 'exit':
                return
            elif curr == 'skip':
                break
            else:
                print('\033[1;31m wrong \033[1;37m')
        else:
            word_count += 1
            print(F'You have completed {word_count} words')


def creating_word_list(): #this function is used to create a word list from the words.txt file
    words = open("words.txt", "r")
    word_list = [word.replace("\n", "") for word in words]
    words.close()
    return word_list


def main():
    core_engine()
    return print("Thanks for playing!")


if __name__ == "__main__":
    main()
