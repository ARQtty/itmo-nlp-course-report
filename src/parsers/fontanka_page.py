from lxml import html
from src.parsers.utils import download_url


class FontankaPage:
    def __init__(self, page_source: str):
        self._tree = html.fromstring(page_source)

    def get_header(self) -> str:
        return self._tree.xpath("//h1")[0].text

    def get_main_text(self) -> str:
        paragraphs = self._tree.xpath("//div[@class='DVah MJa1 MJah']")#[0].text_content().strip()
        paragraphs = [p.text_content().strip() for p in paragraphs]
        return '\n '.join(paragraphs)

    def get_create_date(self) -> str:
        return self._tree.xpath("//span[@itemprop='datePublished']")[0].text

    def __repr__(self) -> str:
        return f'{self.get_header()}\n\n{self.get_create_date()}\n\n{self.get_main_text()}'


if __name__ == '__main__':
    page = download_url('https://www.fontanka.ru/2018/01/12/047/')
    page = FontankaPage(page)
    print(page)
