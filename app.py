import requests


class CurrentWeather:

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": "76017"}

    headers = {
        "X-RapidAPI-Key": "2c71ce1e67mshbe095b0bbab43e8p116612jsnb270b2e19b38",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    def __init__(self):
        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring).json()

    @property
    def current_weather(self):
        return self.response['current']


class Forecast:
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": "76017", "days": "3"}

    headers = {
        "X-RapidAPI-Key": "2c71ce1e67mshbe095b0bbab43e8p116612jsnb270b2e19b38",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    def __init__(self):
        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring).json()

    @property
    def weather(self):
        return self.response['current']


class MeteomaticsAPI:
                                          # https://
                                          # api.meteomatics.com
                                          # /
                                          # 2023-02-01T03:10:00.000-06:00
                                          # /
                                          # t_2m:C
                                          # /
                                          # 51.5073219,-0.1276474
                                          # /
                                          # json
                                          # ?
                                          # model
                                          # =
                                          # mix
    url = 'https://api.meteomatics.com/'  # /validdatetime/parameters/locations/format?optionals

    def __init__(self, validdatetime: str = None, parameters: str = None, locations: str = None, format: str = None):
        if validdatetime:
            self.url += validdatetime + '/'
        if parameters:
            self.url += parameters + '/'
        if locations:
            self.url += locations + '/'
        if format:
            self.url += format

        self.user = ('personal_sargent', 'wZ0Ba93yMm')

        print(self.url)
        self.response = requests.post(self.url, auth=self.user, headers={'Accept': 'application/octet-stream'}).json()
        for i in self.response:
            print(f'{i} = {self.response[i]}')


if __name__ == "__main__":

    MeteomaticsAPI(validdatetime='2023-02-03T00:00:00Z', parameters='t_2m:C', locations='32.705002,-97.122780', format='json')


