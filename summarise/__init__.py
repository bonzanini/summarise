__all__ = ['Summariser']

class Summariser:

    def __init__(self, sentences):
        self.sentences = sentences

    def __repr__(self):
        return "Summariser() object. Full text has %d sentences" % len(self.sentences)

    def summarise(self, size=2):
        if len(self.sentences) >= size:
            return self.sentences[:size]
        else:
            return self.sentences
