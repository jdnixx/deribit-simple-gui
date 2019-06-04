# openapi_client.WalletApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_add_to_address_book_get**](WalletApi.md#private_add_to_address_book_get) | **GET** /private/add_to_address_book | Adds new entry to address book of given type
[**private_cancel_transfer_by_id_get**](WalletApi.md#private_cancel_transfer_by_id_get) | **GET** /private/cancel_transfer_by_id | Cancel transfer
[**private_cancel_withdrawal_get**](WalletApi.md#private_cancel_withdrawal_get) | **GET** /private/cancel_withdrawal | Cancels withdrawal request
[**private_create_deposit_address_get**](WalletApi.md#private_create_deposit_address_get) | **GET** /private/create_deposit_address | Creates deposit address in currency
[**private_get_address_book_get**](WalletApi.md#private_get_address_book_get) | **GET** /private/get_address_book | Retrieves address book of given type
[**private_get_current_deposit_address_get**](WalletApi.md#private_get_current_deposit_address_get) | **GET** /private/get_current_deposit_address | Retrieve deposit address for currency
[**private_get_deposits_get**](WalletApi.md#private_get_deposits_get) | **GET** /private/get_deposits | Retrieve the latest users deposits
[**private_get_transfers_get**](WalletApi.md#private_get_transfers_get) | **GET** /private/get_transfers | Adds new entry to address book of given type
[**private_get_withdrawals_get**](WalletApi.md#private_get_withdrawals_get) | **GET** /private/get_withdrawals | Retrieve the latest users withdrawals
[**private_remove_from_address_book_get**](WalletApi.md#private_remove_from_address_book_get) | **GET** /private/remove_from_address_book | Adds new entry to address book of given type
[**private_submit_transfer_to_subaccount_get**](WalletApi.md#private_submit_transfer_to_subaccount_get) | **GET** /private/submit_transfer_to_subaccount | Transfer funds to a subaccount.
[**private_submit_transfer_to_user_get**](WalletApi.md#private_submit_transfer_to_user_get) | **GET** /private/submit_transfer_to_user | Transfer funds to a another user.
[**private_toggle_deposit_address_creation_get**](WalletApi.md#private_toggle_deposit_address_creation_get) | **GET** /private/toggle_deposit_address_creation | Enable or disable deposit address creation
[**private_withdraw_get**](WalletApi.md#private_withdraw_get) | **GET** /private/withdraw | Creates a new withdrawal request


# **private_add_to_address_book_get**
> object private_add_to_address_book_get(currency, type, address, name, tfa=tfa)

Adds new entry to address book of given type

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type
address = 'address_example' # str | Address in currency format, it must be in address book
name = 'Main address' # str | Name of address book entry
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_add_to_address_book_get(currency, type, address, name, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_add_to_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **name** | **str**| Name of address book entry | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_transfer_by_id_get**
> object private_cancel_transfer_by_id_get(currency, id, tfa=tfa)

Cancel transfer

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
id = 12 # int | Id of transfer
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Cancel transfer
    api_response = api_instance.private_cancel_transfer_by_id_get(currency, id, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_cancel_transfer_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **id** | **int**| Id of transfer | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_withdrawal_get**
> object private_cancel_withdrawal_get(currency, id)

Cancels withdrawal request

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
id = 1 # float | The withdrawal id

try:
    # Cancels withdrawal request
    api_response = api_instance.private_cancel_withdrawal_get(currency, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_cancel_withdrawal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **id** | **float**| The withdrawal id | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_create_deposit_address_get**
> object private_create_deposit_address_get(currency)

Creates deposit address in currency

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Creates deposit address in currency
    api_response = api_instance.private_create_deposit_address_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_create_deposit_address_get: %s\n" % e)
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

# **private_get_address_book_get**
> object private_get_address_book_get(currency, type)

Retrieves address book of given type

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type

try:
    # Retrieves address book of given type
    api_response = api_instance.private_get_address_book_get(currency, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_get_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_current_deposit_address_get**
> object private_get_current_deposit_address_get(currency)

Retrieve deposit address for currency

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Retrieve deposit address for currency
    api_response = api_instance.private_get_current_deposit_address_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_get_current_deposit_address_get: %s\n" % e)
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

# **private_get_deposits_get**
> object private_get_deposits_get(currency, count=count, offset=offset)

Retrieve the latest users deposits

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Retrieve the latest users deposits
    api_response = api_instance.private_get_deposits_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_get_deposits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_transfers_get**
> object private_get_transfers_get(currency, count=count, offset=offset)

Adds new entry to address book of given type

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_get_transfers_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_get_transfers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_withdrawals_get**
> object private_get_withdrawals_get(currency, count=count, offset=offset)

Retrieve the latest users withdrawals

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Retrieve the latest users withdrawals
    api_response = api_instance.private_get_withdrawals_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_get_withdrawals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_remove_from_address_book_get**
> object private_remove_from_address_book_get(currency, type, address, tfa=tfa)

Adds new entry to address book of given type

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type
address = 'address_example' # str | Address in currency format, it must be in address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_remove_from_address_book_get(currency, type, address, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_remove_from_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_submit_transfer_to_subaccount_get**
> object private_submit_transfer_to_subaccount_get(currency, amount, destination)

Transfer funds to a subaccount.

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 1 # int | Id of destination subaccount

try:
    # Transfer funds to a subaccount.
    api_response = api_instance.private_submit_transfer_to_subaccount_get(currency, amount, destination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_submit_transfer_to_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **amount** | **float**| Amount of funds to be transferred | 
 **destination** | **int**| Id of destination subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_submit_transfer_to_user_get**
> object private_submit_transfer_to_user_get(currency, amount, destination, tfa=tfa)

Transfer funds to a another user.

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 'destination_example' # str | Destination address from address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Transfer funds to a another user.
    api_response = api_instance.private_submit_transfer_to_user_get(currency, amount, destination, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_submit_transfer_to_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **amount** | **float**| Amount of funds to be transferred | 
 **destination** | **str**| Destination address from address book | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_toggle_deposit_address_creation_get**
> object private_toggle_deposit_address_creation_get(currency, state)

Enable or disable deposit address creation

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
state = True # bool | 

try:
    # Enable or disable deposit address creation
    api_response = api_instance.private_toggle_deposit_address_creation_get(currency, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_toggle_deposit_address_creation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **state** | **bool**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_withdraw_get**
> object private_withdraw_get(currency, address, amount, priority=priority, tfa=tfa)

Creates a new withdrawal request

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
api_instance = openapi_client.WalletApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
address = 'address_example' # str | Address in currency format, it must be in address book
amount = 3.4 # float | Amount of funds to be withdrawn
priority = 'priority_example' # str | Withdrawal priority, optional for BTC, default: `high` (optional)
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Creates a new withdrawal request
    api_response = api_instance.private_withdraw_get(currency, address, amount, priority=priority, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->private_withdraw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **amount** | **float**| Amount of funds to be withdrawn | 
 **priority** | **str**| Withdrawal priority, optional for BTC, default: &#x60;high&#x60; | [optional] 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

