import scrapy

class QuotesSpider(scrapy.Spider): # here QuotesSpider is the class having subclass which is scrapy.Spider created and have defined some attributes and methods
    name = 'quotes'  # name of the spider(has to be unique)
    
    """ 
    def start_requests(self):
        # initially I am going to scrap just two pages of website(having two urls)
        urls = ['http://quotes.toscrape.com/page/1',
               'http://quotes.toscrape.com/page/2'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page # this will create two files viz. quotes-1.html and quotes-2.html
        
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' % filename) 
    """
    
    # Shortcut way to do above thing
    start_urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2'
        ]
    def parse(self, response):    # this is default call-back method 
        """ 
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        """
        
        for quote in response.css('div.quote'):  # here, div.quote => koi div hai uske ander yek class ka name 'quote' hai
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }    
            
'''
Note: 
- start_requests function generates scrapy.requests objects from urls which is bit lengthy, there is shortcut to it
- the best way to extract data with scrapy is trying selector using the scrapy shell
'''