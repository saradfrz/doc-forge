from config import FILEPATH
from app.pdf_reader import PDFReader
from app.epub_reader import EPUBReader
from app.text_splitter import TextSlpitter

import os

class PromptCreator():

    def __init__(self, filepath, output_folder, prompt_path):
        self.filepath = filepath
        self.output_folder = output_folder
        self.filename = filepath.split('\\')[-1].split('.')[0].replace(' ', '')
        self.prompt_path = prompt_path

    def create_prompts(self):
        if not os.path.exists(f"output/{self.output_folder}"):
            os.makedirs(f"output/{self.output_folder}")

        if not os.path.exists(f"output/{self.output_folder}/{self.filename}"):
            os.makedirs(f"output/{self.output_folder}/{self.filename}")


        with open(f'{self.filepath}', 'r', encoding='utf-8') as f:
            text = f.read()

        with open(f'{self.prompt_path}', 'r', encoding='utf-8') as f:
            prompt = f.read()

        text_splitter = TextSlpitter(text)

        n_parts = len(text) // 12800
        chunks = text_splitter.split(parts=n_parts)

        for n, chunk in enumerate(chunks):
            with open(f'output/{self.output_folder}/{self.filename}/{self.filename}_{n}.txt', 'w', encoding='utf-8') as f:
                f.write(prompt + '\n\n\n' + chunk)
            print(f'Text from {self.filename} saved to output/{self.output_folder}/{self.filename}/{self.filename}_{n}.txt')