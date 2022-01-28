import sys
from datetime import datetime

from utils import currency_rates_adv

script, code = sys.argv
value, date = currency_rates_adv(code=code)

if value:
    print(f'{value:.4f}, {datetime.strftime(date, "%Y-%m-%d")}')
else:
    print(datetime.strftime(date, "%Y-%m-%d"))
