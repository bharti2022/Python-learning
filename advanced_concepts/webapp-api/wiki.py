import wikipedia

print(wikipedia.search('Python (programming language)'))

page = wikipedia.page('Python (programming language)')


print(page.url)

#['Python', 'Python (programming language)', 
#'Monty Python', 'Burmese python', 
#'Python molurus', 'Python (missile)',
#'Ball python', 'Python curtus', 
#'African rock python', 'History of Python']

print(wikipedia.summary('Python (programming language)'))
