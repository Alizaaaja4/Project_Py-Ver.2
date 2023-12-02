import os
import csv
import webbrowser

def print_header():
    print("=================================== RegisHub ===================================")
    print("                     ___                                     ")
    print("                    / _ \\__ _ _ __   __ _  __ _  ___ _ __    ")
    print("                   / /_\\/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|   ")
    print("                  / /_\\\\ (_| | | | | (_| | (_| |  __/ |      ")
    print("                  \\____/\\__,_|_| |_|\\__,_|\\__, |\\___|_|      ")
    print("                                                             ")
    print("====================== Developer by Aliza Nurfitrian [ALL] ======================")

def Sign_Up():
    print_header()
    
    print("\n")
    print("------------------------------------------------------------------------------------")
    name = input("=== Full Name     : ")
    nis = input("=== NIS           : ")
    school = input("=== School        : ")
    email = input ("=== Email         : ")
    print("------------------------------------------------------------------------------------")
    username = input("=== Username      : ")
    password = input("=== Password      : ")
    print("------------------------------------------------------------------------------------\n")
    
    databaseAccount = []
    
    with open("Database Students.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=',')
        
        for row in csv_reader:
            databaseAccount.append({'name' : row[0], 'nis' : row[1], 'school' : row[2], 'email' : row[3], 'username' : row[4], 'password' : row[5]})
            
    username_ada = False
    
    for account in databaseAccount :
        if username == account['username'] :
            print("username already used, please create a new one !!")
            username_ada = True
            break
        
    if username_ada == False :
        newdata = {'name' : name, 'nis' : nis, 'school' : school, 'email' : email, 'username' : username, 'password' : password}  
        with open('Database Students.csv', 'a',  newline='') as file:
            writer = csv.DictWriter(file, fieldnames=newdata.keys())
            writer.writerow(newdata)
            
    print('  >Registration Successful<  ')
    
    os.system('pause')
    os.system('cls')
    menu_utama()
    
def Sign_in():
    print_header()

    print("\n")
    print("------------------------------------------------------------------------------------")
    username_input = input("=== Username      : ")
    password_input = input("=== Password      : ")
    print("------------------------------------------------------------------------------------\n")

    databaseAccount = []
    with open("Database Students.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            databaseAccount.append({'username' : row[4], 'password' : row[5]})
            
    
    datalogin = []
    for i in databaseAccount:
        if username_input == i['username'] and password_input == i['password']:
            datalogin.append(i)
            
            print("\nSuccessful login !!")
            
            os.system('pause')
            os.system('cls')
            dasboard_program()
            break
    
    if len(datalogin) == 0:
        print("Account could not be found")   
        
    os.system('pause')
    os.system('cls')
    menu_utama()
    
def information():
    print_header()
    
    print("\n")
    print("------------------------------------------------------------------------------------")
    print('--                                                                                --')
    print('-- RegisHub is a smart app specifically designed to help prospective students     --')
    print('-- gauge and calculate their chances of being accepted into the official school   --')
    print('-- of choice. With RegisHub, users can enter their profile information, including --')
    print('-- academic achievements, extracurricular experience, and recommendations, then   --')
    print('-- the app will useintelligent algorithms to analyze and assess their acceptance  --')
    print('-- potential.                                                                     --')
    print('--                                                                                --')
    print("------------------------------------------------------------------------------------")
    
    os.system('pause')
    os.system('cls')
        
    menu_utama()
        
def menu_utama():
    print_header()
    
    print("------------------------------------")
    print("=====    [1]. Sign Up         =====")
    print("=====    [2]. Sign In         =====")
    print("=====    [3]. Information     =====")
    print("------------------------------------")
    
    pilihan = input("Input option (1/2/3) :  ")
    print("\n")
    
    if pilihan == '1':
        os.system('cls')
        Sign_Up()
        
    elif pilihan == '2':
        os.system('cls')
        Sign_in()
        
    elif pilihan == '3':
        os.system('cls')
        information()
        
    else :
        print("Your selection is not in the menu !!")
        os.system('cls')
        
        menu_utama()

def view_profile():
    print_header()
    username_input = input("Enter your username: ")

    with open("Database Students.csv", "r") as file:
        csv_reader = csv.reader(file)
        found = False

        for row in csv_reader:
            if row[4] == username_input:  
                found = True
                print("----------------------------------------------------------------------------------")
                print(f"== Name     : {row[0]}{' ' * (29 - len(row[0]))}| Email    : {row[3]}{' ' * (30 - len(row[3]))}")
                print("----------------------------------------------------------------------------------")
                print(f"== School   : {row[2]}{' ' * (73 - len(row[2]))}")
                print("----------------------------------------------------------------------------------")
                print(f"== Username : {row[4]}{' ' * (29 - len(row[4]))}| Password : {row[5]}{' ' * (30 - len(row[5]))}")
                print("----------------------------------------------------------------------------------")
                
                os.system('pause')
                os.system('cls')
                dasboard_program()
                break

        if not found:
            print("Account not found.")
            
    os.system('pause')
    os.system('cls')
    dasboard_program()

def search_academy():
    print_header()
    
    print("----------------------------------------------------------------------------------")
    print("==  [1]. Institute of Internal Governmen   [2]. State Financial Polytechnic     ==")
    print("==  [3]. Police Academy                    [4]. Air Force Academy               ==")
    print("==  [5]. Naval Academy                     [6]. Army Academy                    ==")
    print("----------------------------------------------------------------------------------")
    print("==  [0]. Back                                                                   ==")
    print("----------------------------------------------------------------------------------")
    pilihan = input("Input Option : ")
    print('\n')
    
    if pilihan == '1':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://jakarta.ipdn.ac.id/')
        
        search_academy()
        
    elif pilihan == '2':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://pknstan.ac.id/')
        
        search_academy()
        
    elif pilihan == '3':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://akpol.ac.id/')
        
        search_academy()
        
    elif pilihan == '4':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://aau.ac.id/')
        
        search_academy()
    
    elif pilihan == '5':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://www.aal.ac.id/')

        search_academy()
    
    elif pilihan =='6':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://www.akmil.ac.id/')
        
        search_academy()

    elif pilihan == '0':
        os.system('cls')
        dasboard_program()
    
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        search_academy()
    
def find_opprtunities():
    print_header()
    
    print("\n")
    print("------------------------------------------------------------------------------------")
    print("--                                ANNOUNCEMENT                                    --")
    print("------------------------------------------------------------------------------------")
    print("-- (1). Please choose the official academy you want to see the entrance opportunities")
    print('-- (2). Input the requested data as well as possible')
    print("-- (3). Wait for the calculation result for a few seconds")
    print("------------------------------------------------------------------------------------")
    print("==                [0]. Back             |                [9]. Next                ==")
    print("------------------------------------------------------------------------------------")
    pilihan = input("Type (Back or Next) : ")
    print("\n")
    
    if pilihan.lower() == 'Back' or pilihan.lower() == 'back':
        os.system('cls')
        dasboard_program()
    
    elif pilihan.lower() == 'Next' or pilihan.lower() == 'next':
        os.system('cls')
        lest_opportunities()
        
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        find_opprtunities()

def dasboard_program():
    print_header()
    
    print("\n")
    print("----------------------------------------------------------------------------------")
    print('--       [A].   View Profile         [B].    Search for academies on the site   --')
    print('--                                                                              --')
    print('--       [C].   Find opportunities   [D].    Exit the site                      --')
    print("----------------------------------------------------------------------------------")
    pilihan = input("Input option (A/B/C/D) : ")
    print("\n")
    
    if pilihan == 'A' or pilihan == 'a':
        os.system('cls')
        view_profile()
        
    elif pilihan == 'B' or pilihan == 'b':
        os.system('cls')
        search_academy()
        
    elif pilihan == 'C' or pilian =='c':
        os.system('cls')
        find_opprtunities()
    
    elif pilihan == 'D' or pilihan =='d':
        os.system('cls')
        menu_utama()
    
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        
        dasboard_program()

def calculate_ipdn():
    print('progres')

def calculate_stan():
    print('progres')
    
def calculate_akpol():
    print('progres')

def calculate_aau():
    print('progres')

def calculate_aal():
    print('progres')

def calculate_aad():
    print('progres')

def lest_opportunities():
    print_header()
    
    print("----------------------------------------------------------------------------------")
    print("==  [1]. Institute of Internal Governmen   [2]. State Financial Polytechnic     ==")
    print("==  [3]. Police Academy                    [4]. Air Force Academy               ==")
    print("==  [5]. Naval Academy                     [6]. Army Academy                    ==")
    print("----------------------------------------------------------------------------------")
    print("==  [0]. Back                                                                   ==")
    print("----------------------------------------------------------------------------------")
    pilihan = input("Input Option : ")
    print('\n')
    
    if pilihan == '1':
        os.system('cls')
        calculate_ipdn()
        
    elif pilihan == '2':
        os.system('cls')
        calculate_stan()
        
    elif pilihan == '3':
        os.system('cls')
        calculate_akpol()
    
    elif pilihan == '4':
        os.system('cls')
        calculate_aau()
    
    elif pilihan == '5':
        os.system('cls')
        calculate_aal()
    
    elif pilihan == '6':
        os.system('cls')
        calculate_aad()
        
    elif pilihan == '0':
        os.system('cls')
        find_opprtunities()
    
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        lest_opportunities()

## all function
menu_utama()
