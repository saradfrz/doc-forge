# Doc Forge

A simple Python project for reading PDF files and updating configuration parameters from the terminal.

## Features
- Extract text from PDF files by page or range (see `app/pdf_reader.py`)
- Update parameters in `config.py` using a terminal command (see `update_config.py`)

## Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

### Extracting PDF Text
Use the `PDFReader` class in `app/pdf_reader.py` to extract text from PDF files.

### Updating Config Parameters
Update a parameter in `config.py` from the terminal:
```bash
python update_config.py PARAM_NAME NEW_VALUE
```
- Replace `PARAM_NAME` with the name of the parameter in `config.py`.
- Replace `NEW_VALUE` with the new value (as a string).

## Project Structure
```
monstrinho/
├── app/
│   ├── __init__.py
│   └── pdf_reader.py
├── pdf_files/
│   └── <your-pdf-files>
├── config.py
├── main.py
├── requirements.txt
├── update_config.py
└── .gitignore
```

## Examples

Extract text from a range of pages in a PDF

```python
document_manipulator = DocumentManipulator()
delta = 7
start = 1 + delta
end = 21 + delta
document_manipulator.get_text_from_pdf(start, end)
```
---

Extract all chapters from an EPUB file

```python
    for x in range(7, 26):
        document_manipulator.get_text_from_epub(x, x+1)
```

---

