import random 
import string
import openpyxl

def regAccount():
    count = 0
    stringg = ''
    acct_data = []

    print("Registration: ")
    
    # acct no generator
    # https://pypi.org/project/random-username/
    stringg = stringg + str(count)
    randomNumber = random. randrange(1000,9999) 
    print(randomNumber)
    stringg = stringg + str(randomNumber)
    letters = string.ascii_uppercase
    rand_letters = random.choices(letters, k = 5) # where k is the number of required rand_letters
    for i in rand_letters:
        stringg = stringg + i
    print("Account no: ", stringg)
    acct_data.append(stringg)

    name = input("Enter your name: ")
    acct_data.append(name)
    gender = input("[m] Male    [f] Female")
    acct_data.append(gender)
    age = int(input("Enter your age: "))
    acct_data.append(age)
    bday = input("Enter your birthday: [mm/dd/yyyy]")
    acct_data.append(bday)
    telno = input("Enter your phone number: ")
    acct_data.append(telno)

    # user name generator
    username = input("Enter your username: ")
    acct_data.append(username)

    # acct_data = ['04588IIIUD', 'missy sumatra', 'f', 20, '12/12/12', '09123456789', 'user1234']
    print(acct_data)
    
    wb = openpyxl.load_workbook("nag-iisa-lang-to.xlsx")
    ws = wb.active
    ws.append(acct_data)
    wb.save("nag-iisa-lang-to.xlsx")



regAccount()