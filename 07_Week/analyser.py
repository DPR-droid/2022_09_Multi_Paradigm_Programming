# Metadata can be described as information describing other information
# The following is a list of such metadata: 

import re


# Create Class
class text_meta:
    # Class variables
    def __init__(self, wordcount, num_characters, ws_characters, sent, avg_words, num_para ):
        self.wordcount = wordcount
        self.num_characters = num_characters
        self.ws_characters = ws_characters
        self.sent = sent
        self.avg_words = avg_words
        self.num_para = num_para


    def __repr__(self):
        string = f'Number of words in text file: {self.wordcount}\nNumber of characters in text file: {self.num_characters}\nNumber of characters excluding spaces in text file:{self.ws_characters}\nNumber of sentences in text file: {self.sent}\nNumber of paragraphs in text file:  {self.avg_words}\nAverage number of words in a sentence: {self.num_para}'
        return string


# 1. Number of Words 
def number_of_words(data):
    wordcount = 0
    for word in data.split():
        wordcount += 1
    #print('Number of words in text file: ', wordcount)
    return wordcount

# 2. Number of characters
def number_of_characters(data):
    num_characters = len(data)
    #print('Number of characters in text file: ', num_characters)
    return num_characters

# 3. Number of characters excluding white spaces
def number_of_characters_ws(data):
    data = data.replace(" ","")
    ws_characters = len(data)
    #print('Number of characters excluding spaces in text file: ', ws_characters)
    return ws_characters

# 4. Number of sentences
def number_of_sentences(data):
    sent = [len(l.split()) for l in re.split(r'[?!.]', data) if l.strip()]
    len_sen = len(sent)
    #print('Number of sentences in text file: ', len_sen)
    return len_sen

# 5. Number of paragraphs
def number_of_paragraphs(data):
    para = [len(l.split()) for l in re.split(r'[\n\n]', data) if l.strip()]
    num_para = len(para)
    #print('Number of paragraphs in text file: ', num_para)
    return num_para

# 6. Average number of words in a sentence
def average_sentence(sent):
    sent = [len(l.split()) for l in re.split(r'[?!.]', data) if l.strip()]
    avg_words = sum(sent)/len(sent)
    #print('Average number of words in a sentence: ', avg_words)
    return avg_words


# Request users text file
#file = open("sometext.txt", "r")
filename = input("File name to read: ")

# Open for text file for reading text
file = open(filename, "r")
data = file.read()

# Functions to get meta data
part1 = number_of_words(data)
part2 = number_of_characters(data)
part3 = number_of_characters_ws(data)
part4 = number_of_sentences(data)
part5 = number_of_paragraphs(data)
part6 = average_sentence(data)

# create first object
get_meta = text_meta(part1, part2, part3,part4, part5, part6)

print("Print class")
print(get_meta)
print("\n")

# access class variable
print("Access Class variable sent : ", get_meta.sent)
print("Access Class variable avg_words : ", get_meta.avg_words)
print("Access Class variable num_characters : ", get_meta.num_characters)
print("Access Class variable num_para : ", get_meta.num_para)
print("Access Class variable wordcount : ", get_meta.wordcount)

