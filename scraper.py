import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class DocumentSpider(scrapy.Spider):
    name = "document_crawler"
    
    def __init__(self, seed_url, output_file='output.json', max_pages=None, max_depth=None):
        self.start_urls = [seed_url]
        self.output_file = output_file
        self.max_pages = max_pages if max_pages is not None else float('inf')  
        self.max_depth = max_depth  
        self.count_pages = 0
        self.data = []  
    
    custom_settings = {}

    def update_custom_settings(self):
        if self.max_depth is not None:
            self.custom_settings['DEPTH_LIMIT'] = self.max_depth
        if self.max_pages is not None:
            self.custom_settings['CLOSESPIDER_PAGECOUNT'] = self.max_pages

    def parse(self, response):
        self.count_pages += 1
        html_content = response.text
        self.data.append({
            'url': response.url,
            'content': html_content
        })

        # Follow links to next pages only if under page limit
        if self.count_pages < self.max_pages:
            for href in response.css('a::attr(href)'):
                full_url = response.urljoin(href.extract())
                yield scrapy.Request(full_url, callback=self.parse)

    def closed(self, reason):
        # When the spider closes, write the data to a JSON file
        with open(self.output_file, 'w') as f:
            json.dump(self.data, f)

    def start_requests(self):
        # Update custom settings before starting requests
        self.update_custom_settings()
        # Return the initial requests for the spider
        yield from super().start_requests()

# Example usage:
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(DocumentSpider, seed_url='https://books.toscrape.com/')
    process.start()
