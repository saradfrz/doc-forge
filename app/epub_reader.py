import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class EPUBReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = self._read()
        self.spine_items = [item for item in self.reader.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
        self.len_spine_items = len(self.spine_items)

    def _read(self):
        reader = epub.read_epub(self.file_path)
        return reader
    
    def extract_text_by_spine_range(self, start=0, end=None):
        extracted = []

        if end is None or end > len(self.spine_items):
            end = len(self.spine_items)

        for i in range(start, end):
            soup = BeautifulSoup(self.spine_items[i].get_content(), 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            extracted.append(text)

        return '\n\n'.join(extracted)
    

    