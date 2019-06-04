# openapi_client.MarketDataApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_get_book_summary_by_currency_get**](MarketDataApi.md#public_get_book_summary_by_currency_get) | **GET** /public/get_book_summary_by_currency | Retrieves the summary information such as open interest, 24h volume, etc. for all instruments for the currency (optionally filtered by kind).
[**public_get_book_summary_by_instrument_get**](MarketDataApi.md#public_get_book_summary_by_instrument_get) | **GET** /public/get_book_summary_by_instrument | Retrieves the summary information such as open interest, 24h volume, etc. for a specific instrument.
[**public_get_contract_size_get**](MarketDataApi.md#public_get_contract_size_get) | **GET** /public/get_contract_size | Retrieves contract size of provided instrument.
[**public_get_currencies_get**](MarketDataApi.md#public_get_currencies_get) | **GET** /public/get_currencies | Retrieves all cryptocurrencies supported by the API.
[**public_get_funding_chart_data_get**](MarketDataApi.md#public_get_funding_chart_data_get) | **GET** /public/get_funding_chart_data | Retrieve the latest user trades that have occurred for PERPETUAL instruments in a specific currency symbol and within given time range.
[**public_get_historical_volatility_get**](MarketDataApi.md#public_get_historical_volatility_get) | **GET** /public/get_historical_volatility | Provides information about historical volatility for given cryptocurrency.
[**public_get_index_get**](MarketDataApi.md#public_get_index_get) | **GET** /public/get_index | Retrieves the current index price for the instruments, for the selected currency.
[**public_get_instruments_get**](MarketDataApi.md#public_get_instruments_get) | **GET** /public/get_instruments | Retrieves available trading instruments. This method can be used to see which instruments are available for trading, or which instruments have existed historically.
[**public_get_last_settlements_by_currency_get**](MarketDataApi.md#public_get_last_settlements_by_currency_get) | **GET** /public/get_last_settlements_by_currency | Retrieves historical settlement, delivery and bankruptcy events coming from all instruments within given currency.
[**public_get_last_settlements_by_instrument_get**](MarketDataApi.md#public_get_last_settlements_by_instrument_get) | **GET** /public/get_last_settlements_by_instrument | Retrieves historical public settlement, delivery and bankruptcy events filtered by instrument name.
[**public_get_last_trades_by_currency_and_time_get**](MarketDataApi.md#public_get_last_trades_by_currency_and_time_get) | **GET** /public/get_last_trades_by_currency_and_time | Retrieve the latest trades that have occurred for instruments in a specific currency symbol and within given time range.
[**public_get_last_trades_by_currency_get**](MarketDataApi.md#public_get_last_trades_by_currency_get) | **GET** /public/get_last_trades_by_currency | Retrieve the latest trades that have occurred for instruments in a specific currency symbol.
[**public_get_last_trades_by_instrument_and_time_get**](MarketDataApi.md#public_get_last_trades_by_instrument_and_time_get) | **GET** /public/get_last_trades_by_instrument_and_time | Retrieve the latest trades that have occurred for a specific instrument and within given time range.
[**public_get_last_trades_by_instrument_get**](MarketDataApi.md#public_get_last_trades_by_instrument_get) | **GET** /public/get_last_trades_by_instrument | Retrieve the latest trades that have occurred for a specific instrument.
[**public_get_order_book_get**](MarketDataApi.md#public_get_order_book_get) | **GET** /public/get_order_book | Retrieves the order book, along with other market values for a given instrument.
[**public_get_trade_volumes_get**](MarketDataApi.md#public_get_trade_volumes_get) | **GET** /public/get_trade_volumes | Retrieves aggregated 24h trade volumes for different instrument types and currencies.
[**public_get_tradingview_chart_data_get**](MarketDataApi.md#public_get_tradingview_chart_data_get) | **GET** /public/get_tradingview_chart_data | Publicly available market data used to generate a TradingView candle chart.
[**public_ticker_get**](MarketDataApi.md#public_ticker_get) | **GET** /public/ticker | Get ticker for an instrument.


# **public_get_book_summary_by_currency_get**
> object public_get_book_summary_by_currency_get(currency, kind=kind)

Retrieves the summary information such as open interest, 24h volume, etc. for all instruments for the currency (optionally filtered by kind).

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)

try:
    # Retrieves the summary information such as open interest, 24h volume, etc. for all instruments for the currency (optionally filtered by kind).
    api_response = api_instance.public_get_book_summary_by_currency_get(currency, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_book_summary_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_book_summary_by_instrument_get**
> object public_get_book_summary_by_instrument_get(instrument_name)

Retrieves the summary information such as open interest, 24h volume, etc. for a specific instrument.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieves the summary information such as open interest, 24h volume, etc. for a specific instrument.
    api_response = api_instance.public_get_book_summary_by_instrument_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_book_summary_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_contract_size_get**
> object public_get_contract_size_get(instrument_name)

Retrieves contract size of provided instrument.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieves contract size of provided instrument.
    api_response = api_instance.public_get_contract_size_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_contract_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_currencies_get**
> object public_get_currencies_get()

Retrieves all cryptocurrencies supported by the API.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves all cryptocurrencies supported by the API.
    api_response = api_instance.public_get_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_funding_chart_data_get**
> object public_get_funding_chart_data_get(instrument_name, length=length)

Retrieve the latest user trades that have occurred for PERPETUAL instruments in a specific currency symbol and within given time range.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
length = 'length_example' # str | Specifies time period. `8h` - 8 hours, `24h` - 24 hours (optional)

try:
    # Retrieve the latest user trades that have occurred for PERPETUAL instruments in a specific currency symbol and within given time range.
    api_response = api_instance.public_get_funding_chart_data_get(instrument_name, length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_funding_chart_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **length** | **str**| Specifies time period. &#x60;8h&#x60; - 8 hours, &#x60;24h&#x60; - 24 hours | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_historical_volatility_get**
> object public_get_historical_volatility_get(currency)

Provides information about historical volatility for given cryptocurrency.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Provides information about historical volatility for given cryptocurrency.
    api_response = api_instance.public_get_historical_volatility_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_historical_volatility_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_index_get**
> object public_get_index_get(currency)

Retrieves the current index price for the instruments, for the selected currency.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Retrieves the current index price for the instruments, for the selected currency.
    api_response = api_instance.public_get_index_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_instruments_get**
> object public_get_instruments_get(currency, kind=kind, expired=expired)

Retrieves available trading instruments. This method can be used to see which instruments are available for trading, or which instruments have existed historically.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
expired = False # bool | Set to true to show expired instruments instead of active ones. (optional) (default to False)

try:
    # Retrieves available trading instruments. This method can be used to see which instruments are available for trading, or which instruments have existed historically.
    api_response = api_instance.public_get_instruments_get(currency, kind=kind, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_instruments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **expired** | **bool**| Set to true to show expired instruments instead of active ones. | [optional] [default to False]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_settlements_by_currency_get**
> object public_get_last_settlements_by_currency_get(currency, type=type, count=count, continuation=continuation, search_start_timestamp=search_start_timestamp)

Retrieves historical settlement, delivery and bankruptcy events coming from all instruments within given currency.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Settlement type (optional)
count = 56 # int | Number of requested items, default - `20` (optional)
continuation = 'xY7T6cutS3t2B9YtaDkE6TS379oKnkzTvmEDUnEUP2Msa9xKWNNaT' # str | Continuation token for pagination (optional)
search_start_timestamp = 1536569522277 # int | The latest timestamp to return result for (optional)

try:
    # Retrieves historical settlement, delivery and bankruptcy events coming from all instruments within given currency.
    api_response = api_instance.public_get_last_settlements_by_currency_get(currency, type=type, count=count, continuation=continuation, search_start_timestamp=search_start_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_settlements_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Settlement type | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 
 **continuation** | **str**| Continuation token for pagination | [optional] 
 **search_start_timestamp** | **int**| The latest timestamp to return result for | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_settlements_by_instrument_get**
> object public_get_last_settlements_by_instrument_get(instrument_name, type=type, count=count, continuation=continuation, search_start_timestamp=search_start_timestamp)

Retrieves historical public settlement, delivery and bankruptcy events filtered by instrument name.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
type = 'type_example' # str | Settlement type (optional)
count = 56 # int | Number of requested items, default - `20` (optional)
continuation = 'xY7T6cutS3t2B9YtaDkE6TS379oKnkzTvmEDUnEUP2Msa9xKWNNaT' # str | Continuation token for pagination (optional)
search_start_timestamp = 1536569522277 # int | The latest timestamp to return result for (optional)

try:
    # Retrieves historical public settlement, delivery and bankruptcy events filtered by instrument name.
    api_response = api_instance.public_get_last_settlements_by_instrument_get(instrument_name, type=type, count=count, continuation=continuation, search_start_timestamp=search_start_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_settlements_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **type** | **str**| Settlement type | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 
 **continuation** | **str**| Continuation token for pagination | [optional] 
 **search_start_timestamp** | **int**| The latest timestamp to return result for | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_trades_by_currency_and_time_get**
> object public_get_last_trades_by_currency_and_time_get(currency, start_timestamp, end_timestamp, kind=kind, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest trades that have occurred for instruments in a specific currency symbol and within given time range.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest trades that have occurred for instruments in a specific currency symbol and within given time range.
    api_response = api_instance.public_get_last_trades_by_currency_and_time_get(currency, start_timestamp, end_timestamp, kind=kind, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_trades_by_currency_and_time_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **start_timestamp** | **int**| The earliest timestamp to return result for | 
 **end_timestamp** | **int**| The most recent timestamp to return result for | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_trades_by_currency_get**
> object public_get_last_trades_by_currency_get(currency, kind=kind, start_id=start_id, end_id=end_id, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest trades that have occurred for instruments in a specific currency symbol.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
start_id = 'start_id_example' # str | The ID number of the first trade to be returned (optional)
end_id = 'end_id_example' # str | The ID number of the last trade to be returned (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest trades that have occurred for instruments in a specific currency symbol.
    api_response = api_instance.public_get_last_trades_by_currency_get(currency, kind=kind, start_id=start_id, end_id=end_id, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_trades_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **start_id** | **str**| The ID number of the first trade to be returned | [optional] 
 **end_id** | **str**| The ID number of the last trade to be returned | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_trades_by_instrument_and_time_get**
> object public_get_last_trades_by_instrument_and_time_get(instrument_name, start_timestamp, end_timestamp, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest trades that have occurred for a specific instrument and within given time range.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest trades that have occurred for a specific instrument and within given time range.
    api_response = api_instance.public_get_last_trades_by_instrument_and_time_get(instrument_name, start_timestamp, end_timestamp, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_trades_by_instrument_and_time_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **start_timestamp** | **int**| The earliest timestamp to return result for | 
 **end_timestamp** | **int**| The most recent timestamp to return result for | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_last_trades_by_instrument_get**
> object public_get_last_trades_by_instrument_get(instrument_name, start_seq=start_seq, end_seq=end_seq, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest trades that have occurred for a specific instrument.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_seq = 56 # int | The sequence number of the first trade to be returned (optional)
end_seq = 56 # int | The sequence number of the last trade to be returned (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest trades that have occurred for a specific instrument.
    api_response = api_instance.public_get_last_trades_by_instrument_get(instrument_name, start_seq=start_seq, end_seq=end_seq, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_last_trades_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **start_seq** | **int**| The sequence number of the first trade to be returned | [optional] 
 **end_seq** | **int**| The sequence number of the last trade to be returned | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_order_book_get**
> object public_get_order_book_get(instrument_name, depth=depth)

Retrieves the order book, along with other market values for a given instrument.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'instrument_name_example' # str | The instrument name for which to retrieve the order book, see [`getinstruments`](#getinstruments) to obtain instrument names.
depth = 3.4 # float | The number of entries to return for bids and asks. (optional)

try:
    # Retrieves the order book, along with other market values for a given instrument.
    api_response = api_instance.public_get_order_book_get(instrument_name, depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_order_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| The instrument name for which to retrieve the order book, see [&#x60;getinstruments&#x60;](#getinstruments) to obtain instrument names. | 
 **depth** | **float**| The number of entries to return for bids and asks. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_trade_volumes_get**
> object public_get_trade_volumes_get()

Retrieves aggregated 24h trade volumes for different instrument types and currencies.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves aggregated 24h trade volumes for different instrument types and currencies.
    api_response = api_instance.public_get_trade_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_trade_volumes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_tradingview_chart_data_get**
> object public_get_tradingview_chart_data_get(instrument_name, start_timestamp, end_timestamp)

Publicly available market data used to generate a TradingView candle chart.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for

try:
    # Publicly available market data used to generate a TradingView candle chart.
    api_response = api_instance.public_get_tradingview_chart_data_get(instrument_name, start_timestamp, end_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_get_tradingview_chart_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **start_timestamp** | **int**| The earliest timestamp to return result for | 
 **end_timestamp** | **int**| The most recent timestamp to return result for | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_ticker_get**
> object public_ticker_get(instrument_name)

Get ticker for an instrument.

### Example

* Bearer (Auth. Token) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization (Auth. Token): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = openapi_client.MarketDataApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Get ticker for an instrument.
    api_response = api_instance.public_ticker_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->public_ticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

