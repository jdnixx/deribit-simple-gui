# openapi_client.InternalApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_add_to_address_book_get**](InternalApi.md#private_add_to_address_book_get) | **GET** /private/add_to_address_book | Adds new entry to address book of given type
[**private_disable_tfa_with_recovery_code_get**](InternalApi.md#private_disable_tfa_with_recovery_code_get) | **GET** /private/disable_tfa_with_recovery_code | Disables TFA with one time recovery code
[**private_get_address_book_get**](InternalApi.md#private_get_address_book_get) | **GET** /private/get_address_book | Retrieves address book of given type
[**private_remove_from_address_book_get**](InternalApi.md#private_remove_from_address_book_get) | **GET** /private/remove_from_address_book | Adds new entry to address book of given type
[**private_submit_transfer_to_subaccount_get**](InternalApi.md#private_submit_transfer_to_subaccount_get) | **GET** /private/submit_transfer_to_subaccount | Transfer funds to a subaccount.
[**private_submit_transfer_to_user_get**](InternalApi.md#private_submit_transfer_to_user_get) | **GET** /private/submit_transfer_to_user | Transfer funds to a another user.
[**private_toggle_deposit_address_creation_get**](InternalApi.md#private_toggle_deposit_address_creation_get) | **GET** /private/toggle_deposit_address_creation | Enable or disable deposit address creation
[**public_get_footer_get**](InternalApi.md#public_get_footer_get) | **GET** /public/get_footer | Get information to be displayed in the footer of the website.
[**public_get_option_mark_prices_get**](InternalApi.md#public_get_option_mark_prices_get) | **GET** /public/get_option_mark_prices | Retrives market prices and its implied volatility of options instruments
[**public_validate_field_get**](InternalApi.md#public_validate_field_get) | **GET** /public/validate_field | Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.


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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling InternalApi->private_add_to_address_book_get: %s\n" % e)
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

# **private_disable_tfa_with_recovery_code_get**
> object private_disable_tfa_with_recovery_code_get(password, code)

Disables TFA with one time recovery code

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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
password = 'password_example' # str | The password for the subaccount
code = 'code_example' # str | One time recovery code

try:
    # Disables TFA with one time recovery code
    api_response = api_instance.private_disable_tfa_with_recovery_code_get(password, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_disable_tfa_with_recovery_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the subaccount | 
 **code** | **str**| One time recovery code | 

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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type

try:
    # Retrieves address book of given type
    api_response = api_instance.private_get_address_book_get(currency, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_get_address_book_get: %s\n" % e)
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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type
address = 'address_example' # str | Address in currency format, it must be in address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_remove_from_address_book_get(currency, type, address, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_remove_from_address_book_get: %s\n" % e)
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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 1 # int | Id of destination subaccount

try:
    # Transfer funds to a subaccount.
    api_response = api_instance.private_submit_transfer_to_subaccount_get(currency, amount, destination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_submit_transfer_to_subaccount_get: %s\n" % e)
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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 'destination_example' # str | Destination address from address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Transfer funds to a another user.
    api_response = api_instance.private_submit_transfer_to_user_get(currency, amount, destination, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_submit_transfer_to_user_get: %s\n" % e)
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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
state = True # bool | 

try:
    # Enable or disable deposit address creation
    api_response = api_instance.private_toggle_deposit_address_creation_get(currency, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->private_toggle_deposit_address_creation_get: %s\n" % e)
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

# **public_get_footer_get**
> object public_get_footer_get()

Get information to be displayed in the footer of the website.

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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))

try:
    # Get information to be displayed in the footer of the website.
    api_response = api_instance.public_get_footer_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->public_get_footer_get: %s\n" % e)
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

# **public_get_option_mark_prices_get**
> object public_get_option_mark_prices_get(currency)

Retrives market prices and its implied volatility of options instruments

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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Retrives market prices and its implied volatility of options instruments
    api_response = api_instance.public_get_option_mark_prices_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->public_get_option_mark_prices_get: %s\n" % e)
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
api_instance = openapi_client.InternalApi(openapi_client.ApiClient(configuration))
field = 'field_example' # str | Name of the field to be validated, examples: postal_code, date_of_birth
value = 'value_example' # str | Value to be checked
value2 = 'value2_example' # str | Additional value to be compared with (optional)

try:
    # Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
    api_response = api_instance.public_validate_field_get(field, value, value2=value2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->public_validate_field_get: %s\n" % e)
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

