from config import FILEPATH
from app.pdf_reader import PDFReader
from app.epub_reader import EPUBReader
from app.text_splitter import TextSlpitter

import os


filepath = 'input\medallion_ch03.txt'
filename = filepath.split('\\')[-1].split('.')[0].replace(' ', '') 
output_folder = 'medallion_prompts'

if not os.path.exists(f"output/{output_folder}"):
    os.makedirs(f"output/{output_folder}")

if not os.path.exists(f"output/{output_folder}/{filename}"):
    os.makedirs(f"output/{output_folder}/{filename}")


with open(f'{filepath}', 'r', encoding='utf-8') as f:
    text = f.read()


with open('chatgpt_prompt_03.txt', 'r', encoding='utf-8') as f:
    prompt = f.read()

text_splitter = TextSlpitter(text)

n_parts = len(text) // 12800
chunks = text_splitter.split(parts=n_parts)

for n, chunk in enumerate(chunks):
    with open(f'output/{output_folder}/{filename}/{filename}_{n}.txt', 'w', encoding='utf-8') as f:
        f.write(prompt + '\n\n\n' + chunk)
    print(f'Text from {filename} saved to output/{output_folder}/{filename}/{filename}_{n}.txt')