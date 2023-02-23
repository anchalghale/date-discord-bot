import re
from datetime import datetime
from datetime import timedelta

import requests

from logger import logger


def extract_date(date_string):
    pattern = r'</strong>(.+)\| <span>(.+)</span'
    matches = re.findall(pattern, date_string)
    if matches == []:
        return None
    return matches[0]


def convert_to_bs(date=None):
    '''
        Convert a date to a BS date.
        date None means today.
    '''
    today = datetime.today()
    if date is None or date == 'today':
        date = today
    if date == 'yesterday':
        date = today - timedelta(days=1)
    if date == 'tomorrow':
        date = today + timedelta(days=1)

    if type(date) == datetime:
        date = date.strftime('%Y-%m-%d')

    try:
        data = {
            'actionName': 'dconverter',
            'datefield': date,
            'convert_option': 'eng_to_nep',
        }
        res = requests.post("https://www.hamropatro.com/getMethod.php", data=data, timeout=10)
        if res.ok:
            return extract_date(res.text)
        logger.info(f'{res.status_code}, {res.text}')
        return None
    except requests.exceptions.RequestException:
        return None


if __name__ == '__main__':
    print(convert_to_bs())
