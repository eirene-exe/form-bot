import requests
import os

os.system('cls||clear')
os.system('title Eirene Form-Bot')

url = input('Enter your post url: ')
entry_number = input("Entry Number: ")
option = input('Full name of your question: ')
number = int(input('Repeat count: '))
counter = 1

payload = {
    f"entry.{entry_number}": f"{option}"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}


while True:
    requests.post(url, data=payload, headers=headers)
    print(f'Succesfly voted [{counter}]')
    counter += 1
    if counter > number:
        break