import random   # For number generation
import re       # For regular expression functionality
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()


# Ievadteksts.
print("Welcome to Hangman!")
print("There are multiple difficulty settings shown below:")
print("\t1. Beginner (10 lives)")
print("\t2. Intermediate (8 lives)")
print("\t3. Expert (6 lives)")
print("\t4. Advanced (4 lives)")
print("\t5. Insane (2 lives)")

# Izvēlas grūtības līmeni
user_setting = input("Please choose a difficulty by typing its number: ")

# Programma nolasa .txt failu, kurā ierakstīti minamie vārdi
with open("words_database.txt", encoding="UTF8") as f:
    word_list= f.read().split()

# Izdrukā konsolē, kādu grūtības pakāpi spēlētājs ir izvēlējies
if (str(user_setting) == "1"):
    number_of_lives = 10
    print("\nYou have chosen %s and will receive %d lives." % ("Beginner", number_of_lives))
    logging.info("Player has chosen "+str(number_of_lives)+" lives")
elif (str(user_setting) == "2"):
    number_of_lives = 8
    print("\nYou have chosen %s and will receive %d lives." % ("Intermediate", number_of_lives))
    logging.info("Player has chosen "+str(number_of_lives)+" lives")
elif (str(user_setting) == "3"):
    number_of_lives = 6
    print("\nYou have chosen %s and will receive %d lives." % ("Expert", number_of_lives))
    logging.info("Player has chosen "+str(number_of_lives)+" lives")
elif (str(user_setting) == "4"):
    number_of_lives = 4
    print("\nYou have chosen %s and will receive %d lives." % ("Advanced", number_of_lives))
    logging.info("Player has chosen "+str(number_of_lives)+" lives")
elif (str(user_setting) == "5"):
    number_of_lives = 2
    print("\nYou have chosen %s and will receive %d lives." % ("Insane", number_of_lives))
    logging.info("Player has chosen "+str(number_of_lives)+" lives")
else:
    number_of_lives = 10
    print("\nYou have made an invalid selection and will receive %d lives by default." % number_of_lives)
    logging.info("Player did make a valid input, therefore "+str(number_of_lives)+" lives was chosen by default")

# Izvēlas random vārdu no .txt faila
random_num = random.randint(0, len(word_list)-1)
word_chosen = word_list[random_num]
logging.info("Random word has been chosen, it is "+str(word_chosen))

# Vārdu aizstāj ar svītrām
encoded_word = re.sub('[0-9a-zA-Z]', '-', word_chosen)
logging.info("Word has been encoded with lines")

# Vārdu minēšanas funkcija
def guess(letter, word, encoded):
    # Pārbauda vai burts ir vārdā, kuru jāuzmin
    found = False
    if letter in word:
        found = True
        # Svītru samaina ar burtu
        for i in range(0, len(word)):
            if word[i] == letter:
                encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
                logging.info("The guessed letter has been decoded")
    return (found, encoded)


# Sākas spēle un var minēt vārdu/burtu
print("\nTime to guess a letter! You have %d lives remaining." % number_of_lives)
print(encoded_word)

while(number_of_lives > 0):
    guessed_letter = input("Your guess: ")[:1]

    letter_found, encoded_word = guess(guessed_letter, word_chosen, encoded_word)

    if not letter_found:
        number_of_lives -= 1
        if number_of_lives == 0:
            print("\nGame over, you lost! :( The word or phrase was '%s'" % word_chosen)
            logging.info("The game has ended. Player did not guess the word and lost.")
            #Te var uz datu bāzi, ka ___ spēlētājs neuzminēja ____ vārdu ar __ grūtības pakāpi
            break
        else:
            print("\nWhoops! That letter was not found. You now have %d lives remaining." % number_of_lives)
            print(encoded_word)
            logging.info("Wrong letter guessed," +str(number_of_lives)+ " lives remaining")
    else:
        if "-" not in encoded_word:
            print("\nHooray! You won with %d lives remaining. The word or phrase was '%s'" % (number_of_lives, word_chosen))
            logging.info("Game has ended. Player guessed '"+ str(word_chosen) +"' with "+str(number_of_lives)+" lives left.")
            #Te var uz datu bāzi, ka ___ spēlētājs uzminēja ____ vārdu ar ___ grūtības pakāpi un palika _ dzīvības
            break
        else:
            print("\nGood job! That letter was found. You still have %d lives remaining." % number_of_lives)
            logging.info("Right letter guessed," +str(number_of_lives)+ " lives remaining")
            print(encoded_word)