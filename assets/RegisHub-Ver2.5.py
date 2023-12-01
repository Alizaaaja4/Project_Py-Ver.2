import os
import csv

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
    
    print("\n")
    print("----------------------------------------------------------------------------------")
    print("== Name     :                        | Email    :                               ==")
    print("----------------------------------------------------------------------------------")
    print("== School   :                                                                   ==")
    print("----------------------------------------------------------------------------------")
    print('== Username :                        | Password :                               ==')
    print("----------------------------------------------------------------------------------")
    
def search_academy():
    print("on progress")
    
def find_opprtunities():
    print("on progress")

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
    
    if pilihan == 'A' or 'a':
        os.system('cls')
        view_profile()
        
    elif pilihan == 'B' or 'b':
        os.system('cls')
        search_academy()
        
    elif pilihan == 'C' or 'c':
        os.system('cls')
        find_opprtunities()
    
    elif pilihan == 'D' or 'd':
        os.system('cls')
        menu_utama()
    
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        
        dasboard_program()

## all function
menu_utama()
