import scrapy
import json


class PokemonSpider(scrapy.Spider):
    name = "pokemon"

    def start_requests(self):
        yield scrapy.Request(
            url="https://pokemondb.net/pokedex/national", callback=self.parse
        )

    def parse(self, response):
        arr = []
        for card in response.css("span.infocard-lg-data"):
            name = card.css(".ent-name::text").extract_first()
            url_details = "https://pokemondb.net/pokedex/%s" % name.lower()

            id = (
                card.css("span.infocard-lg-data small")[0]
                .css("small::text")
                .extract_first()
            )
            types_elements = (
                card.css("span.infocard-lg-data small")[1]
                .css("small a::text")
                .extract()
            )

            types = []
            for type in types_elements:
                types.append(type)

            arr.append(
                {"id": id, "name": name, "url_details": url_details, "types": types}
            )

        with open("pokemons.json", "w") as json_file:
            json.dump(arr, json_file)
        # name = response.css("span.infocard-lg-data .ent-name::text")
        # self.log("Pokemon name : %s" % name)
        # id = response.css("span.infocard-lg-data small::text").extract_first()
        # self.log("Pokemon id: %s" % id)
        # types = response.css("span.infocard-lg-data small a::text").extract_first()
        # self.log("Pokemon type: %s" % types)
