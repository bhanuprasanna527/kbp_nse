# kbp_nse

kbp_nse is a Python library for getting stock data with more features. We use this library to get stock data from National Stock Exchange (NSE) which is present in India. It is one of the Largest Stock exchanges present in the World.

Let us take a look at How we can get the Stock Data? Let us see what normal stock data with fewer features look like:

| Series | Open | Close | High | Low | Volume |
|------|------|-------|------|-----|--------|

Now let us see the data that we are extracting for Individual companies listed in the National Stock Exchange:

 LAST_PRICE	 CLOSE_PRICE	 AVG_PRICE	 TTL_TRD_QNTY	 TURNOVER_LACS	 NO_OF_TRADES	 DELIV_QTY	 DELIV_PER

| SYMBOL | SERIES	DATE1 | PREV_CLOSE | OPEN_PRICE | HIGH_PRICE | LOW_PRICE | LAST_PRICE | CLOSE_PRICE | AVG_PRICE | TTL_TRD_QNTY | TURNOVER_LACS | NO_OF_TRADES | DELIV_QTY | DELIV_PER |
|------|------|-------|------|-----|--------|------|------|-------|------|-----|--------| ------ | ------ |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install kbp_nse
```

## Usage

```python
from kbp_nse import kbp_nse

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
