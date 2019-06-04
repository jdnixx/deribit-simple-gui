# openapi_client.AuthenticationApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_logout_get**](AuthenticationApi.md#private_logout_get) | **GET** /private/logout | Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
[**public_auth_get**](AuthenticationApi.md#public_auth_get) | **GET** /public/auth | Authenticate


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
api_instance = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))

try:
    # Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
    api_instance.private_logout_get()
except ApiException as e:
    print("Exception when calling AuthenticationApi->private_logout_get: %s\n" % e)
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
api_instance = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))
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
    print("Exception when calling AuthenticationApi->public_auth_get: %s\n" % e)
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

