from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, title, text, ext, pages):
        self.title = title
        self.text = text
        self.extension = ext
        self.pages = pages

    @abstractmethod
    def print_document(self):
        pass


class ExcellDocument(Document):
    def print_document(self):
        print(f"Друк Excel-документа: {self.title}.{self.extension}")
        print(f"Сторінок: {self.pages}")
        print(self.text)


class WordDocument(Document):
    def print_document(self):
        print(f"Друк Word-документа: {self.title}.{self.extension}")
        print(f"Сторінок: {self.pages}")
        print(self.text)


class HtmlDocument(Document):
    def print_document(self):
        print(f"Друк HTML-документа: {self.title}.{self.extension}")
        print(f"Сторінок: {self.pages}")
        print(self.text)


class Printer:
    def __init__(self, model):
        self.model = model
    def print(self, document: Document):
        print(f"\nПринтер: {self.model}")
        document.print_document()
        print("Завершено.")


excel = ExcellDocument("Звіт", "Шось звітове", "xlsx", 56)
word = WordDocument("Реферат", "Шось дуже важливе", "docx", 8)
html = HtmlDocument("Сторінка", "Шось", "html", 2000)

printer = Printer("SuperPrinter 2000")

printer.print(excel)
printer.print(word)
printer.print(html)