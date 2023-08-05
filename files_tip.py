
'''
r = open('test.txt', 'r')
file_contents = r.read()
r.close()
'''
# the above code can be written usping a context manager like so:
with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
