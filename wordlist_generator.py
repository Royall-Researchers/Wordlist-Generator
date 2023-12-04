# Royall-Researchers

print("Wordlist-Generator By")
print( '''  
 ____                   _ _ 
|  _ \ ___  _   _  __ _| | |
| |_) / _ \| | | |/ _` | | |
|  _ < (_) | |_| | (_| | | |
|_| \_\___/ \__, |\__,_|_|_|
            |___/           
 ____                               _                   
|  _ \ ___  ___  ___  __ _ _ __ ___| |__   ___ _ __ ___ 
| |_) / _ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__/ __|
|  _ <  __/\__ \  __/ (_| | | | (__| | | |  __/ |  \__ \ 
|_| \_\___||___/\___|\__,_|_|  \___|_| |_|\___|_|  |___/
 
''')


print('''	[+]This Tool is Created by Royall Researchers 
	[+]This Tool is only for Educational Purpose 
        [+]no support for illegal or Un Ethical Activities 
        [+]You can Learn More From me 
        [+]Follow More InstaGram : https://instagram.com/royallresearchers 
        [+]Blog : https://royallresearchers.blogspot.com 
        [+]Medium : https://medium.com/@royallresearchers 
        [+]Quora : https://royallresearchers.quora.com 
''')
import itertools

def generate_wordlist(characters, min_length, max_length):
    wordlist = []

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            wordlist.append(''.join(combination))

    return wordlist

if __name__ == "__main__":
    characters = input("What are The Characters you need: ")  # Add more characters as needed
    min_length = int(input("Enter the minimum length of words: "))
    max_length = int(input("Enter the maximum length of words: "))

    wordlist = generate_wordlist(characters, min_length, max_length)

    with open("wordlist.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")

    print("Wordlist generated and saved to wordlist.txt.")
    print(f"Number of words generated: {len(wordlist)}")

    # Print each word on a new line
    for word in wordlist:
        print(word)
        
print("                     Thank you                       ")

