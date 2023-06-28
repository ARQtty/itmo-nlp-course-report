from lxml import html
from src.parsers.utils import download_url


class SpbDnevnikPage:
    def __init__(self, page_source: str):
        self._tree = html.fromstring(page_source)

    def get_header(self) -> str:
        return self._tree.xpath("//h2[@class='news-full--element-title']")[0].text

    def get_subtitle(self) -> str:
        return self._tree.xpath("//div[@class='news-full--element-subtitle']")[0].text

    def get_main_text(self) -> str:
        return self._tree.xpath("//div[@class='news-full--element-text']")[0].text_content().strip()

    def get_create_date(self) -> str:
        return self._tree.xpath("//time[@class='news-full--element-date']")[0].text

    def __repr__(self) -> str:
        return f'{self.get_header()}\n\n{self.get_create_date()}\n\n{self.get_subtitle()}\n{self.get_main_text()}'


if __name__ == '__main__':
    page = download_url('https://spbdnevnik.ru/news/2018-01-01/deputat-romanov-vruchil-invalidnuyu-kolyasku-novogo-pokoleniya-glave-fizkulturno-sportivnogo-kluba--paralimpik')
    page = SpbDnevnikPage(page)
    print(page)
