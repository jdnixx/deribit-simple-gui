# coding: utf-8

"""
    Deribit API

    #Overview  Deribit provides three different interfaces to access the API:  * [JSON-RPC over Websocket](#json-rpc) * [JSON-RPC over HTTP](#json-rpc) * [FIX](#fix-api) (Financial Information eXchange)  With the API Console you can use and test the JSON-RPC API, both via HTTP and  via Websocket. To visit the API console, go to __Account > API tab >  API Console tab.__   ##Naming Deribit tradeable assets or instruments use the following system of naming:  |Kind|Examples|Template|Comments| |----|--------|--------|--------| |Future|<code>BTC-25MAR16</code>, <code>BTC-5AUG16</code>|<code>BTC-DMMMYY</code>|<code>BTC</code> is currency, <code>DMMMYY</code> is expiration date, <code>D</code> stands for day of month (1 or 2 digits), <code>MMM</code> - month (3 first letters in English), <code>YY</code> stands for year.| |Perpetual|<code>BTC-PERPETUAL</code>                        ||Perpetual contract for currency <code>BTC</code>.| |Option|<code>BTC-25MAR16-420-C</code>, <code>BTC-5AUG16-580-P</code>|<code>BTC-DMMMYY-STRIKE-K</code>|<code>STRIKE</code> is option strike price in USD. Template <code>K</code> is option kind: <code>C</code> for call options or <code>P</code> for put options.|   # JSON-RPC JSON-RPC is a light-weight remote procedure call (RPC) protocol. The  [JSON-RPC specification](https://www.jsonrpc.org/specification) defines the data structures that are used for the messages that are exchanged between client and server, as well as the rules around their processing. JSON-RPC uses JSON (RFC 4627) as data format.  JSON-RPC is transport agnostic: it does not specify which transport mechanism must be used. The Deribit API supports both Websocket (preferred) and HTTP (with limitations: subscriptions are not supported over HTTP).  ## Request messages > An example of a request message:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 8066,     \"method\": \"public/ticker\",     \"params\": {         \"instrument\": \"BTC-24AUG18-6500-P\"     } } ```  According to the JSON-RPC sepcification the requests must be JSON objects with the following fields.  |Name|Type|Description| |----|----|-----------| |jsonrpc|string|The version of the JSON-RPC spec: \"2.0\"| |id|integer or string|An identifier of the request. If it is included, then the response will contain the same identifier| |method|string|The method to be invoked| |params|object|The parameters values for the method. The field names must match with the expected parameter names. The parameters that are expected are described in the documentation for the methods, below.|  <aside class=\"warning\"> The JSON-RPC specification describes two features that are currently not supported by the API:  <ul> <li>Specification of parameter values by position</li> <li>Batch requests</li> </ul>  </aside>   ## Response messages > An example of a response message:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 5239,     \"testnet\": false,     \"result\": [         {             \"currency\": \"BTC\",             \"currencyLong\": \"Bitcoin\",             \"minConfirmation\": 2,             \"txFee\": 0.0006,             \"isActive\": true,             \"coinType\": \"BITCOIN\",             \"baseAddress\": null         }     ],     \"usIn\": 1535043730126248,     \"usOut\": 1535043730126250,     \"usDiff\": 2 } ```  The JSON-RPC API always responds with a JSON object with the following fields.   |Name|Type|Description| |----|----|-----------| |id|integer|This is the same id that was sent in the request.| |result|any|If successful, the result of the API call. The format for the result is described with each method.| |error|error object|Only present if there was an error invoking the method. The error object is described below.| |testnet|boolean|Indicates whether the API in use is actually the test API.  <code>false</code> for production server, <code>true</code> for test server.| |usIn|integer|The timestamp when the requests was received (microseconds since the Unix epoch)| |usOut|integer|The timestamp when the response was sent (microseconds since the Unix epoch)| |usDiff|integer|The number of microseconds that was spent handling the request|  <aside class=\"notice\"> The fields <code>testnet</code>, <code>usIn</code>, <code>usOut</code> and <code>usDiff</code> are not part of the JSON-RPC standard.  <p>In order not to clutter the examples they will generally be omitted from the example code.</p> </aside>  > An example of a response with an error:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 8163,     \"error\": {         \"code\": 11050,         \"message\": \"bad_request\"     },     \"testnet\": false,     \"usIn\": 1535037392434763,     \"usOut\": 1535037392448119,     \"usDiff\": 13356 } ``` In case of an error the response message will contain the error field, with as value an object with the following with the following fields:  |Name|Type|Description |----|----|-----------| |code|integer|A number that indicates the kind of error.| |message|string|A short description that indicates the kind of error.| |data|any|Additional data about the error. This field may be omitted.|  ## Notifications  > An example of a notification:  ```json {     \"jsonrpc\": \"2.0\",     \"method\": \"subscription\",     \"params\": {         \"channel\": \"deribit_price_index.btc_usd\",         \"data\": {             \"timestamp\": 1535098298227,             \"price\": 6521.17,             \"index_name\": \"btc_usd\"         }     } } ```  API users can subscribe to certain types of notifications. This means that they will receive JSON-RPC notification-messages from the server when certain events occur, such as changes to the index price or changes to the order book for a certain instrument.   The API methods [public/subscribe](#public-subscribe) and [private/subscribe](#private-subscribe) are used to set up a subscription. Since HTTP does not support the sending of messages from server to client, these methods are only availble when using the Websocket transport mechanism.  At the moment of subscription a \"channel\" must be specified. The channel determines the type of events that will be received.  See [Subscriptions](#subscriptions) for more details about the channels.  In accordance with the JSON-RPC specification, the format of a notification  is that of a request message without an <code>id</code> field. The value of the <code>method</code> field will always be <code>\"subscription\"</code>. The <code>params</code> field will always be an object with 2 members: <code>channel</code> and <code>data</code>. The value of the <code>channel</code> member is the name of the channel (a string). The value of the <code>data</code> member is an object that contains data  that is specific for the channel.   ## Authentication  > An example of a JSON request with token:  ```json {     \"id\": 5647,     \"method\": \"private/get_subaccounts\",     \"params\": {         \"access_token\": \"67SVutDoVZSzkUStHSuk51WntMNBJ5mh5DYZhwzpiqDF\"     } } ```  The API consists of `public` and `private` methods. The public methods do not require authentication. The private methods use OAuth 2.0 authentication. This means that a valid OAuth access token must be included in the request, which can get achived by calling method [public/auth](#public-auth).  When the token was assigned to the user, it should be passed along, with other request parameters, back to the server:  |Connection type|Access token placement |----|-----------| |**Websocket**|Inside request JSON parameters, as an `access_token` field| |**HTTP (REST)**|Header `Authorization: bearer ```Token``` ` value|  ### Additional authorization method - basic user credentials  <span style=\"color:red\"><b> ! Not recommended - however, it could be useful for quick testing API</b></span></br>  Every `private` method could be accessed by providing, inside HTTP `Authorization: Basic XXX` header, values with user `ClientId` and assigned `ClientSecret` (both values can be found on the API page on the Deribit website) encoded with `Base64`:  <code>Authorization: Basic BASE64(`ClientId` + `:` + `ClientSecret`)</code>   ### Additional authorization method - Deribit signature credentials  The Derbit service provides dedicated authorization method, which harness user generated signature to increase security level for passing request data. Generated value is passed inside `Authorization` header, coded as:  <code>Authorization: deri-hmac-sha256 id=```ClientId```,ts=```Timestamp```,sig=```Signature```,nonce=```Nonce```</code>  where:  |Deribit credential|Description |----|-----------| |*ClientId*|Can be found on the API page on the Deribit website| |*Timestamp*|Time when the request was generated - given as **miliseconds**. It's valid for **60 seconds** since generation, after that time any request with an old timestamp will be rejected.| |*Signature*|Value for signature calculated as described below | |*Nonce*|Single usage, user generated initialization vector for the server token|  The signature is generated by the following formula:  <code> Signature = HEX_STRING( HMAC-SHA256( ClientSecret, StringToSign ) );</code></br>  <code> StringToSign =  Timestamp + \"\\n\" + Nonce + \"\\n\" + RequestData;</code></br>  <code> RequestData =  UPPERCASE(HTTP_METHOD())  + \"\\n\" + URI() + \"\\n\" + RequestBody + \"\\n\";</code></br>   e.g. (using shell with ```openssl``` tool):  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientId=AAAAAAAAAAA</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientSecret=ABCD</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Timestamp=$( date +%s000 )</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Nonce=$( cat /dev/urandom | tr -dc 'a-z0-9' | head -c8 )</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;URI=\"/api/v2/private/get_account_summary?currency=BTC\"</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;HttpMethod=GET</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Body=\"\"</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Signature=$( echo -ne \"${Timestamp}\\n${Nonce}\\n${HttpMethod}\\n${URI}\\n${Body}\\n\" | openssl sha256 -r -hmac \"$ClientSecret\" | cut -f1 -d' ' )</code></br></br> <code>&nbsp;&nbsp;&nbsp;&nbsp;echo $Signature</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;shell output> ea40d5e5e4fae235ab22b61da98121fbf4acdc06db03d632e23c66bcccb90d2c  (**WARNING**: Exact value depends on current timestamp and client credentials</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;curl -s -X ${HttpMethod} -H \"Authorization: deri-hmac-sha256 id=${ClientId},ts=${Timestamp},nonce=${Nonce},sig=${Signature}\" \"https://www.deribit.com${URI}\"</code></br></br>    ### Additional authorization method - signature credentials (WebSocket API)  When connecting through Websocket, user can request for authorization using ```client_credential``` method, which requires providing following parameters (as a part of JSON request):  |JSON parameter|Description |----|-----------| |*grant_type*|Must be **client_signature**| |*client_id*|Can be found on the API page on the Deribit website| |*timestamp*|Time when the request was generated - given as **miliseconds**. It's valid for **60 seconds** since generation, after that time any request with an old timestamp will be rejected.| |*signature*|Value for signature calculated as described below | |*nonce*|Single usage, user generated initialization vector for the server token| |*data*|**Optional** field, which contains any user specific value|  The signature is generated by the following formula:  <code> StringToSign =  Timestamp + \"\\n\" + Nonce + \"\\n\" + Data;</code></br>  <code> Signature = HEX_STRING( HMAC-SHA256( ClientSecret, StringToSign ) );</code></br>   e.g. (using shell with ```openssl``` tool):  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientId=AAAAAAAAAAA</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientSecret=ABCD</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Timestamp=$( date +%s000 ) # e.g. 1554883365000 </code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Nonce=$( cat /dev/urandom | tr -dc 'a-z0-9' | head -c8 ) # e.g. fdbmmz79 </code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Data=\"\"</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Signature=$( echo -ne \"${Timestamp}\\n${Nonce}\\n${Data}\\n\" | openssl sha256 -r -hmac \"$ClientSecret\" | cut -f1 -d' ' )</code></br></br> <code>&nbsp;&nbsp;&nbsp;&nbsp;echo $Signature</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;shell output> e20c9cd5639d41f8bbc88f4d699c4baf94a4f0ee320e9a116b72743c449eb994  (**WARNING**: Exact value depends on current timestamp and client credentials</code></br></br>   You can also check the signature value using some online tools like, e.g: [https://codebeautify.org/hmac-generator](https://codebeautify.org/hmac-generator) (but don't forget about adding *newline* after each part of the hashed text and remember that you **should use** it only with your **test credentials**).   Here's a sample JSON request created using the values from the example above:  <code> {                            </br> &nbsp;&nbsp;\"jsonrpc\" : \"2.0\",         </br> &nbsp;&nbsp;\"id\" : 9929,               </br> &nbsp;&nbsp;\"method\" : \"public/auth\",  </br> &nbsp;&nbsp;\"params\" :                 </br> &nbsp;&nbsp;{                        </br> &nbsp;&nbsp;&nbsp;&nbsp;\"grant_type\" : \"client_signature\",   </br> &nbsp;&nbsp;&nbsp;&nbsp;\"client_id\" : \"AAAAAAAAAAA\",         </br> &nbsp;&nbsp;&nbsp;&nbsp;\"timestamp\": \"1554883365000\",        </br> &nbsp;&nbsp;&nbsp;&nbsp;\"nonce\": \"fdbmmz79\",                 </br> &nbsp;&nbsp;&nbsp;&nbsp;\"data\": \"\",                          </br> &nbsp;&nbsp;&nbsp;&nbsp;\"signature\" : \"e20c9cd5639d41f8bbc88f4d699c4baf94a4f0ee320e9a116b72743c449eb994\"  </br> &nbsp;&nbsp;}                        </br> }                            </br> </code>   ### Access scope  When asking for `access token` user can provide the required access level (called `scope`) which defines what type of functionality he/she wants to use, and whether requests are only going to check for some data or also to update them.  Scopes are required and checked for `private` methods, so if you plan to use only `public` information you can stay with values assigned by default.  |Scope|Description |----|-----------| |*account:read*|Access to **account** methods - read only data| |*account:read_write*|Access to **account** methods - allows to manage account settings, add subaccounts, etc.| |*trade:read*|Access to **trade** methods - read only data| |*trade:read_write*|Access to **trade** methods - required to create and modify orders| |*wallet:read*|Access to **wallet** methods - read only data| |*wallet:read_write*|Access to **wallet** methods - allows to withdraw, generate new deposit address, etc.| |*wallet:none*, *account:none*, *trade:none*|Blocked access to specified functionality|    <span style=\"color:red\">**NOTICE:**</span> Depending on choosing an authentication method (```grant type```) some scopes could be narrowed by the server. e.g. when ```grant_type = client_credentials``` and ```scope = wallet:read_write``` it's modified by the server as ```scope = wallet:read```\"   ## JSON-RPC over websocket Websocket is the prefered transport mechanism for the JSON-RPC API, because it is faster and because it can support [subscriptions](#subscriptions) and [cancel on disconnect](#private-enable_cancel_on_disconnect). The code examples that can be found next to each of the methods show how websockets can be used from Python or Javascript/node.js.  ## JSON-RPC over HTTP Besides websockets it is also possible to use the API via HTTP. The code examples for 'shell' show how this can be done using curl. Note that subscriptions and cancel on disconnect are not supported via HTTP.  #Methods   # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class InternalApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def private_add_to_address_book_get(self, currency, type, address, name, **kwargs):  # noqa: E501
        """Adds new entry to address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_add_to_address_book_get(currency, type, address, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :param str address: Address in currency format, it must be in address book (required)
        :param str name: Name of address book entry (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_add_to_address_book_get_with_http_info(currency, type, address, name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_add_to_address_book_get_with_http_info(currency, type, address, name, **kwargs)  # noqa: E501
            return data

    def private_add_to_address_book_get_with_http_info(self, currency, type, address, name, **kwargs):  # noqa: E501
        """Adds new entry to address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_add_to_address_book_get_with_http_info(currency, type, address, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :param str address: Address in currency format, it must be in address book (required)
        :param str name: Name of address book entry (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'type', 'address', 'name', 'tfa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_add_to_address_book_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_add_to_address_book_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `private_add_to_address_book_get`")  # noqa: E501
        # verify the required parameter 'address' is set
        if ('address' not in local_var_params or
                local_var_params['address'] is None):
            raise ApiValueError("Missing the required parameter `address` when calling `private_add_to_address_book_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ApiValueError("Missing the required parameter `name` when calling `private_add_to_address_book_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))  # noqa: E501
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'tfa' in local_var_params:
            query_params.append(('tfa', local_var_params['tfa']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/add_to_address_book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_disable_tfa_with_recovery_code_get(self, password, code, **kwargs):  # noqa: E501
        """Disables TFA with one time recovery code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_disable_tfa_with_recovery_code_get(password, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str password: The password for the subaccount (required)
        :param str code: One time recovery code (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_disable_tfa_with_recovery_code_get_with_http_info(password, code, **kwargs)  # noqa: E501
        else:
            (data) = self.private_disable_tfa_with_recovery_code_get_with_http_info(password, code, **kwargs)  # noqa: E501
            return data

    def private_disable_tfa_with_recovery_code_get_with_http_info(self, password, code, **kwargs):  # noqa: E501
        """Disables TFA with one time recovery code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_disable_tfa_with_recovery_code_get_with_http_info(password, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str password: The password for the subaccount (required)
        :param str code: One time recovery code (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['password', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_disable_tfa_with_recovery_code_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ApiValueError("Missing the required parameter `password` when calling `private_disable_tfa_with_recovery_code_get`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `private_disable_tfa_with_recovery_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/disable_tfa_with_recovery_code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_get_address_book_get(self, currency, type, **kwargs):  # noqa: E501
        """Retrieves address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_address_book_get(currency, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_address_book_get_with_http_info(currency, type, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_address_book_get_with_http_info(currency, type, **kwargs)  # noqa: E501
            return data

    def private_get_address_book_get_with_http_info(self, currency, type, **kwargs):  # noqa: E501
        """Retrieves address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_address_book_get_with_http_info(currency, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_address_book_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_address_book_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `private_get_address_book_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/get_address_book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_remove_from_address_book_get(self, currency, type, address, **kwargs):  # noqa: E501
        """Adds new entry to address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_remove_from_address_book_get(currency, type, address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :param str address: Address in currency format, it must be in address book (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_remove_from_address_book_get_with_http_info(currency, type, address, **kwargs)  # noqa: E501
        else:
            (data) = self.private_remove_from_address_book_get_with_http_info(currency, type, address, **kwargs)  # noqa: E501
            return data

    def private_remove_from_address_book_get_with_http_info(self, currency, type, address, **kwargs):  # noqa: E501
        """Adds new entry to address book of given type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_remove_from_address_book_get_with_http_info(currency, type, address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Address book type (required)
        :param str address: Address in currency format, it must be in address book (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'type', 'address', 'tfa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_remove_from_address_book_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_remove_from_address_book_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `private_remove_from_address_book_get`")  # noqa: E501
        # verify the required parameter 'address' is set
        if ('address' not in local_var_params or
                local_var_params['address'] is None):
            raise ApiValueError("Missing the required parameter `address` when calling `private_remove_from_address_book_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))  # noqa: E501
        if 'tfa' in local_var_params:
            query_params.append(('tfa', local_var_params['tfa']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/remove_from_address_book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_submit_transfer_to_subaccount_get(self, currency, amount, destination, **kwargs):  # noqa: E501
        """Transfer funds to a subaccount.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_submit_transfer_to_subaccount_get(currency, amount, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param float amount: Amount of funds to be transferred (required)
        :param int destination: Id of destination subaccount (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_submit_transfer_to_subaccount_get_with_http_info(currency, amount, destination, **kwargs)  # noqa: E501
        else:
            (data) = self.private_submit_transfer_to_subaccount_get_with_http_info(currency, amount, destination, **kwargs)  # noqa: E501
            return data

    def private_submit_transfer_to_subaccount_get_with_http_info(self, currency, amount, destination, **kwargs):  # noqa: E501
        """Transfer funds to a subaccount.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_submit_transfer_to_subaccount_get_with_http_info(currency, amount, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param float amount: Amount of funds to be transferred (required)
        :param int destination: Id of destination subaccount (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'amount', 'destination']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_submit_transfer_to_subaccount_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_submit_transfer_to_subaccount_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_submit_transfer_to_subaccount_get`")  # noqa: E501
        # verify the required parameter 'destination' is set
        if ('destination' not in local_var_params or
                local_var_params['destination'] is None):
            raise ApiValueError("Missing the required parameter `destination` when calling `private_submit_transfer_to_subaccount_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/submit_transfer_to_subaccount', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_submit_transfer_to_user_get(self, currency, amount, destination, **kwargs):  # noqa: E501
        """Transfer funds to a another user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_submit_transfer_to_user_get(currency, amount, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param float amount: Amount of funds to be transferred (required)
        :param str destination: Destination address from address book (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_submit_transfer_to_user_get_with_http_info(currency, amount, destination, **kwargs)  # noqa: E501
        else:
            (data) = self.private_submit_transfer_to_user_get_with_http_info(currency, amount, destination, **kwargs)  # noqa: E501
            return data

    def private_submit_transfer_to_user_get_with_http_info(self, currency, amount, destination, **kwargs):  # noqa: E501
        """Transfer funds to a another user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_submit_transfer_to_user_get_with_http_info(currency, amount, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param float amount: Amount of funds to be transferred (required)
        :param str destination: Destination address from address book (required)
        :param str tfa: TFA code, required when TFA is enabled for current account
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'amount', 'destination', 'tfa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_submit_transfer_to_user_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_submit_transfer_to_user_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_submit_transfer_to_user_get`")  # noqa: E501
        # verify the required parameter 'destination' is set
        if ('destination' not in local_var_params or
                local_var_params['destination'] is None):
            raise ApiValueError("Missing the required parameter `destination` when calling `private_submit_transfer_to_user_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))  # noqa: E501
        if 'tfa' in local_var_params:
            query_params.append(('tfa', local_var_params['tfa']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/submit_transfer_to_user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_toggle_deposit_address_creation_get(self, currency, state, **kwargs):  # noqa: E501
        """Enable or disable deposit address creation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_toggle_deposit_address_creation_get(currency, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param bool state: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_toggle_deposit_address_creation_get_with_http_info(currency, state, **kwargs)  # noqa: E501
        else:
            (data) = self.private_toggle_deposit_address_creation_get_with_http_info(currency, state, **kwargs)  # noqa: E501
            return data

    def private_toggle_deposit_address_creation_get_with_http_info(self, currency, state, **kwargs):  # noqa: E501
        """Enable or disable deposit address creation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_toggle_deposit_address_creation_get_with_http_info(currency, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param bool state: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_toggle_deposit_address_creation_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_toggle_deposit_address_creation_get`")  # noqa: E501
        # verify the required parameter 'state' is set
        if ('state' not in local_var_params or
                local_var_params['state'] is None):
            raise ApiValueError("Missing the required parameter `state` when calling `private_toggle_deposit_address_creation_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/private/toggle_deposit_address_creation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_get_footer_get(self, **kwargs):  # noqa: E501
        """Get information to be displayed in the footer of the website.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_get_footer_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.public_get_footer_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.public_get_footer_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def public_get_footer_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get information to be displayed in the footer of the website.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_get_footer_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method public_get_footer_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/public/get_footer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_get_option_mark_prices_get(self, currency, **kwargs):  # noqa: E501
        """Retrives market prices and its implied volatility of options instruments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_get_option_mark_prices_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.public_get_option_mark_prices_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.public_get_option_mark_prices_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def public_get_option_mark_prices_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Retrives market prices and its implied volatility of options instruments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_get_option_mark_prices_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method public_get_option_mark_prices_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `public_get_option_mark_prices_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/public/get_option_mark_prices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_validate_field_get(self, field, value, **kwargs):  # noqa: E501
        """Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_validate_field_get(field, value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: Name of the field to be validated, examples: postal_code, date_of_birth (required)
        :param str value: Value to be checked (required)
        :param str value2: Additional value to be compared with
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.public_validate_field_get_with_http_info(field, value, **kwargs)  # noqa: E501
        else:
            (data) = self.public_validate_field_get_with_http_info(field, value, **kwargs)  # noqa: E501
            return data

    def public_validate_field_get_with_http_info(self, field, value, **kwargs):  # noqa: E501
        """Method used to introduce the client software connected to Deribit platform over websocket. Provided data may have an impact on the maintained connection and will be collected for internal statistical purposes. In response, Deribit will also introduce itself.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_validate_field_get_with_http_info(field, value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: Name of the field to be validated, examples: postal_code, date_of_birth (required)
        :param str value: Value to be checked (required)
        :param str value2: Additional value to be compared with
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['field', 'value', 'value2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method public_validate_field_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in local_var_params or
                local_var_params['field'] is None):
            raise ApiValueError("Missing the required parameter `field` when calling `public_validate_field_get`")  # noqa: E501
        # verify the required parameter 'value' is set
        if ('value' not in local_var_params or
                local_var_params['value'] is None):
            raise ApiValueError("Missing the required parameter `value` when calling `public_validate_field_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'field' in local_var_params:
            query_params.append(('field', local_var_params['field']))  # noqa: E501
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))  # noqa: E501
        if 'value2' in local_var_params:
            query_params.append(('value2', local_var_params['value2']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/public/validate_field', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
