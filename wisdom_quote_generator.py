import requests
from bs4 import BeautifulSoup
import random

file = requests.get('https://www.brainyquote.com/topics/wisdom-quotes').text
soup = BeautifulSoup(file, 'html.parser')
prettified = soup.prettify()

selector = soup.select("[style*='display: flex']")
list_of_quotes = []

# Get all quotes, turn to list and append to new list.
for quotes in selector:
    quotes = list(quotes)
    all_quotes = quotes[0]
    list_of_quotes.append(all_quotes)


new_quotes = []
# Stripping the /n in quotes
for els in list_of_quotes:
    new_quotes.append(els.strip())

list_of_authors = []
# Finding all the authors and appending to new list.
for author in soup.find_all(title='view author'):
    authors = author.text   # .text otherwise it will not show only the author.
    list_of_authors.append(authors)

# Pairing author list and quote list together.
quote_combos = dict(zip(list_of_authors, new_quotes))

prompt = '>'
print('Welcome to the hub of wisdom quotes. To fetch a random quote, type in "quote".')
user_input = input(prompt + ' ')

while user_input == 'quote':
    entry_list = list(quote_combos.items())
    random_entry = random.choice(entry_list)
    print('\n\n', '--------------------------------------------------------------------------'
                  '-----------------------------------------------------------------')
    print('\t*\t', random_entry[1])
    print('--------------------------------------------------------------------------'
          '-----------------------------------------------------------------')
    print('\n' + '-', random_entry[0])
    print('\n\n')

    while True:
        run_again = input('Run again? (y/n): ')
    
        if (run_again == 'y') or (run_again == 'n'):
            break
        print('Type "y" if you want to fetch another quote'
              'or type "n" if you would like to exit the program.')

    if run_again == 'y':
        continue
    else:
        print('Goodbye!')
        break


