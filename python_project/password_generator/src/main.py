
from abc import ABC, abstractmethod
import random
import string
import nltk

nltk.download('words')



class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length=5) -> None:
        self.length = length


    def generate(self) -> str:
        return ''.join(random.choice(string.digits) for _ in range(self.length))
    

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_symbols: bool = False, include_numbers: bool = False) -> None:
        self.length = length
        self.charactor = string.ascii_letters
        if include_numbers:
            self.charactor += string.digits
        if include_symbols:
            self.charactor += string.punctuation

    def generate(self) -> str:
        return ''.join(random.choice(self.charactor) for _ in range(self.length))
    


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_word: int = 4,
        seperator: str = '-',
        capitalization: bool = True, 
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()
        self.num_of_word = num_of_word
        self.capitalization = capitalization
        self.seperator = seperator

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_word)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
            
            return self.seperator.join(password_words)
        

if __name__ == '__main__':
    p_obj = MemorablePasswordGenerator()
    print(p_obj.generate())

    