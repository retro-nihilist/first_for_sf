input_string = 'Hello! My name is Python. I will help you to analyze some data.'
## count_words = 13

#input_string = 'There are many great articles about Artificial Intelligence and its benefits for business and society. However, many of these articles are too technical for the average reader.'
## count_words = 27


input_string.replace('!', "")
input_string.replace('?', "")
input_string.replace('.', "")
input_string.replace(',', "")


count_words = len(input_string.split())
print(count_words)