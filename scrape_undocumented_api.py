url = "https://tracreports.org/phptools/immigration/closure/table_json.php"

params = {
    "stat": "count",
    "state": "5",
    "custody": "1",
    "dimension": "represented",
    "sort": "valdesc"
}

import requests
from pprint import pprint

response = requests.get(url, params=params)
data = response.json()

pprint(data)