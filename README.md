# kbp_nse

kbp_nse is a Python library for getting stock data with more features. We use this library to get stock data from National Stock Exchange (NSE) which is present in India. It is one of the Largest Stock exchanges present in the World.

Let us take a look at How we can get the Stock Data? Let us see what normal stock data with fewer features look like:

| Series | Open | Close | High | Low | Volume |
|------|------|-------|------|-----|--------|

Now let us see the data that we are extracting for Individual companies listed in the National Stock Exchange:


| SYMBOL | SERIES	DATE1 | PREV_CLOSE | OPEN_PRICE | HIGH_PRICE | LOW_PRICE | LAST_PRICE | CLOSE_PRICE | AVG_PRICE | TTL_TRD_QNTY | TURNOVER_LACS | NO_OF_TRADES | DELIV_QTY | DELIV_PER |
|------|------|-------|------|-----|--------|------|------|-------|------|-----|--------| ------ | ------ |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install kbp_nse.

```bash
pip install kbp_nse
```

## Usage

```python
from kbp_nse import kbp_nse
from kbp_nse import time_interval
from kbp_nse import get_csvurl
from kbp_nse import get_company

# To get the Time-Interval
ti = time_interval.get_interval(year_from=19, month_from=10)

# To get all the CSV in the given time_interval
get_csvurl.CSV_URL(ti)

# Get specific company Stock data - Originally Set to Reliance company
get_company.specific_company()

# To visualize the Data Extracted
import pandas as pd

df = pd.read_csv('RELIANCE.csv')
```

Run the above script to get accurate results. The library will be further updated with new features. 

- Currently, the library can only get Data from 2019-10-01 - Till today.
- We can data up to 715 days.
- One many thing to note is that to **Have very good internet to run this.**

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
