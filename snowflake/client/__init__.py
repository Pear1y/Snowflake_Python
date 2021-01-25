import requests
import json


class SnowflakeClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.api_uri = 'http://%s:%s/' % (self.host, self.port)
        self.Session = requests.Session()

    def get_guid(self):
        res = self.Session.get(self.api_uri)
        res.close()
        return int(res.text)

    def get_stats(self):
        res = self.Session.get(self.api_uri + 'stats', headers=self.headers)
        res.close()
        return json.loads(res.text)


default_client = SnowflakeClient('localhost', 8910)

def setup(host, port):
    global default_client
    default_client = SnowflakeClient(host, port)


def get_guid():
    return default_client.get_guid()


def get_stats():
    return default_client.get_stats()