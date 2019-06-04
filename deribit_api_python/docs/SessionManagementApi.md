# openapi_client.SessionManagementApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_disable_cancel_on_disconnect_get**](SessionManagementApi.md#private_disable_cancel_on_disconnect_get) | **GET** /private/disable_cancel_on_disconnect | Disable Cancel On Disconnect for the connection. This does not change the default account setting.
[**private_enable_cancel_on_disconnect_get**](SessionManagementApi.md#private_enable_cancel_on_disconnect_get) | **GET** /private/enable_cancel_on_disconnect | Enable Cancel On Disconnect for the connection. This does not change the default account setting.
[**public_disable_heartbeat_get**](SessionManagementApi.md#public_disable_heartbeat_get) | **GET** /public/disable_heartbeat | Stop sending heartbeat messages.
[**public_set_heartbeat_get**](SessionManagementApi.md#public_set_heartbeat_get) | **GET** /public/set_heartbeat | Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send &#x60;heartbeat&#x60; messages and &#x60;test_request&#x60; messages. Your software should respond to &#x60;test_request&#x60; messages by sending a &#x60;/api/v2/public/test&#x60; request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.


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
api_instance = openapi_client.SessionManagementApi(openapi_client.ApiClient(configuration))

try:
    # Disable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_disable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionManagementApi->private_disable_cancel_on_disconnect_get: %s\n" % e)
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
api_instance = openapi_client.SessionManagementApi(openapi_client.ApiClient(configuration))

try:
    # Enable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_enable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionManagementApi->private_enable_cancel_on_disconnect_get: %s\n" % e)
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
api_instance = openapi_client.SessionManagementApi(openapi_client.ApiClient(configuration))

try:
    # Stop sending heartbeat messages.
    api_response = api_instance.public_disable_heartbeat_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionManagementApi->public_disable_heartbeat_get: %s\n" % e)
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
api_instance = openapi_client.SessionManagementApi(openapi_client.ApiClient(configuration))
interval = 60 # float | The heartbeat interval in seconds, but not less than 10

try:
    # Signals the Websocket connection to send and request heartbeats. Heartbeats can be used to detect stale connections. When heartbeats have been set up, the API server will send `heartbeat` messages and `test_request` messages. Your software should respond to `test_request` messages by sending a `/api/v2/public/test` request. If your software fails to do so, the API server will immediately close the connection. If your account is configured to cancel on disconnect, any orders opened over the connection will be cancelled.
    api_response = api_instance.public_set_heartbeat_get(interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionManagementApi->public_set_heartbeat_get: %s\n" % e)
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

