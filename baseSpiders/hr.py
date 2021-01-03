import baseSpiders.baseSpider

class hrSpider(baseSpiders.baseSpider.baseSpider):
    def get_loop(self, response):
        return response.css('li.c-epgBroadcast__item')
    
    def get_date(self, response, item, counter):
        return response.css('span.c-epgControlBar__date:nth-child(2)::text').extract_first().strip()[-6:]
    
    def get_time(self, response, item, counter):
        return response.css('.c-epgBroadcast__startTime > time::text').extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('div:nth-child(2) > span:nth-child(1)::text').extract_first().strip().lower()

""" 
<li class="c-epgBroadcast__item" itemscope="" itemtype="https://schema.org/MusicRecording">
<div class="c-epgBroadcast__timeWrapper">
<div class="c-epgBroadcast__time">
<strong class="c-epgBroadcast__startTime">
<time datetime="2021-01-03T14:46+0100" itemprop="duration" content="T192S">14:46</time>
</strong>
</div>
</div>
<div class="c-epgBroadcast__details">
<span class="c-epgBroadcast__headline text__headline" itemprop="name">
Dreh dich
</span>
<span class="c-epgBroadcast__subline text__subline">
<span itemprop="byArtist" itemscope="" itemtype="https://schema.org/MusicGroup">
<span itemprop="name">
Nena
</span>
</span>
</span>
</div>
</li>
 """