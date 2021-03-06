"""
Created by Alex
"""
import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        result = requests.get(url)

        if result.status_code != 200:
            return {} if return_json else ''
        return result.json() if return_json else result.text



