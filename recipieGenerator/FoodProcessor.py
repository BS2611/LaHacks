from Backend.QueryGenerator import QueryGenerator
import requests


class FoodProcessor:
    __query = None
    __recipie_Name = []
    __recipie_Uri = []
    def generateRecipes(self,ingridient):
        query = QueryGenerator(ingridient)
        url = query.getUrl()
        r = requests.get(url)
        data = r.json()
        self.processResponse(data)
        return data
    def processResponse(self, data):
        for hit in data['hits']:
            recipe = hit['recipe']
            self.__recipie_Name.append(recipe["label"])
            self.__recipie_Uri.append(recipe["url"])

    def getUriList(self):
        return self.__recipie_Uri

    def getNameList(self):
        return self.__recipie_Name