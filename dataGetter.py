import requests


class DataGetter(object):
    def __init__(self, data_url):
        self.data_url = data_url

    def set_data_url(self, data_url):
        self.data_url = data_url

    def get_data_url(self):
        return self.data_url

    def get_json_data(self, **payload):
        try:
            resp = requests.get(self.data_url, params=payload)
        except Exception as e:
            raise Exception("Erro ao recuperar os dados do servidor!!!")

        if resp.status_code != requests.codes.ok:
            raise Exception("Erro ao recuperar os dados do servidor!!!")

        return resp.json() if resp.content else "Sem resultados"
        
