import requests
import xmltodict


from requests.api import get


url = 'https://ClinicalTrials.gov/api/query/full_studies?expr='
diagnose = 'heart+attack'


def get_info(url, diagnose):

    rst = requests.get(url+diagnose)
    dict_data = xmltodict.parse(rst.content)
    return (dict_data)


if __name__ == '__main__':
    print(get_info(url, diagnose))
