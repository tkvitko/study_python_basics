import sys
from datetime import datetime

from utils.tools import currency_rates

script, code = sys.argv
value, date = currency_rates(code=code)

if value:
    print(f'{value:.2f}, {datetime.strftime(date, "%Y-%m-%d")}')
else:
    print(datetime.strftime(date, "%Y-%m-%d"))
