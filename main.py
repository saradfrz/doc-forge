from config import FILEPATH, MAX_CHUNK_SIZE, PROMPT_FILE
from app.pdf_reader import PDFReader
from app.epub_reader import EPUBReader
from app.text_splitter import TextSlpitter

from app.prompt_creator import PromptCreator

import re

class DocumentManipulator():

    def __init__(self):
        self.filename = FILEPATH.split('\\')[-1].split('.')[0].replace(' ', '')

    def get_text_from_epub(self, start,end):
        epub_reader = EPUBReader(FILEPATH)
        text = epub_reader.extract_text_by_spine_range(start, end)
        text = self.text_sanitizer(text)
        with open(f'output/epub_output_{start}_{end}.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Text from spine range {start}-{end} saved to output/epub_output_{start}_{end}.txt')

    def get_text_from_pdf(self, start_page, end_page):
        filename = self.filename
        pdf_reader = PDFReader(FILEPATH)
        text = pdf_reader.extract_text_by_page_range(start_page, end_page)
        text = self.text_sanitizer(text)
        with open(f'output/{filename}_{start_page}_{end_page}.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Text from page range {start_page}_{end_page} saved to output/{filename}_{start_page}_{end_page}.txt')

        self.test_generator(text)

    def text_sanitizer(self, text):
        text = re.sub(r'\n+', '\n', text)
        # Implement your text sanitization logic here
        return text
    
    def test_generator(self, text):
        filename = self.filename
        with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
            prompt = f.read()

        text_splitter = TextSlpitter(text)
        n_parts = len(text) // MAX_CHUNK_SIZE
        chunks = text_splitter.split(parts=n_parts)

        for n, chunk in enumerate(chunks):
            with open(f'{filename}_{n}.txt', 'w', encoding='utf-8') as f:
                f.write(prompt + '\n\n\n' + chunk)
            print(f'Text from {filename} saved to output/{filename}_{n}.txt')


if __name__ == '__main__':
    filepath = 'input\\medallion_ch03.txt'
    output_folder = 'medallion_prompts'
    prompt_path = 'prompts\\ellaborate_questions.txt'

    prompt_creator = PromptCreator(filepath, output_folder, prompt_path)
    prompt_creator.create_prompts()

