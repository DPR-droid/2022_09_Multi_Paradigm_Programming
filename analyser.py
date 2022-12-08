import re

"""
in designing this solution my thought was that there are no 'is-a' relationships 
which would indicate inheritance relationships explicitly. As such I structured
the solution with an object composition wherein content has-many paragraphs, a paragraph 
has many sentences etc.

The calculations of the statistics is dependant on the constituent classes, for example
content relies on each paragraph to answer for it's own length. This is not efficient but
is intended to show the principle of 'separation of concerns' or 'division of labour' that
is espoused in the OOP paradigm
"""

class Content:
    
    def __init__(self, content):
        self.content = content
        self.__create_paragraphs()

    """
    This is a private method of the Content class, 
    it is used to create paragraph instances for each
    paragraph found in the text content
    """
    def __create_paragraphs(self):
        # content has-many paragraphs
        self.paragraphs = []
        # the content is split where we find 
        # two side by side new line characters
        for i in content.split('\n\n'):
            # create a new paragraph instance
            temp = Paragraph(i)
            # add it to the list of paragraphs
            self.paragraphs.append(temp)
    
    """
    This method tells us the number of characters 
    in the complete text content. This is calculated 
    from the lengths of the individual paragraphs.
    As such we do not account for the now removed characters
    such as the '\n\n', minor changes would allow this.
    This is intended as an example of object composition.
    """
    def num_chars(self):
        sum = 0;
        for par in self.paragraphs:
            sum += par.num_chars()
        return sum 
        
    def num_words(self):
        sum = 0
        for para in self.paragraphs:
            sum += para.num_words()
        return sum
    
    def num_sentences(self):
        sum = 0
        for para in self.paragraphs:
            sum += para.num_sentences()
        return sum
    
    def num_paragraphs(self):
        return len(self.paragraphs)
        
    def average_num_sentences_in_paragraph(self):
        return self.num_sentences() / self.num_paragraphs()
           
    """
    special method which is always used to return a textual representation of an object
    Some times this is referred to as the 'to string' method.
    """
    def __str__(self):
        str = f"In this content, there are {self.num_chars()} characters ({len(self.content)} before splitting), {self.num_words()} words, {self.num_sentences()} sentences, inside {self.num_paragraphs()} paragraphs. On average there are {self.average_num_sentences_in_paragraph()} sentences in a paragraph"
        for par in self.paragraphs:
            str += f"\n{par}"
        return str
        
class Paragraph:

    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.__create_sentences()

    def __create_sentences(self):
        self.sentences = []
        temp_arr = re.split('[.!?]', self.paragraph)
        for sentence in temp_arr:
            temp = Sentence(sentence)
            self.sentences.append(temp)

    def num_chars(self):
        sum = 0;
        for sen in self.sentences:
            sum += sen.num_chars()
        return sum 
    
    def num_words(self):
        sum = 0
        for sentence in self.sentences:
            sum += sentence.num_words()
        return sum
        
    def num_sentences(self):
        return len(self.sentences)
        
    def average_num_words_in_sentence(self):
        return self.num_words() / self.num_sentences()
        
    def __str__(self):
        return f"PARAGRAPH: On average {self.average_num_words_in_sentence()} words in each sentence."
        

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.__create_words()
        
    def __create_words(self):
        temp_arr = re.split('\s', self.sentence)
        self.words = []
        for word in temp_arr:
            temp = Word(word)
            self.words.append(temp)

    def num_chars(self):
        sum = 0;
        for word in self.words:
            sum += word.num_chars()
        return sum 
    
    def num_words(self):
        return len(self.words)

class Word:
    def __init__(self, word):
        self.word = word
        self.characters = self.__create_characters()
        
    def __create_characters(self):
        lst = []
        for letter in self.word:
            lst.append(letter)
        return lst
    
    def num_chars(self):
        return len(self.characters)
 
content = """So entirely unaware was Mrs. Wilkins that her April for that year had
then and there been settled for her that she dropped the newspaper with
a gesture that was both irritated and resigned, and went over to the
window and stared drearily out at the dripping street.

Not for her were mediaeval castles, even those that are specially
described as small. Not for her the shores in April of the
Mediterranean, and the wisteria and sunshine. Such delights were only
for the rich. Yet the advertisement had been addressed to persons who
appreciate these things, so that it had been, anyhow addressed too to
her, for she certainly appreciated them; more than anybody knew; more
than she had ever told. But she was poor. 

In the whole world she possessed of her very own only ninety pounds, saved from year to year,
put by carefully pound by pound, out of her dress allowance. She had
scraped this sum together at the suggestion of her husband as a shield
and refuge against a rainy day. Her dress allowance, given her by her
father, was £100 a year, so that Mrs. Wilkins’s clothes were what her
husband, urging her to save, called modest and becoming, and her
acquaintance to each other, when they spoke of her at all, which was
seldom for she was very negligible, called a perfect sight."""


c = Content(content)
print(c)