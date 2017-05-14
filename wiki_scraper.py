'''

Wikipedia scraper - Jayser Mendez

'''
import os, platform, sys
import wikipedia as database
from time import sleep

from internet import * # Module to check internet connection.

# Since we have too much variables, let get them from external module.
from var import *
# Import everything since we don't have conflict between modules.

from write import * # Import typewriter-effect from external module.

class main():

    def menu(main_menu, main_menu_title, language):


        write(main_menu[0] + "\n" + main_menu[1] + "\n" +
              main_menu[2] + "\n" + main_menu[3] + "\n")

        # If user input something wrong, don't stop the program.
        while True:
            answer = input(write("\n" + main_menu_title))
        
            if answer == "1": # Open search function

                # Check for language fallback.
                if language == "english": # Fallback language English.
                    main.clear_alt()
                    query.search(query_question[0],language)
                    break
                
                elif language == "spanish": # Fallback language Spanish.
                    main.clear_alt()
                    query.search(query_question[1],language)
                    break

                elif language == "french": # Fallback language French.
                    main.clear_alt()
                    query.search(query_question[2],language)
                    break
                # Check for language fallback.

            elif answer == "2": # Open select language menu
            
                if language == "english": # Fallback language English
                    main.clear_alt()
                    main.selectLanguage(language_menu_title,
                                        languages_list,
                                        language_select,
                                        language)
                    break
                
                elif language == "spanish": # Fallback language Spanish
                    main.clear_alt()
                    main.selectLanguage(language_menu_title,
                                        languages_list,
                                        language_select,
                                        language)
                    break
                
                elif language == "french": # Fallback language French
                    main.clear_alt()
                    main.selectLanguage(language_menu_title,
                                        languages_list,
                                        language_select,
                                        language)
                    break
                
            elif answer == "3": # Close program
                if language == "english":
                    write("Goodbye! :)")
                    break

                elif language == "spanish":
                    write("Adiós! :)")
                    break

                elif language == "french":
                    write("Au Revoir! :)")
                    break

            else:
                if language == "english":
                    write(option_error[0])
                    main.clear_alt()
                    
                elif language == "spanish":
                    write(option_error[1])
                    main.clear_alt()

                elif language == "french":
                    write(option_error[2])
                    main.clear_atl()
            
    
    def selectLanguage(title, languages, select_language, language):
        
        if language == "english":
            write(title[0]
                  + "\n" + languages[0]
                  + "\n" + languages[1]
                  + "\n" + languages[2])
            
        elif language == "spanish":
            write(title[1]
                  + "\n" + languages[3]
                  + "\n" + languages[4]
                  + "\n" + languages[5])

        elif language == "french":
            write(title[2]
                  + "\n" + languages[6]
                  + "\n" + languages[7]
                  + "\n" + languages[8])
            
        while True:
            if language == "english":
                answer = input(write(select_language[0]))
                
            elif language == "spanish":
                answer = input(write(select_language[1]))

            elif language == "french":
                answer = input(write(select_language[2]))
                
            if answer == "1":
                write("\nEnglish is set!")
                database.set_lang("en")
                main.clear_alt()
                language = "english" # Set fallback language as English
                main.menu(main_menu, main_menu_title, language)
                break
            
            elif answer == "2":
                write("\nSpanish is set!")
                database.set_lang("es")
                main.clear_alt()
                spanish = main_menu_spanish
                spanish_title = mainMenu_spanish
                language = "spanish" # Set fallback language as Spanish
                main.menu(spanish, spanish_title, language)
                break
        
            elif answer == "3":
                write("\nFrench is set!")
                database.set_lang("fr")
                main.clear_alt()
                french = main_menu_french
                language = "french" # Set fallback language as French
                main.menu(french, mainMenu_french, language)
                break

            else:
                if language == "english":
                    write(option_error[0])
                    main.clear_alt()
                    
                elif language == "spanish":
                    write(option_error[1])
                    main.clear_alt()

                elif language == "french":
                    write(option_error[2])
                    main.clear_alt()
                
    def clear_alt():
        # only works when you are using console
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
            
    def clear():
        print("\n##################################################\n")
        
class query():
    
    def search(query_question, language):
        search = input(write(query_question))
        main.clear_alt()
        try:
            summary = database.summary(search, sentences=2) + "\n"
            write(summary)

            if language == "english": # Fallback language English

                # Show if and only if language is English
                question = input(write("\nWant to hear me dictating this text? 'Y' for yes, 'N' for no.\n"
                                 "Note: This is an experimental function and just work in English"
                                 "\n? "))
                while True:
                    if question.lower() in("yes","y"):
                        write("Dictation is playing, make sure to turn the speakers on!")
                        os.system("say '"+summary+"'")
                        write("\nDictation ends.\n")
                        break

                    elif question.lower() in("no","n"):
                        break

                    else:
                        write(option_error)
                    
            elif language == "spanish":
                pass # Just ignore this statement (NULL)

            elif language == "french":
                pass # Just ignore this statement (NULL)

        # Check for any possible errors.           
        except database.exceptions.DisambiguationError:
            if language == "english":
                write("Too much results for this term, please be specific!")

            elif language == "spanish":
                write("Demasiado resultados para este término, ¡por favor sea específico!")

            elif language == "french":
                write("Trop de résultats pour ce terme, soyez précis!")

        except database.exceptions.PageError:
            if language == "english":
                write("'" + search + "'" + " does not match any page, try again!\n")

            elif language == "spanish":
                write("'" + search + "'" + " no coincide con ninguna página, vuelve a intentarlo!\n")

            elif language == "french":
                write("'" + search + "'" + " no coincide con ninguna página, vuelve a intentarlo!\n")

        main.clear_alt()
        query.askUser(query_question, user_options, language)
 
    def askUser(query_question, user_options, language):
        while True:
            if language == "english":
                answer = input(write(user_options[0] + "\n" +
                                     user_options[1] + "\n" +
                                     user_options[2] + "\n" +
                                     "\n" + user_options[3] ))

            elif language == "spanish":
                answer = input(write(user_options[4] + "\n" +
                                     user_options[5] + "\n" +
                                     user_options[6] + "\n" +
                                     "\n" + user_options[7] ))

            elif language == "french":
                answer = input(write(user_options[8] + "\n" +
                                     user_options[9] + "\n" +
                                     user_options[10] + "\n" +
                                     "\n" + user_options[11] ))
 
       
            if answer == "1":
                if language == "english": # Fallback language English
                    main.clear_alt()
                    query.search(query_question, language)
                    break
                
                elif language == "spanish": # Fallback language Spanish
                    main.clear_alt()
                    query.search(spanish_q, language)
                    break

                elif language == "french": # Fallback language Spanish
                    main.clear_alt()
                    query.search(french_q, language)
                    break 

            elif answer == "2":
                if language == "english":
                    main.clear_alt()
                    main.menu(main_menu, main_menu_title, language)
                    break
                
                elif language == "spanish":
                    main.clear_alt()
                    main.menu(main_menu_spanish, mainMenu_spanish, language)
                    break

                elif language == "french":
                    main.clear_alt()
                    main.menu(main_menu_french, mainMenu_french, language)
                    break

            else:
                if language == "english": # Fallback language English
                    write(option_error[0])
                    main.clear_alt()
                    
                elif language == "spanish": # Fallback language Spanish
                    write(option_error[1])
                    main.clear_alt()

                elif language == "french": # Fallback language Spanish
                    write(option_error[2])
                    main.clear_alt()

######################################################################

# Entry point to the program
if __name__ == "__main__":

    # Don't allow the user to use the program without internet.
    while True:
        if is_connected() == True:
    
            write("Welcome to wikipedia console.\n")
            write("Here you can search for anything in three languages: English, Spanish, French.\n")
            write("Enjoy :)\n\n")
            main.menu(main_menu, main_menu_title, language)
            break

        else:
            write("\nPlease connect to the internet before loading this program")
            ask_again = input(write("\nWant to try again? Type 'y' for yes or 'n' for no: \n"))

            if ask_again.lower() in("yes","y"):
                pass

            else:
                write("Goodbye!")
                break

        

# If module was imported into another module
else:
    pass

'''

Observations: I can improve the code by giving the correct use of classes,
but I learned classes after this project.

'''
