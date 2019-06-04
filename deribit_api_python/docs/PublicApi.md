# openapi_client.PublicApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_auth_get**](PublicApi.md#public_auth_get) | **GET** /public/auth | Authenticate
[**public_disable_heartbeat_get**](PublicApi.md#public_disable_heartbeat_get) | **GET** /public/disable_heartbeat | Stop sending heartbeat messages.
[**public_get_announcements_get**](PublicApi.md#public_get_announcements_get) | **GET** /public/get_announcements | Retrieves announcements from the last 30 days.
[**public_get_book_summary_by_currency_get**](PublicApi.md#public_get_book_summary_by_currency_get) | **GET** /public/get_book_summary_by_currency | Retrieves the summary information such as open interest, 24h volume, etc. for all instruments for the currency (optionally filtered by kind).
[**public_get_book_summary_by_instrument_get**](PublicApi.md#public_get_book_summary_by_instrument_get) | **GET** /public/get_book_summary_by_instrument | Retrieves the summary information such as open interest, 24h volume, etc. for a specific instrument.
[**public_get_contract_size_get**](PublicApi.md#public_get_contract_size_get) | **GET** /public/get_contract_size | Retrieves contract size of provided instrument.
[**public_get_currencies_get**](PublicApi.md#public_get_currencies_get) | **GET** /public/get_currencies | Retrieves all cryptocurrencies supported by the API.
[**public_get_funding_chart_data_get**](PublicApi.md#public_get_funding_chart_data_get) | **GET** /public/get_funding_chart_data | Retrieve the latest user trades that have occurred for PERPETUAL instruments in a specific currency symbol and within given time range.
[**public_get_historical_volatility_get**](PublicApi.md#public_get_historical_volatility_get) | **GET** /public/get_historical_volatility | Provides information about historical volatility for given cryptocurrency.
[**public_get_index_get**](PublicApi.md#public_get_index_get) | **GET** /public/get_index | Retrieves the current index price for the instruments, for the selected currency.
[**public_get_instruments_get**](PublicApi.md#public_get_instruments_get) | **GET** /public/get_instruments | Retrieves available trading instruments. This method can be used to see which instruments are available for trading, or which instruments have existed historically.
[**public_get_last_settlements_by_currency_get**](PublicApi.md#public_get_last_settlements_by_currency_get) | **GET** /public/get_last_settlements_by_currency | Retrieves historical settlement, delivery and bankruptcy events coming from all instruments within given currency.
[**public_get_last_settlements_by_instrument_get**](PublicApi.md#public_get_last_settlements_by_instrument_get) | **GET** /public/get_last_settlements_by_instrument | Retrieves historical public settlement, delivery and bankruptcy events filtered by instrument name.
[**public_get_last_trades_by_currency_and_time_get**](PublicApi.md#public_get_last_trades_by_currency_and_time_get) | **GET** /public/get_last_trades_by_currency_and_time | Retrieve the latest trades that have occurred for instruments in a specific currency symbol and within given time range.
[**public_get_last_trades_by_currency_get**](PublicApi.md#public_get_last_trades_by_currency_get) | **GET** /public/get_last_trades_by_currency | Retrieve the latest trades that have occurred for instruments in a specific currency symbol.
[**public_get_last_trades_by_instrument_and_time_get**](PublicApi.md#public_get_last_trades_by_instrument_and_time_get) | **GET** /public/get_last_trades_by_instrument_and_time | Retrieve the latest trades that have occurred for a specific instrument and within given time range.
[**public_get_last_trades_by_instrument_get**](PublicApi.md#public_get_last_trades_by_instrument_get) | **GET** /public/get_last_trades_by_instrument | Retrieve the latest trades that have occurred for a specific instrument.
[**public_get_order_book_get**](PublicApi.md#public_get_order_book_get) | **GET** /public/get_order_book | Retrieves the order book, along with other market values for a given instrument.
[**public_get_time_get**](PublicApi.md#public_get_time_get) | **GET** /public/get_time | Retrieves the current time (in milliseconds). This API endpoint can be used to check the clock skew between your software and Deribit&#39;s systems.
[**public_get_trade_volumes_get**](PublicApi.md#public_get_trade_volumes_get) | **GET** /public/get_trade_volumes | Retrieves aggregated 24h trade volumes for different instrument types and currencies.
[**public_get_tradingview_chart_data_get**](PublicApi.md#public_get_tradingview_chart_data_get) | **GET** /public/get_tradingview_chart_data | Publicly available market data used to generate a TradingView candle chart.
[**public_hello_get**](PublicApi.md#public_hello_get) | **GET** /public/hello | Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
[**public_set_heartbeat_get**](PublicApi.md#public_set_heartbeat_get) | **GET** /public/set_heartbeat | Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send &#x60;heartbeat&#x60; messages and &#x60;test_request&#x60; messages. Your software should respond to &#x60;test_request&#x60; messages by sending a &#x60;/api/v2/public/test&#x60; request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.
[**public_subscribe_get**](PublicApi.md#public_subscribe_get) | **GET** /public/subscribe | Subscribe to one or more channels.
[**public_test_get**](PublicApi.md#public_test_get) | **GET** /public/test | Tests the connection to the API server, and returns its version. You can use this to make sure the API is reachable, and matches the expected version.
[**public_ticker_get**](PublicApi.md#public_ticker_get) | **GET** /public/ticker | Get ticker for an instrument.
[**public_validate_field_get**](PublicApi.md#public_validate_field_get) | **GET** /public/validate_field | Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.


# **public_auth_get**
> object public_auth_get(grant_type, username, password, client_id, client_secret, refresh_token, timestamp, signature, nonce=nonce, state=state, scope=scope)

Authenticate

Retrieve an Oauth access token, to be used for authentication of 'private' requests.  Three methods of authentication are supported:  - <code>password</code> - using email and and password as when logging on to the website - <code>client_credentials</code> - using the access key and access secret that can be found on the API page on the website - <code>client_signature</code> - using the access key that can be found on the API page on the website and user generated signature. The signature is calculated using some fields provided in the request, using formula described here [Deribit signature credentials](#additional-authorization-method-deribit-signature-credentials) - <code>refresh_token</code> - using a refresh token that was received from an earlier invocation  The response will contain an access token, expiration period (number of seconds that the token is valid) and a refresh token that can be used to get a new set of tokens. 

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
grant_type = 'grant_type_example' # str | Method of authentication
username = 'your_email@mail.com' # str | Required for grant type `password`
password = 'your_password' # str | Required for grant type `password`
client_id = 'client_id_example' # str | Required for grant type `client_credentials` and `client_signature`
client_secret = 'client_secret_example' # str | Required for grant type `client_credentials`
refresh_token = 'refresh_token_example' # str | Required for grant type `refresh_token`
timestamp = 'timestamp_example' # str | Required for grant type `client_signature`, provides time when request has been generated
signature = 'signature_example' # str | Required for grant type `client_signature`; it's a cryptographic signature calculated over provided fields using user **secret key**. The signature should be calculated as an HMAC (Hash-based Message Authentication Code) with `SHA256` hash algorithm
nonce = 'nonce_example' # str | Optional for grant type `client_signature`; delivers user generated initialization vector for the server token (optional)
state = 'state_example' # str | Will be passed back in the response (optional)
scope = 'connection' # str | Describes type of the access for assigned token, possible values: `connection`, `session`, `session:name`, `trade:[read, read_write, none]`, `wallet:[read, read_write, none]`, `account:[read, read_write, none]`, `expires:NUMBER` (token will expire after `NUMBER` of seconds).</BR></BR> **NOTICE:** Depending on choosing an authentication method (```grant type```) some scopes could be narrowed by the server. e.g. when ```grant_type = client_credentials``` and ```scope = wallet:read_write``` it's modified by the server as ```scope = wallet:read``` (optional)

try:
    # Authenticate
    api_response = api_instance.public_auth_get(grant_type, username, password, client_id, client_secret, refresh_token, timestamp, signature, nonce=nonce, state=state, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_auth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Method of authentication | 
 **username** | **str**| Required for grant type &#x60;password&#x60; | 
 **password** | **str**| Required for grant type &#x60;password&#x60; | 
 **client_id** | **str**| Required for grant type &#x60;client_credentials&#x60; and &#x60;client_signature&#x60; | 
 **client_secret** | **str**| Required for grant type &#x60;client_credentials&#x60; | 
 **refresh_token** | **str**| Required for grant type &#x60;refresh_token&#x60; | 
 **timestamp** | **str**| Required for grant type &#x60;client_signature&#x60;, provides time when request has been generated | 
 **signature** | **str**| Required for grant type &#x60;client_signature&#x60;; it&#39;s a cryptographic signature calculated over provided fields using user **secret key**. The signature should be calculated as an HMAC (Hash-based Message Authentication Code) with &#x60;SHA256&#x60; hash algorithm | 
 **nonce** | **str**| Optional for grant type &#x60;client_signature&#x60;; delivers user generated initialization vector for the server token | [optional] 
 **state** | **str**| Will be passed back in the response | [optional] 
 **scope** | **str**| Describes type of the access for assigned token, possible values: &#x60;connection&#x60;, &#x60;session&#x60;, &#x60;session:name&#x60;, &#x60;trade:[read, read_write, none]&#x60;, &#x60;wallet:[read, read_write, none]&#x60;, &#x60;account:[read, read_write, none]&#x60;, &#x60;expires:NUMBER&#x60; (token will expire after &#x60;NUMBER&#x60; of seconds).&lt;/BR&gt;&lt;/BR&gt; **NOTICE:** Depending on choosing an authentication method (&#x60;&#x60;&#x60;grant type&#x60;&#x60;&#x60;) some scopes could be narrowed by the server. e.g. when &#x60;&#x60;&#x60;grant_type &#x3D; client_credentials&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;scope &#x3D; wallet:read_write&#x60;&#x60;&#x60; it&#39;s modified by the server as &#x60;&#x60;&#x60;scope &#x3D; wallet:read&#x60;&#x60;&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_disable_heartbeat_get**
> object public_disable_heartbeat_get()

Stop sending heartbeat messages.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

try:
    # Stop sending heartbeat messages.
    api_response = api_instance.public_disable_heartbeat_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_disable_heartbeat_get: %s\n" % e)
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

# **public_get_announcements_get**
> object public_get_announcements_get()

Retrieves announcements from the last 30 days.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves announcements from the last 30 days.
    api_response = api_instance.public_get_announcements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_announcements_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)

try:
    # Retrieves the summary information such as open interest, 24h volume, etc. for all instruments for the currency (optionally filtered by kind).
    api_response = api_instance.public_get_book_summary_by_currency_get(currency, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_book_summary_by_currency_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieves the summary information such as open interest, 24h volume, etc. for a specific instrument.
    api_response = api_instance.public_get_book_summary_by_instrument_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_book_summary_by_instrument_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieves contract size of provided instrument.
    api_response = api_instance.public_get_contract_size_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_contract_size_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves all cryptocurrencies supported by the API.
    api_response = api_instance.public_get_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_currencies_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
length = 'length_example' # str | Specifies time period. `8h` - 8 hours, `24h` - 24 hours (optional)

try:
    # Retrieve the latest user trades that have occurred for PERPETUAL instruments in a specific currency symbol and within given time range.
    api_response = api_instance.public_get_funding_chart_data_get(instrument_name, length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_funding_chart_data_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Provides information about historical volatility for given cryptocurrency.
    api_response = api_instance.public_get_historical_volatility_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_historical_volatility_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Retrieves the current index price for the instruments, for the selected currency.
    api_response = api_instance.public_get_index_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_index_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
expired = False # bool | Set to true to show expired instruments instead of active ones. (optional) (default to False)

try:
    # Retrieves available trading instruments. This method can be used to see which instruments are available for trading, or which instruments have existed historically.
    api_response = api_instance.public_get_instruments_get(currency, kind=kind, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_instruments_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_settlements_by_currency_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_settlements_by_instrument_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_trades_by_currency_and_time_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_trades_by_currency_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_trades_by_instrument_and_time_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling PublicApi->public_get_last_trades_by_instrument_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'instrument_name_example' # str | The instrument name for which to retrieve the order book, see [`getinstruments`](#getinstruments) to obtain instrument names.
depth = 3.4 # float | The number of entries to return for bids and asks. (optional)

try:
    # Retrieves the order book, along with other market values for a given instrument.
    api_response = api_instance.public_get_order_book_get(instrument_name, depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_order_book_get: %s\n" % e)
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

# **public_get_time_get**
> object public_get_time_get()

Retrieves the current time (in milliseconds). This API endpoint can be used to check the clock skew between your software and Deribit's systems.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves the current time (in milliseconds). This API endpoint can be used to check the clock skew between your software and Deribit's systems.
    api_response = api_instance.public_get_time_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_time_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves aggregated 24h trade volumes for different instrument types and currencies.
    api_response = api_instance.public_get_trade_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_trade_volumes_get: %s\n" % e)
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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for

try:
    # Publicly available market data used to generate a TradingView candle chart.
    api_response = api_instance.public_get_tradingview_chart_data_get(instrument_name, start_timestamp, end_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_get_tradingview_chart_data_get: %s\n" % e)
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

# **public_hello_get**
> object public_hello_get(client_name, client_version)

Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
client_name = 'My Trading Software' # str | Client software name
client_version = '1.0.2' # str | Client software version

try:
    # Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
    api_response = api_instance.public_hello_get(client_name, client_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_hello_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | **str**| Client software name | 
 **client_version** | **str**| Client software version | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_set_heartbeat_get**
> object public_set_heartbeat_get(interval)

Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send `heartbeat` messages and `test_request` messages. Your software should respond to `test_request` messages by sending a `/api/v2/public/test` request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
interval = 60 # float | The heartbeat interval in seconds, but not less than 10

try:
    # Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send `heartbeat` messages and `test_request` messages. Your software should respond to `test_request` messages by sending a `/api/v2/public/test` request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.
    api_response = api_instance.public_set_heartbeat_get(interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_set_heartbeat_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **float**| The heartbeat interval in seconds, but not less than 10 | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_subscribe_get**
> object public_subscribe_get(channels)

Subscribe to one or more channels.

Subscribe to one or more channels.  This is the same method as [/private/subscribe](#private_subscribe), but it can only be used for 'public' channels. 

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.public_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_subscribe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channels** | [**list[str]**](str.md)| A list of channels to subscribe to. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_test_get**
> object public_test_get(expected_result=expected_result)

Tests the connection to the API server, and returns its version. You can use this to make sure the API is reachable, and matches the expected version.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
expected_result = 'expected_result_example' # str | The value \"exception\" will trigger an error response. This may be useful for testing wrapper libraries. (optional)

try:
    # Tests the connection to the API server, and returns its version. You can use this to make sure the API is reachable, and matches the expected version.
    api_response = api_instance.public_test_get(expected_result=expected_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_test_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expected_result** | **str**| The value \&quot;exception\&quot; will trigger an error response. This may be useful for testing wrapper libraries. | [optional] 

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Get ticker for an instrument.
    api_response = api_instance.public_ticker_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_ticker_get: %s\n" % e)
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

# **public_validate_field_get**
> object public_validate_field_get(field, value, value2=value2)

Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.

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
api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
field = 'field_example' # str | Name of the field to be validated, examples: postal_code, date_of_birth
value = 'value_example' # str | Value to be checked
value2 = 'value2_example' # str | Additional value to be compared with (optional)

try:
    # Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
    api_response = api_instance.public_validate_field_get(field, value, value2=value2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->public_validate_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Name of the field to be validated, examples: postal_code, date_of_birth | 
 **value** | **str**| Value to be checked | 
 **value2** | **str**| Additional value to be compared with | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

