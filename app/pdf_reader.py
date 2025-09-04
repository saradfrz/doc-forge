from pypdf import PdfReader

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = self._read()
        self.number_of_pages = len(self.reader.pages)

    def _read(self):
        reader = PdfReader(self.file_path)
        return reader
    
    def extract_all_text(self):
        all_text = ''
        for i in range(self.number_of_pages):
            page = self.reader.pages[i]
            text = page.extract_text()
            all_text += text
        return all_text
    
    def extract_text_by_page_range(self, start_page, end_page):
        if start_page > end_page or start_page < 0 or end_page >= self.number_of_pages:
            raise ValueError("Invalid page range")
        
        range_text = ''
        for i in range(start_page, end_page + 1):
            page = self.reader.pages[i]
            text = page.extract_text()
            range_text += text
        return range_text
    

    