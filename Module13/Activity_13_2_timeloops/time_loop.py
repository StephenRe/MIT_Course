import time
from threading import Timer


titles = ['Harry Potter', 'Pride and Prejudice']
pages = [250, 430]
first_name = ['J.K.', 'Jane']
last_name = ['Rowling', 'Austen']
location = ['UK', 'UK']

def build_book_dict(titles, pages, first_name, last_name, location):
    #define inputs
    inputs = zip(titles, pages, first_name, last_name, location)
    #define empty dictionary below
    d = {}
    #for loop
    for title, page, first, last, location in inputs:
        d[title] = {
            'Pages': page,
            'Author': {'First': first, 'Last': last},
            'Publisher': {'Location': location}
        }
    time.sleep(3)
    return d

print(build_book_dict(titles, pages, first_name, last_name, location))

timer = Timer(5, build_book_dict, args=(titles, pages, first_name, last_name, location))
timer.start()
time.sleep(3)
timer.cancel()
print('Timer Cancelled')

