from abc import ABCMeta, abstractmethod

__all__ = ['Analyzer', 'Tokenizer', 'CharFilter', 'Filter']

class Analyzer:
    
    def __init__(self, char_filters=[], tokenizer=DefaultTokenizer(), filters=[]):
        self.char_filters = char_filters
        self.tokenizer = tokenizer
        self.filters = filters

    def process(self, text):
        pass

class Tokenizer:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def tokenize(self, text):
        pass

class DefaultTokenizer(Tokenizer):

    def tokenize(self, text):
        #TODO: implement http://unicode.org/reports/tr29/
        pass

class TwitterTokenizer(Tokenizer):

    def tokenize(self, text):
        #TODO: implement variation of DefaultTokenizer to handle #hashtags, 
        # @usernames, emoticons, etc.
        pass

class Filter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def filter(self):
        pass

class LowerFilter(Filter):

    def filter(self, token):
        return token.lower()

class CharFilter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def filter(self):
        pass
