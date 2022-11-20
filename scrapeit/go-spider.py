from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from sreal1.spiders.srPages2 import Srpages2Spider


process = CrawlerProcess(get_project_settings())
process.crawl(Srpages2Spider)
process.start()