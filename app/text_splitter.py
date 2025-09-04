class TextSlpitter:
    def __init__(self, text):
        self.text = text
        self.length = len(text)

    def split(self, parts=2):
        chunk_size = (self.length // parts) + 1
        return [self.text[i:i + chunk_size] for i in range(0, self.length, chunk_size)]
