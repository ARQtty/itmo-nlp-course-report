from lxml import html


class Moyka78Page:
    def __init__(self, page_source: str):
        self._tree = html.fromstring(page_source)

    def get_header(self) -> str:
        return self._tree.xpath("//section[@class='single-top']")[0].xpath('//h1')[0].text

    def get_citation(self) -> str:
        style = 'background-color: #fff;display: block;border-left: 4px solid #ec345e;margin: 24px 0;font-size: 20px;line-height: 26px;font-style: italic;padding-left: 48px;line-height: 26px;'
        citations = self._tree.xpath(f"//div[@style='{style}']")
        citations = [c.text_content() for c in citations]
        return '\n'.join(citations)

    def get_main_text(self) -> str:
        texts = self._tree.xpath("//section[@class='single-body']")[0].xpath('//p')[:-1]
        texts = [t.text_content() for t in texts]
        return '\n '.join(texts)

    def get_create_date(self) -> str:
        return self._tree.xpath("//time[@itemprop='dateCreated datePublished']")[0].attrib['datetime']

    def __repr__(self) -> str:
        return f'{self.get_header()}\n\n{self.get_create_date()}\n\n{self.get_main_text()}\n\n{self.get_citation()}'
