# openapi_client.AccountManagementApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_change_subaccount_name_get**](AccountManagementApi.md#private_change_subaccount_name_get) | **GET** /private/change_subaccount_name | Change the user name for a subaccount
[**private_create_subaccount_get**](AccountManagementApi.md#private_create_subaccount_get) | **GET** /private/create_subaccount | Create a new subaccount
[**private_disable_tfa_for_subaccount_get**](AccountManagementApi.md#private_disable_tfa_for_subaccount_get) | **GET** /private/disable_tfa_for_subaccount | Disable two factor authentication for a subaccount.
[**private_get_account_summary_get**](AccountManagementApi.md#private_get_account_summary_get) | **GET** /private/get_account_summary | Retrieves user account summary.
[**private_get_email_language_get**](AccountManagementApi.md#private_get_email_language_get) | **GET** /private/get_email_language | Retrieves the language to be used for emails.
[**private_get_new_announcements_get**](AccountManagementApi.md#private_get_new_announcements_get) | **GET** /private/get_new_announcements | Retrieves announcements that have not been marked read by the user.
[**private_get_position_get**](AccountManagementApi.md#private_get_position_get) | **GET** /private/get_position | Retrieve user position.
[**private_get_positions_get**](AccountManagementApi.md#private_get_positions_get) | **GET** /private/get_positions | Retrieve user positions.
[**private_get_subaccounts_get**](AccountManagementApi.md#private_get_subaccounts_get) | **GET** /private/get_subaccounts | Get information about subaccounts
[**private_set_announcement_as_read_get**](AccountManagementApi.md#private_set_announcement_as_read_get) | **GET** /private/set_announcement_as_read | Marks an announcement as read, so it will not be shown in &#x60;get_new_announcements&#x60;.
[**private_set_email_for_subaccount_get**](AccountManagementApi.md#private_set_email_for_subaccount_get) | **GET** /private/set_email_for_subaccount | Assign an email address to a subaccount. User will receive an email with confirmation link.
[**private_set_email_language_get**](AccountManagementApi.md#private_set_email_language_get) | **GET** /private/set_email_language | Changes the language to be used for emails.
[**private_set_password_for_subaccount_get**](AccountManagementApi.md#private_set_password_for_subaccount_get) | **GET** /private/set_password_for_subaccount | Set the password for the subaccount
[**private_toggle_notifications_from_subaccount_get**](AccountManagementApi.md#private_toggle_notifications_from_subaccount_get) | **GET** /private/toggle_notifications_from_subaccount | Enable or disable sending of notifications for the subaccount.
[**private_toggle_subaccount_login_get**](AccountManagementApi.md#private_toggle_subaccount_login_get) | **GET** /private/toggle_subaccount_login | Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.
[**public_get_announcements_get**](AccountManagementApi.md#public_get_announcements_get) | **GET** /public/get_announcements | Retrieves announcements from the last 30 days.


# **private_change_subaccount_name_get**
> object private_change_subaccount_name_get(sid, name)

Change the user name for a subaccount

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
name = 'newUserName' # str | The new user name

try:
    # Change the user name for a subaccount
    api_response = api_instance.private_change_subaccount_name_get(sid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_change_subaccount_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **name** | **str**| The new user name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_create_subaccount_get**
> object private_create_subaccount_get()

Create a new subaccount

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))

try:
    # Create a new subaccount
    api_response = api_instance.private_create_subaccount_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_create_subaccount_get: %s\n" % e)
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

# **private_disable_tfa_for_subaccount_get**
> object private_disable_tfa_for_subaccount_get(sid)

Disable two factor authentication for a subaccount.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount

try:
    # Disable two factor authentication for a subaccount.
    api_response = api_instance.private_disable_tfa_for_subaccount_get(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_disable_tfa_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_account_summary_get**
> object private_get_account_summary_get(currency, extended=extended)

Retrieves user account summary.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
extended = false # bool | Include additional fields (optional)

try:
    # Retrieves user account summary.
    api_response = api_instance.private_get_account_summary_get(currency, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_account_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **extended** | **bool**| Include additional fields | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_email_language_get**
> object private_get_email_language_get()

Retrieves the language to be used for emails.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves the language to be used for emails.
    api_response = api_instance.private_get_email_language_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_email_language_get: %s\n" % e)
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

# **private_get_new_announcements_get**
> object private_get_new_announcements_get()

Retrieves announcements that have not been marked read by the user.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves announcements that have not been marked read by the user.
    api_response = api_instance.private_get_new_announcements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_new_announcements_get: %s\n" % e)
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

# **private_get_position_get**
> object private_get_position_get(instrument_name)

Retrieve user position.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieve user position.
    api_response = api_instance.private_get_position_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_position_get: %s\n" % e)
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

# **private_get_positions_get**
> object private_get_positions_get(currency, kind=kind)

Retrieve user positions.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | 
kind = 'kind_example' # str | Kind filter on positions (optional)

try:
    # Retrieve user positions.
    api_response = api_instance.private_get_positions_get(currency, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **kind** | **str**| Kind filter on positions | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_subaccounts_get**
> object private_get_subaccounts_get(with_portfolio=with_portfolio)

Get information about subaccounts

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
with_portfolio = True # bool |  (optional)

try:
    # Get information about subaccounts
    api_response = api_instance.private_get_subaccounts_get(with_portfolio=with_portfolio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_get_subaccounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_portfolio** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_announcement_as_read_get**
> object private_set_announcement_as_read_get(announcement_id)

Marks an announcement as read, so it will not be shown in `get_new_announcements`.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
announcement_id = 3.4 # float | the ID of the announcement

try:
    # Marks an announcement as read, so it will not be shown in `get_new_announcements`.
    api_response = api_instance.private_set_announcement_as_read_get(announcement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_set_announcement_as_read_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **float**| the ID of the announcement | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_email_for_subaccount_get**
> object private_set_email_for_subaccount_get(sid, email)

Assign an email address to a subaccount. User will receive an email with confirmation link.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
email = 'subaccount_1@email.com' # str | The email address for the subaccount

try:
    # Assign an email address to a subaccount. User will receive an email with confirmation link.
    api_response = api_instance.private_set_email_for_subaccount_get(sid, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_set_email_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **email** | **str**| The email address for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_email_language_get**
> object private_set_email_language_get(language)

Changes the language to be used for emails.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
language = 'en' # str | The abbreviated language name. Valid values include `\"en\"`, `\"ko\"`, `\"zh\"`

try:
    # Changes the language to be used for emails.
    api_response = api_instance.private_set_email_language_get(language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_set_email_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| The abbreviated language name. Valid values include &#x60;\&quot;en\&quot;&#x60;, &#x60;\&quot;ko\&quot;&#x60;, &#x60;\&quot;zh\&quot;&#x60; | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_password_for_subaccount_get**
> object private_set_password_for_subaccount_get(sid, password)

Set the password for the subaccount

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
password = 'password_example' # str | The password for the subaccount

try:
    # Set the password for the subaccount
    api_response = api_instance.private_set_password_for_subaccount_get(sid, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_set_password_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **password** | **str**| The password for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_toggle_notifications_from_subaccount_get**
> object private_toggle_notifications_from_subaccount_get(sid, state)

Enable or disable sending of notifications for the subaccount.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
state = True # bool | enable (`true`) or disable (`false`) notifications

try:
    # Enable or disable sending of notifications for the subaccount.
    api_response = api_instance.private_toggle_notifications_from_subaccount_get(sid, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_toggle_notifications_from_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **state** | **bool**| enable (&#x60;true&#x60;) or disable (&#x60;false&#x60;) notifications | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_toggle_subaccount_login_get**
> object private_toggle_subaccount_login_get(sid, state)

Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
state = 'state_example' # str | enable or disable login.

try:
    # Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.
    api_response = api_instance.private_toggle_subaccount_login_get(sid, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->private_toggle_subaccount_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **state** | **str**| enable or disable login. | 

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
api_instance = openapi_client.AccountManagementApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves announcements from the last 30 days.
    api_response = api_instance.public_get_announcements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->public_get_announcements_get: %s\n" % e)
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

