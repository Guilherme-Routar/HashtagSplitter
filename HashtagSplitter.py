import nltk
import re

class HashtagSplitter():
    
    '''
    HashtagSplitter class description
    '''
    
    # Initializing list of words according to input
    def __init__(self, data):
        # Checking if user inserted a language (currently only EN and PT supported)
        if type(data) is str:
            if data == 'EN':
                self.import_data_EN()
            elif data == 'PT':
                self.import_data_PT()
            else:
                raise ValueError('Invalid input. Try a valid language or dictionary.')
        # Checking if user inserted a personalized list of words
        elif type(data) is list:
            print("Dict provided")
        else:
            raise ValueError('Invalid input. Try a valid language or dictionary.')
            
    '''
    # Meant to automatize the whole data import process
    def data_builder(self, corpora, alphabet):
        # TO BE IMPLEMENTED
    '''
        
    
    # Importing data for the English language
    def import_data_EN(self):
        
        # EN text corpora
        #    - words
        #    - Brown: 15 genres, 1.15M words, tagged, categorized
        
        # Downloading corpora
        nltk.download('words', quiet=True)
        nltk.download('brown', quiet=True)
        
        # Building list of words
        self.words_list = \
            list(set(words.words())) + \
            list(set(brown.words()))
        
        # Ignoring characters that aren't words
        ignore_chars = "bcdefghjklmnopqrstuvwxyz"
        for char in ignore_chars:
            if char in self.words_list:
                self.words_list.remove(char)
    
    # Importing data for the Portuguese language
    def import_data_PT(self):
        
        # PT text corpora
        #    - Machado
        #    - MacMorpho tagged corpus: 1M words, tagged
        #    - Floresta treebank: 9k sentences, tagged and parsed
        
         # Downloading corpora
        nltk.download('machado', quiet=True)
        nltk.download('floresta', quiet=True)
        nltk.download('mac_morpho', quiet=True)
        
        # Building list of words
        self.words_list = \
            list(set(machado.words())) + \
            list(set(floresta.words())) + \
            list(set(mac_morpho.words()))
        
        # Ignoring characters that aren't words
        ignore_chars = "bcdfghijklmnpqrstuvwxyz"
        for char in ignore_chars:
            if char in self.words_list:
                self.words_list.remove(char)
    
    def split(self, hashtag):
        
        # Removing hash symbol
        string = hashtag.replace('#', '')
        
        # 3 different possibilities must be considered when decomposing an hashtag
        #   1: Hashtag is camel case (e.g. #ThisIsAHashtag)
        #   2: Hashtag words are separated by symbols (e.g. '_')
        #   3: Hashtag is all lower or upper caps
        
        # Initializing results list
        decomposed_list = []
        # Case 1 & 2: Camel case (or dromedary) and symbol
        decomposed_list.append(self.camel_case_symbol_splitter(string))
        # Case 3: All lower or upper caps
        decomposed_list.append(self.brute_force_splitter(string))
        
        return decomposed_list
        
    # Returns a list of valid decompositions based on camel and dromedary case or symbols separation
    def camel_case_symbol_splitter(string):
        return re.findall(r'[0-9]+|[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', string)
    
    # Returns a list of valid decompositions based on brute force
    def brute_force_splitter(string):
        print("brute_force_splitter")
        