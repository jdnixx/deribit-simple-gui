# openapi_client.SubscriptionManagementApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_subscribe_get**](SubscriptionManagementApi.md#private_subscribe_get) | **GET** /private/subscribe | Subscribe to one or more channels.
[**private_unsubscribe_get**](SubscriptionManagementApi.md#private_unsubscribe_get) | **GET** /private/unsubscribe | Unsubscribe from one or more channels.
[**public_subscribe_get**](SubscriptionManagementApi.md#public_subscribe_get) | **GET** /public/subscribe | Subscribe to one or more channels.
[**public_unsubscribe_get**](SubscriptionManagementApi.md#public_unsubscribe_get) | **GET** /public/unsubscribe | Unsubscribe from one or more channels.


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
api_instance = openapi_client.SubscriptionManagementApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.private_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionManagementApi->private_subscribe_get: %s\n" % e)
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
api_instance = openapi_client.SubscriptionManagementApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to unsubscribe from.

try:
    # Unsubscribe from one or more channels.
    api_response = api_instance.private_unsubscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionManagementApi->private_unsubscribe_get: %s\n" % e)
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
api_instance = openapi_client.SubscriptionManagementApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.public_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionManagementApi->public_subscribe_get: %s\n" % e)
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
api_instance = openapi_client.SubscriptionManagementApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to unsubscribe from.

try:
    # Unsubscribe from one or more channels.
    api_response = api_instance.public_unsubscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionManagementApi->public_unsubscribe_get: %s\n" % e)
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

