# openapi_client.WebsocketOnlyApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_disable_cancel_on_disconnect_get**](WebsocketOnlyApi.md#private_disable_cancel_on_disconnect_get) | **GET** /private/disable_cancel_on_disconnect | Disable Cancel On Disconnect for the connection. This does not change the default account setting.
[**private_enable_cancel_on_disconnect_get**](WebsocketOnlyApi.md#private_enable_cancel_on_disconnect_get) | **GET** /private/enable_cancel_on_disconnect | Enable Cancel On Disconnect for the connection. This does not change the default account setting.
[**private_logout_get**](WebsocketOnlyApi.md#private_logout_get) | **GET** /private/logout | Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
[**private_subscribe_get**](WebsocketOnlyApi.md#private_subscribe_get) | **GET** /private/subscribe | Subscribe to one or more channels.
[**private_unsubscribe_get**](WebsocketOnlyApi.md#private_unsubscribe_get) | **GET** /private/unsubscribe | Unsubscribe from one or more channels.
[**public_disable_heartbeat_get**](WebsocketOnlyApi.md#public_disable_heartbeat_get) | **GET** /public/disable_heartbeat | Stop sending heartbeat messages.
[**public_hello_get**](WebsocketOnlyApi.md#public_hello_get) | **GET** /public/hello | Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
[**public_set_heartbeat_get**](WebsocketOnlyApi.md#public_set_heartbeat_get) | **GET** /public/set_heartbeat | Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send &#x60;heartbeat&#x60; messages and &#x60;test_request&#x60; messages. Your software should respond to &#x60;test_request&#x60; messages by sending a &#x60;/api/v2/public/test&#x60; request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.
[**public_subscribe_get**](WebsocketOnlyApi.md#public_subscribe_get) | **GET** /public/subscribe | Subscribe to one or more channels.
[**public_unsubscribe_get**](WebsocketOnlyApi.md#public_unsubscribe_get) | **GET** /public/unsubscribe | Unsubscribe from one or more channels.


# **private_disable_cancel_on_disconnect_get**
> object private_disable_cancel_on_disconnect_get()

Disable Cancel On Disconnect for the connection. This does not change the default account setting.

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))

try:
    # Disable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_disable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->private_disable_cancel_on_disconnect_get: %s\n" % e)
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

# **private_enable_cancel_on_disconnect_get**
> object private_enable_cancel_on_disconnect_get()

Enable Cancel On Disconnect for the connection. This does not change the default account setting.

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))

try:
    # Enable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_enable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->private_enable_cancel_on_disconnect_get: %s\n" % e)
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

# **private_logout_get**
> private_logout_get()

Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))

try:
    # Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
    api_instance.private_logout_get()
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->private_logout_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_subscribe_get**
> object private_subscribe_get(channels)

Subscribe to one or more channels.

Subscribe to one or more channels.  The name of the channel determines what information will be provided, and in what form. 

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.private_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->private_subscribe_get: %s\n" % e)
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

# **private_unsubscribe_get**
> object private_unsubscribe_get(channels)

Unsubscribe from one or more channels.

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to unsubscribe from.

try:
    # Unsubscribe from one or more channels.
    api_response = api_instance.private_unsubscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->private_unsubscribe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channels** | [**list[str]**](str.md)| A list of channels to unsubscribe from. | 

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))

try:
    # Stop sending heartbeat messages.
    api_response = api_instance.public_disable_heartbeat_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->public_disable_heartbeat_get: %s\n" % e)
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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
client_name = 'My Trading Software' # str | Client software name
client_version = '1.0.2' # str | Client software version

try:
    # Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.
    api_response = api_instance.public_hello_get(client_name, client_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->public_hello_get: %s\n" % e)
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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
interval = 60 # float | The heartbeat interval in seconds, but not less than 10

try:
    # Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send `heartbeat` messages and `test_request` messages. Your software should respond to `test_request` messages by sending a `/api/v2/public/test` request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.
    api_response = api_instance.public_set_heartbeat_get(interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->public_set_heartbeat_get: %s\n" % e)
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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.public_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->public_subscribe_get: %s\n" % e)
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

# **public_unsubscribe_get**
> object public_unsubscribe_get(channels)

Unsubscribe from one or more channels.

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
api_instance = openapi_client.WebsocketOnlyApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to unsubscribe from.

try:
    # Unsubscribe from one or more channels.
    api_response = api_instance.public_unsubscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsocketOnlyApi->public_unsubscribe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channels** | [**list[str]**](str.md)| A list of channels to unsubscribe from. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

