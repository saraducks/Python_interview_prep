import parser

class ParserError(Exception):
    parser.ParserError

class Sentence(object):
    def __init__(self, subject, verb, object):
        self.subject = subject
        self.verb = verb
        self.object = object

    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word
        else:
            return None

    def match(self, word_list, match_param):
        if word_list:
            word = word_list.pop()

            if word[0] == match_param:
                return word
            else:
                return None

    def skip(self, word_list, type):
        if word_list[0] == "stop":
            return

    def parse_subject(self, word_list):
        temp = self.peek(word_list)
        if temp == 'noun':
            self.match(word_list, 'noun')
        elif temp == 'verb':
            self.match(word_list, 'verb')
        else:
            raise ParserError("Inavlid")

    def parse_verb(self, word_list):
        temp = self.peek(word_list)
        if temp == 'verb':
            self.match(word_list, 'verb')
        else:
            raise ParserError("inavlid verb")

    def parse_object(self, word_list):
        temp = self.peek(word_list)
        if temp == 'object':
            self.match(word_list, 'object')
        else:
            raise ParserError("Invalid sentence_object")

    def parse_sentence(self, word_list):
        sub = self.parse_subject(word_list)
        ver = self.parse_verb(word_list)
        sentence_obj = self.parse_object(word_list)

s = Sentence()
my_list = [('verb','sleeping'),('noun','viniya'),('verb','practising'),('object','table'),('verb','sit')]
s.parse_sentence(my_list)


