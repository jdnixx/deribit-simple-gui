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


class TradingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def private_buy_get(self, instrument_name, amount, **kwargs):  # noqa: E501
        """Places a buy order for an instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_buy_get(instrument_name, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param str type: The order type, default: `\"limit\"`
        :param str label: user defined label for the order (maximum 32 characters)
        :param float price: <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p>
        :param str time_in_force: <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul>
        :param float max_show: Maximum amount within an order to be shown to other customers, `0` for invisible order
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param bool reduce_only: If `true`, the order is considered reduce-only which is intended to only reduce a current position
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :param str trigger: Defines trigger type, required for `\"stop_limit\"` order type
        :param str advanced: Advanced option order type. (Only for options)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_buy_get_with_http_info(instrument_name, amount, **kwargs)  # noqa: E501
        else:
            (data) = self.private_buy_get_with_http_info(instrument_name, amount, **kwargs)  # noqa: E501
            return data

    def private_buy_get_with_http_info(self, instrument_name, amount, **kwargs):  # noqa: E501
        """Places a buy order for an instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_buy_get_with_http_info(instrument_name, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param str type: The order type, default: `\"limit\"`
        :param str label: user defined label for the order (maximum 32 characters)
        :param float price: <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p>
        :param str time_in_force: <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul>
        :param float max_show: Maximum amount within an order to be shown to other customers, `0` for invisible order
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param bool reduce_only: If `true`, the order is considered reduce-only which is intended to only reduce a current position
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :param str trigger: Defines trigger type, required for `\"stop_limit\"` order type
        :param str advanced: Advanced option order type. (Only for options)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'amount', 'type', 'label', 'price', 'time_in_force', 'max_show', 'post_only', 'reduce_only', 'stop_price', 'trigger', 'advanced']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_buy_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_buy_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_buy_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))  # noqa: E501
        if 'price' in local_var_params:
            query_params.append(('price', local_var_params['price']))  # noqa: E501
        if 'time_in_force' in local_var_params:
            query_params.append(('time_in_force', local_var_params['time_in_force']))  # noqa: E501
        if 'max_show' in local_var_params:
            query_params.append(('max_show', local_var_params['max_show']))  # noqa: E501
        if 'post_only' in local_var_params:
            query_params.append(('post_only', local_var_params['post_only']))  # noqa: E501
        if 'reduce_only' in local_var_params:
            query_params.append(('reduce_only', local_var_params['reduce_only']))  # noqa: E501
        if 'stop_price' in local_var_params:
            query_params.append(('stop_price', local_var_params['stop_price']))  # noqa: E501
        if 'trigger' in local_var_params:
            query_params.append(('trigger', local_var_params['trigger']))  # noqa: E501
        if 'advanced' in local_var_params:
            query_params.append(('advanced', local_var_params['advanced']))  # noqa: E501

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
            '/private/buy', 'GET',
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

    def private_cancel_all_by_currency_get(self, currency, **kwargs):  # noqa: E501
        """Cancels all orders by currency, optionally filtered by instrument kind and/or order type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_by_currency_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str type: Order type - limit, stop or all, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_cancel_all_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.private_cancel_all_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def private_cancel_all_by_currency_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Cancels all orders by currency, optionally filtered by instrument kind and/or order type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_by_currency_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str type: Order type - limit, stop or all, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'kind', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_cancel_all_by_currency_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_cancel_all_by_currency_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
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
            '/private/cancel_all_by_currency', 'GET',
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

    def private_cancel_all_by_instrument_get(self, instrument_name, **kwargs):  # noqa: E501
        """Cancels all orders by instrument, optionally filtered by order type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_by_instrument_get(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Order type - limit, stop or all, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_cancel_all_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_cancel_all_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
            return data

    def private_cancel_all_by_instrument_get_with_http_info(self, instrument_name, **kwargs):  # noqa: E501
        """Cancels all orders by instrument, optionally filtered by order type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_by_instrument_get_with_http_info(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Order type - limit, stop or all, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_cancel_all_by_instrument_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_cancel_all_by_instrument_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
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
            '/private/cancel_all_by_instrument', 'GET',
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

    def private_cancel_all_get(self, **kwargs):  # noqa: E501
        """This method cancels all users orders and stop orders within all currencies and instrument kinds.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_cancel_all_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.private_cancel_all_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def private_cancel_all_get_with_http_info(self, **kwargs):  # noqa: E501
        """This method cancels all users orders and stop orders within all currencies and instrument kinds.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_all_get_with_http_info(async_req=True)
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
                    " to method private_cancel_all_get" % key
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
            '/private/cancel_all', 'GET',
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

    def private_cancel_get(self, order_id, **kwargs):  # noqa: E501
        """Cancel an order, specified by order id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_get(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_cancel_get_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.private_cancel_get_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def private_cancel_get_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Cancel an order, specified by order id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_cancel_get_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_cancel_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in local_var_params or
                local_var_params['order_id'] is None):
            raise ApiValueError("Missing the required parameter `order_id` when calling `private_cancel_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))  # noqa: E501

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
            '/private/cancel', 'GET',
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

    def private_close_position_get(self, instrument_name, type, **kwargs):  # noqa: E501
        """Makes closing position reduce only order .  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_close_position_get(instrument_name, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: The order type (required)
        :param float price: Optional price for limit order.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_close_position_get_with_http_info(instrument_name, type, **kwargs)  # noqa: E501
        else:
            (data) = self.private_close_position_get_with_http_info(instrument_name, type, **kwargs)  # noqa: E501
            return data

    def private_close_position_get_with_http_info(self, instrument_name, type, **kwargs):  # noqa: E501
        """Makes closing position reduce only order .  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_close_position_get_with_http_info(instrument_name, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: The order type (required)
        :param float price: Optional price for limit order.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'type', 'price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_close_position_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_close_position_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ApiValueError("Missing the required parameter `type` when calling `private_close_position_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'price' in local_var_params:
            query_params.append(('price', local_var_params['price']))  # noqa: E501

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
            '/private/close_position', 'GET',
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

    def private_edit_get(self, order_id, amount, price, **kwargs):  # noqa: E501
        """Change price, amount and/or other properties of an order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_edit_get(order_id, amount, price, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param float price: <p>The order price in base currency.</p> <p>When editing an option order with advanced=usd, the field price should be the option price value in USD.</p> <p>When editing an option order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p> (required)
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param str advanced: Advanced option order type. If you have posted an advanced option order, it is necessary to re-supply this parameter when editing it (Only for options)
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_edit_get_with_http_info(order_id, amount, price, **kwargs)  # noqa: E501
        else:
            (data) = self.private_edit_get_with_http_info(order_id, amount, price, **kwargs)  # noqa: E501
            return data

    def private_edit_get_with_http_info(self, order_id, amount, price, **kwargs):  # noqa: E501
        """Change price, amount and/or other properties of an order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_edit_get_with_http_info(order_id, amount, price, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param float price: <p>The order price in base currency.</p> <p>When editing an option order with advanced=usd, the field price should be the option price value in USD.</p> <p>When editing an option order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p> (required)
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param str advanced: Advanced option order type. If you have posted an advanced option order, it is necessary to re-supply this parameter when editing it (Only for options)
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['order_id', 'amount', 'price', 'post_only', 'advanced', 'stop_price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_edit_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in local_var_params or
                local_var_params['order_id'] is None):
            raise ApiValueError("Missing the required parameter `order_id` when calling `private_edit_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_edit_get`")  # noqa: E501
        # verify the required parameter 'price' is set
        if ('price' not in local_var_params or
                local_var_params['price'] is None):
            raise ApiValueError("Missing the required parameter `price` when calling `private_edit_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'price' in local_var_params:
            query_params.append(('price', local_var_params['price']))  # noqa: E501
        if 'post_only' in local_var_params:
            query_params.append(('post_only', local_var_params['post_only']))  # noqa: E501
        if 'advanced' in local_var_params:
            query_params.append(('advanced', local_var_params['advanced']))  # noqa: E501
        if 'stop_price' in local_var_params:
            query_params.append(('stop_price', local_var_params['stop_price']))  # noqa: E501

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
            '/private/edit', 'GET',
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

    def private_get_margins_get(self, instrument_name, amount, price, **kwargs):  # noqa: E501
        """Get margins for given instrument, amount and price.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_margins_get(instrument_name, amount, price, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: Amount, integer for future, float for option. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. (required)
        :param float price: Price (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_margins_get_with_http_info(instrument_name, amount, price, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_margins_get_with_http_info(instrument_name, amount, price, **kwargs)  # noqa: E501
            return data

    def private_get_margins_get_with_http_info(self, instrument_name, amount, price, **kwargs):  # noqa: E501
        """Get margins for given instrument, amount and price.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_margins_get_with_http_info(instrument_name, amount, price, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: Amount, integer for future, float for option. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. (required)
        :param float price: Price (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'amount', 'price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_margins_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_margins_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_get_margins_get`")  # noqa: E501
        # verify the required parameter 'price' is set
        if ('price' not in local_var_params or
                local_var_params['price'] is None):
            raise ApiValueError("Missing the required parameter `price` when calling `private_get_margins_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'price' in local_var_params:
            query_params.append(('price', local_var_params['price']))  # noqa: E501

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
            '/private/get_margins', 'GET',
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

    def private_get_open_orders_by_currency_get(self, currency, **kwargs):  # noqa: E501
        """Retrieves list of user's open orders.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_open_orders_by_currency_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str type: Order type, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_open_orders_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_open_orders_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def private_get_open_orders_by_currency_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Retrieves list of user's open orders.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_open_orders_by_currency_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str type: Order type, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'kind', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_open_orders_by_currency_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_open_orders_by_currency_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
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
            '/private/get_open_orders_by_currency', 'GET',
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

    def private_get_open_orders_by_instrument_get(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves list of user's open orders within given Instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_open_orders_by_instrument_get(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Order type, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_open_orders_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_open_orders_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
            return data

    def private_get_open_orders_by_instrument_get_with_http_info(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves list of user's open orders within given Instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_open_orders_by_instrument_get_with_http_info(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Order type, default - `all`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_open_orders_by_instrument_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_open_orders_by_instrument_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
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
            '/private/get_open_orders_by_instrument', 'GET',
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

    def private_get_order_history_by_currency_get(self, currency, **kwargs):  # noqa: E501
        """Retrieves history of orders that have been partially or fully filled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_history_by_currency_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param int count: Number of requested items, default - `20`
        :param int offset: The offset for pagination, default - `0`
        :param bool include_old: Include in result orders older than 2 days, default - `false`
        :param bool include_unfilled: Include in result fully unfilled closed orders, default - `false`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_order_history_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_order_history_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def private_get_order_history_by_currency_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Retrieves history of orders that have been partially or fully filled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_history_by_currency_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param int count: Number of requested items, default - `20`
        :param int offset: The offset for pagination, default - `0`
        :param bool include_old: Include in result orders older than 2 days, default - `false`
        :param bool include_unfilled: Include in result fully unfilled closed orders, default - `false`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'kind', 'count', 'offset', 'include_old', 'include_unfilled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_order_history_by_currency_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_order_history_by_currency_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'include_unfilled' in local_var_params:
            query_params.append(('include_unfilled', local_var_params['include_unfilled']))  # noqa: E501

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
            '/private/get_order_history_by_currency', 'GET',
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

    def private_get_order_history_by_instrument_get(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves history of orders that have been partially or fully filled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_history_by_instrument_get(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int count: Number of requested items, default - `20`
        :param int offset: The offset for pagination, default - `0`
        :param bool include_old: Include in result orders older than 2 days, default - `false`
        :param bool include_unfilled: Include in result fully unfilled closed orders, default - `false`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_order_history_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_order_history_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
            return data

    def private_get_order_history_by_instrument_get_with_http_info(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves history of orders that have been partially or fully filled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_history_by_instrument_get_with_http_info(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int count: Number of requested items, default - `20`
        :param int offset: The offset for pagination, default - `0`
        :param bool include_old: Include in result orders older than 2 days, default - `false`
        :param bool include_unfilled: Include in result fully unfilled closed orders, default - `false`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'count', 'offset', 'include_old', 'include_unfilled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_order_history_by_instrument_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_order_history_by_instrument_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'include_unfilled' in local_var_params:
            query_params.append(('include_unfilled', local_var_params['include_unfilled']))  # noqa: E501

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
            '/private/get_order_history_by_instrument', 'GET',
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

    def private_get_order_margin_by_ids_get(self, ids, **kwargs):  # noqa: E501
        """Retrieves initial margins of given orders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_margin_by_ids_get(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: Ids of orders (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_order_margin_by_ids_get_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_order_margin_by_ids_get_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def private_get_order_margin_by_ids_get_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Retrieves initial margins of given orders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_margin_by_ids_get_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: Ids of orders (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_order_margin_by_ids_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in local_var_params or
                local_var_params['ids'] is None):
            raise ApiValueError("Missing the required parameter `ids` when calling `private_get_order_margin_by_ids_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501

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
            '/private/get_order_margin_by_ids', 'GET',
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

    def private_get_order_state_get(self, order_id, **kwargs):  # noqa: E501
        """Retrieve the current state of an order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_state_get(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_order_state_get_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_order_state_get_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def private_get_order_state_get_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Retrieve the current state of an order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_order_state_get_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_order_state_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in local_var_params or
                local_var_params['order_id'] is None):
            raise ApiValueError("Missing the required parameter `order_id` when calling `private_get_order_state_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))  # noqa: E501

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
            '/private/get_order_state', 'GET',
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

    def private_get_settlement_history_by_currency_get(self, currency, **kwargs):  # noqa: E501
        """Retrieves settlement, delivery and bankruptcy events that have affected your account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_settlement_history_by_currency_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Settlement type
        :param int count: Number of requested items, default - `20`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_settlement_history_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_settlement_history_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def private_get_settlement_history_by_currency_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Retrieves settlement, delivery and bankruptcy events that have affected your account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_settlement_history_by_currency_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str type: Settlement type
        :param int count: Number of requested items, default - `20`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'type', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_settlement_history_by_currency_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_settlement_history_by_currency_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

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
            '/private/get_settlement_history_by_currency', 'GET',
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

    def private_get_settlement_history_by_instrument_get(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves public settlement, delivery and bankruptcy events filtered by instrument name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_settlement_history_by_instrument_get(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Settlement type
        :param int count: Number of requested items, default - `20`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_settlement_history_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_settlement_history_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
            return data

    def private_get_settlement_history_by_instrument_get_with_http_info(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieves public settlement, delivery and bankruptcy events filtered by instrument name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_settlement_history_by_instrument_get_with_http_info(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param str type: Settlement type
        :param int count: Number of requested items, default - `20`
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'type', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_settlement_history_by_instrument_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_settlement_history_by_instrument_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

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
            '/private/get_settlement_history_by_instrument', 'GET',
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

    def private_get_user_trades_by_currency_and_time_get(self, currency, start_timestamp, end_timestamp, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for instruments in a specific currency symbol and within given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_currency_and_time_get(currency, start_timestamp, end_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param int start_timestamp: The earliest timestamp to return result for (required)
        :param int end_timestamp: The most recent timestamp to return result for (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_user_trades_by_currency_and_time_get_with_http_info(currency, start_timestamp, end_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_user_trades_by_currency_and_time_get_with_http_info(currency, start_timestamp, end_timestamp, **kwargs)  # noqa: E501
            return data

    def private_get_user_trades_by_currency_and_time_get_with_http_info(self, currency, start_timestamp, end_timestamp, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for instruments in a specific currency symbol and within given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_currency_and_time_get_with_http_info(currency, start_timestamp, end_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param int start_timestamp: The earliest timestamp to return result for (required)
        :param int end_timestamp: The most recent timestamp to return result for (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'start_timestamp', 'end_timestamp', 'kind', 'count', 'include_old', 'sorting']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_user_trades_by_currency_and_time_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_user_trades_by_currency_and_time_get`")  # noqa: E501
        # verify the required parameter 'start_timestamp' is set
        if ('start_timestamp' not in local_var_params or
                local_var_params['start_timestamp'] is None):
            raise ApiValueError("Missing the required parameter `start_timestamp` when calling `private_get_user_trades_by_currency_and_time_get`")  # noqa: E501
        # verify the required parameter 'end_timestamp' is set
        if ('end_timestamp' not in local_var_params or
                local_var_params['end_timestamp'] is None):
            raise ApiValueError("Missing the required parameter `end_timestamp` when calling `private_get_user_trades_by_currency_and_time_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
        if 'start_timestamp' in local_var_params:
            query_params.append(('start_timestamp', local_var_params['start_timestamp']))  # noqa: E501
        if 'end_timestamp' in local_var_params:
            query_params.append(('end_timestamp', local_var_params['end_timestamp']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'sorting' in local_var_params:
            query_params.append(('sorting', local_var_params['sorting']))  # noqa: E501

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
            '/private/get_user_trades_by_currency_and_time', 'GET',
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

    def private_get_user_trades_by_currency_get(self, currency, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for instruments in a specific currency symbol.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_currency_get(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str start_id: The ID number of the first trade to be returned
        :param str end_id: The ID number of the last trade to be returned
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_user_trades_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_user_trades_by_currency_get_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def private_get_user_trades_by_currency_get_with_http_info(self, currency, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for instruments in a specific currency symbol.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_currency_get_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The currency symbol (required)
        :param str kind: Instrument kind, if not provided instruments of all kinds are considered
        :param str start_id: The ID number of the first trade to be returned
        :param str end_id: The ID number of the last trade to be returned
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'kind', 'start_id', 'end_id', 'count', 'include_old', 'sorting']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_user_trades_by_currency_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in local_var_params or
                local_var_params['currency'] is None):
            raise ApiValueError("Missing the required parameter `currency` when calling `private_get_user_trades_by_currency_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params:
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
        if 'start_id' in local_var_params:
            query_params.append(('start_id', local_var_params['start_id']))  # noqa: E501
        if 'end_id' in local_var_params:
            query_params.append(('end_id', local_var_params['end_id']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'sorting' in local_var_params:
            query_params.append(('sorting', local_var_params['sorting']))  # noqa: E501

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
            '/private/get_user_trades_by_currency', 'GET',
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

    def private_get_user_trades_by_instrument_and_time_get(self, instrument_name, start_timestamp, end_timestamp, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for a specific instrument and within given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_instrument_and_time_get(instrument_name, start_timestamp, end_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int start_timestamp: The earliest timestamp to return result for (required)
        :param int end_timestamp: The most recent timestamp to return result for (required)
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_user_trades_by_instrument_and_time_get_with_http_info(instrument_name, start_timestamp, end_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_user_trades_by_instrument_and_time_get_with_http_info(instrument_name, start_timestamp, end_timestamp, **kwargs)  # noqa: E501
            return data

    def private_get_user_trades_by_instrument_and_time_get_with_http_info(self, instrument_name, start_timestamp, end_timestamp, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for a specific instrument and within given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_instrument_and_time_get_with_http_info(instrument_name, start_timestamp, end_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int start_timestamp: The earliest timestamp to return result for (required)
        :param int end_timestamp: The most recent timestamp to return result for (required)
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'start_timestamp', 'end_timestamp', 'count', 'include_old', 'sorting']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_user_trades_by_instrument_and_time_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_user_trades_by_instrument_and_time_get`")  # noqa: E501
        # verify the required parameter 'start_timestamp' is set
        if ('start_timestamp' not in local_var_params or
                local_var_params['start_timestamp'] is None):
            raise ApiValueError("Missing the required parameter `start_timestamp` when calling `private_get_user_trades_by_instrument_and_time_get`")  # noqa: E501
        # verify the required parameter 'end_timestamp' is set
        if ('end_timestamp' not in local_var_params or
                local_var_params['end_timestamp'] is None):
            raise ApiValueError("Missing the required parameter `end_timestamp` when calling `private_get_user_trades_by_instrument_and_time_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'start_timestamp' in local_var_params:
            query_params.append(('start_timestamp', local_var_params['start_timestamp']))  # noqa: E501
        if 'end_timestamp' in local_var_params:
            query_params.append(('end_timestamp', local_var_params['end_timestamp']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'sorting' in local_var_params:
            query_params.append(('sorting', local_var_params['sorting']))  # noqa: E501

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
            '/private/get_user_trades_by_instrument_and_time', 'GET',
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

    def private_get_user_trades_by_instrument_get(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for a specific instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_instrument_get(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int start_seq: The sequence number of the first trade to be returned
        :param int end_seq: The sequence number of the last trade to be returned
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_user_trades_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_user_trades_by_instrument_get_with_http_info(instrument_name, **kwargs)  # noqa: E501
            return data

    def private_get_user_trades_by_instrument_get_with_http_info(self, instrument_name, **kwargs):  # noqa: E501
        """Retrieve the latest user trades that have occurred for a specific instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_instrument_get_with_http_info(instrument_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param int start_seq: The sequence number of the first trade to be returned
        :param int end_seq: The sequence number of the last trade to be returned
        :param int count: Number of requested items, default - `10`
        :param bool include_old: Include trades older than 7 days, default - `false`
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'start_seq', 'end_seq', 'count', 'include_old', 'sorting']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_user_trades_by_instrument_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_get_user_trades_by_instrument_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'start_seq' in local_var_params:
            query_params.append(('start_seq', local_var_params['start_seq']))  # noqa: E501
        if 'end_seq' in local_var_params:
            query_params.append(('end_seq', local_var_params['end_seq']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'include_old' in local_var_params:
            query_params.append(('include_old', local_var_params['include_old']))  # noqa: E501
        if 'sorting' in local_var_params:
            query_params.append(('sorting', local_var_params['sorting']))  # noqa: E501

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
            '/private/get_user_trades_by_instrument', 'GET',
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

    def private_get_user_trades_by_order_get(self, order_id, **kwargs):  # noqa: E501
        """Retrieve the list of user trades that was created for given order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_order_get(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_get_user_trades_by_order_get_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.private_get_user_trades_by_order_get_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def private_get_user_trades_by_order_get_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Retrieve the list of user trades that was created for given order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_get_user_trades_by_order_get_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: The order id (required)
        :param str sorting: Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['order_id', 'sorting']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_get_user_trades_by_order_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in local_var_params or
                local_var_params['order_id'] is None):
            raise ApiValueError("Missing the required parameter `order_id` when calling `private_get_user_trades_by_order_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))  # noqa: E501
        if 'sorting' in local_var_params:
            query_params.append(('sorting', local_var_params['sorting']))  # noqa: E501

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
            '/private/get_user_trades_by_order', 'GET',
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

    def private_sell_get(self, instrument_name, amount, **kwargs):  # noqa: E501
        """Places a sell order for an instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_sell_get(instrument_name, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param str type: The order type, default: `\"limit\"`
        :param str label: user defined label for the order (maximum 32 characters)
        :param float price: <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p>
        :param str time_in_force: <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul>
        :param float max_show: Maximum amount within an order to be shown to other customers, `0` for invisible order
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param bool reduce_only: If `true`, the order is considered reduce-only which is intended to only reduce a current position
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :param str trigger: Defines trigger type, required for `\"stop_limit\"` order type
        :param str advanced: Advanced option order type. (Only for options)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_sell_get_with_http_info(instrument_name, amount, **kwargs)  # noqa: E501
        else:
            (data) = self.private_sell_get_with_http_info(instrument_name, amount, **kwargs)  # noqa: E501
            return data

    def private_sell_get_with_http_info(self, instrument_name, amount, **kwargs):  # noqa: E501
        """Places a sell order for an instrument.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_sell_get_with_http_info(instrument_name, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_name: Instrument name (required)
        :param float amount: It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH (required)
        :param str type: The order type, default: `\"limit\"`
        :param str label: user defined label for the order (maximum 32 characters)
        :param float price: <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p>
        :param str time_in_force: <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul>
        :param float max_show: Maximum amount within an order to be shown to other customers, `0` for invisible order
        :param bool post_only: <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p>
        :param bool reduce_only: If `true`, the order is considered reduce-only which is intended to only reduce a current position
        :param float stop_price: Stop price, required for stop limit orders (Only for stop orders)
        :param str trigger: Defines trigger type, required for `\"stop_limit\"` order type
        :param str advanced: Advanced option order type. (Only for options)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['instrument_name', 'amount', 'type', 'label', 'price', 'time_in_force', 'max_show', 'post_only', 'reduce_only', 'stop_price', 'trigger', 'advanced']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_sell_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_name' is set
        if ('instrument_name' not in local_var_params or
                local_var_params['instrument_name'] is None):
            raise ApiValueError("Missing the required parameter `instrument_name` when calling `private_sell_get`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in local_var_params or
                local_var_params['amount'] is None):
            raise ApiValueError("Missing the required parameter `amount` when calling `private_sell_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_name' in local_var_params:
            query_params.append(('instrument_name', local_var_params['instrument_name']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))  # noqa: E501
        if 'price' in local_var_params:
            query_params.append(('price', local_var_params['price']))  # noqa: E501
        if 'time_in_force' in local_var_params:
            query_params.append(('time_in_force', local_var_params['time_in_force']))  # noqa: E501
        if 'max_show' in local_var_params:
            query_params.append(('max_show', local_var_params['max_show']))  # noqa: E501
        if 'post_only' in local_var_params:
            query_params.append(('post_only', local_var_params['post_only']))  # noqa: E501
        if 'reduce_only' in local_var_params:
            query_params.append(('reduce_only', local_var_params['reduce_only']))  # noqa: E501
        if 'stop_price' in local_var_params:
            query_params.append(('stop_price', local_var_params['stop_price']))  # noqa: E501
        if 'trigger' in local_var_params:
            query_params.append(('trigger', local_var_params['trigger']))  # noqa: E501
        if 'advanced' in local_var_params:
            query_params.append(('advanced', local_var_params['advanced']))  # noqa: E501

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
            '/private/sell', 'GET',
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
