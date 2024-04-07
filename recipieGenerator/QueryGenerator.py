from dotenv import load_dotenv, dotenv_values
import os
class QueryGenerator:
    __api_id =None
    __api_key = None
    __ingridient = None
    __url = None
    __baseUrl = None
    def __init__(self, ingrdient):
        self.__ingridient = ingrdient
    def __getValues(self):
        load_dotenv()
        self.__api_id = os.getenv("APP_ID");
        self.__api_key = os.getenv("APP_KEY");
        self.__baseUrl = os.getenv("Base_URL");
    def __createQuery(self) :
        self.__getValues()
        self.__url = str(self.__baseUrl +
                "search?q=" + self.__ingridient + "&" +
                "app_id=" + self.__api_id + "&" +
                  "app_key=" + self.__api_key);



    def getUrl(self):
        self.__createQuery()
        return self.__url;