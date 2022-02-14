import scrapy
from ..items import JotformItem


class LondonrelocationSpider(scrapy.Spider):
    name = 'londonrelocation'
    start_urls = ['https://londonrelocation.com/our-properties-to-rent/properties/?keyword=aldgate',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=angel',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=ascot',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=balham',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=barnsbury',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=battersea',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=battersea+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=bayswater',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=belsize+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=bermondsey',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=blackheath',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=bow',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=bromley',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=camden',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=canary+wharf',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=canonbury',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=childs+hill',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=clapham',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=clerkenwel',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=dalston',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=dollis+hill',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=ealing',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=east+acton',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=east+finchley',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=east+putney',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=edgware',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=euston',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=farringdon',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=fulham',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=greenwich',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=gunnersbury',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=hackney',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=haggerston',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=hampstead',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=harpenden',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=harrow',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=heather+glen',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=highbury',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=holloway',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=imperial+wharf',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=islington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=kensington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=kilburn+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=kings+cross',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=ladbroke+grove',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=lancaster+gate',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=leicester',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=lewisham',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=lower+holloway',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=maida+vale',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=marylebone',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=ealing',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=north+greenwich',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=northgate',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=northwood',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=notting+hill',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=old+street',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=paddington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=pimlico',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=poplar',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=primrose+hill',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=putney',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=queens+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=raynes+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=richmond',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=royal+oak',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=shoreditch',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=soho',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=south+acton',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=south+hackney',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=south+kensington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=south+norwood',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=south+woodford',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=southwark',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=St+Johns+Wood',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=stoke+newington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=streatham',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=swiss+cottage',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=teddington',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=tooting',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=turnham+green',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=wandsworth',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=waterloo',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=west+brompton',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=west+ealing',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=west+hampstead',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=west+kilburn',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=westbourne+park',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=weston+green',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=weybridge',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=wimbledon',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=winchester',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=wood+green',
              'https://londonrelocation.com/our-properties-to-rent/properties/?keyword=woolwich']


    def parse(self, response):
        items = JotformItem()
        all_divs = response.css('.test-box')
        for place in all_divs:
            title        = [i.lstrip('\n') for i in place.css('.h4-space a::text').extract()]
            price        = [i.strip(' pcm£') for i in place.css('h5::text').extract()]
            property_url = ["https://londonrelocation.com" + i for i in place.css('.h4-space a').xpath('@href').extract()]

            # Record data 
            items['title']        = title
            items['price']        = price
            items['property_url'] = property_url

            # Return data
            yield items
