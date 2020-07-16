import scrapy
from scrapy.http import TextResponse


class SolarRadioSweetRhythmsChartSpider(scrapy.Spider):
    name = "SolarRadioSweetRhythmsChartSpider"
    start_urls = [
        "http://www.solarradio.com/show/sweet-rhythms-chart/",
    ]

    def parse(self, response: TextResponse):
        chart_link = response.xpath(
            '//a[contains(@href, "playlists/")]/@href'
        ).extract_first()
        yield response.follow(chart_link, callback=self._parse_playlist)

    @staticmethod
    def _parse_playlist(response: TextResponse) -> dict:
        chart = response.xpath('//div[@class="myplaylist-playlist-entires"]/table//tr')

        for item in chart[1:]:
            artist = item.xpath("td[3]//text()").extract_first() or ""
            song_title = item.xpath("td[4]//text()").extract_first() or ""
            album_title = item.xpath("td[5]//text()").extract_first() or ""
            label = item.xpath("td[6]//text()").extract_first() or ""

            song = dict()
            song["artist"] = artist
            song["song_title"] = song_title
            song["album_title"] = album_title
            song["label"] = label

            yield song