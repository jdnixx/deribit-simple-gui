# coding: utf-8

"""
    Deribit API

    #Overview  Deribit provides three different interfaces to access the API:  * [JSON-RPC over Websocket](#json-rpc) * [JSON-RPC over HTTP](#json-rpc) * [FIX](#fix-api) (Financial Information eXchange)  With the API Console you can use and test the JSON-RPC API, both via HTTP and  via Websocket. To visit the API console, go to __Account > API tab >  API Console tab.__   ##Naming Deribit tradeable assets or instruments use the following system of naming:  |Kind|Examples|Template|Comments| |----|--------|--------|--------| |Future|<code>BTC-25MAR16</code>, <code>BTC-5AUG16</code>|<code>BTC-DMMMYY</code>|<code>BTC</code> is currency, <code>DMMMYY</code> is expiration date, <code>D</code> stands for day of month (1 or 2 digits), <code>MMM</code> - month (3 first letters in English), <code>YY</code> stands for year.| |Perpetual|<code>BTC-PERPETUAL</code>                        ||Perpetual contract for currency <code>BTC</code>.| |Option|<code>BTC-25MAR16-420-C</code>, <code>BTC-5AUG16-580-P</code>|<code>BTC-DMMMYY-STRIKE-K</code>|<code>STRIKE</code> is option strike price in USD. Template <code>K</code> is option kind: <code>C</code> for call options or <code>P</code> for put options.|   # JSON-RPC JSON-RPC is a light-weight remote procedure call (RPC) protocol. The  [JSON-RPC specification](https://www.jsonrpc.org/specification) defines the data structures that are used for the messages that are exchanged between client and server, as well as the rules around their processing. JSON-RPC uses JSON (RFC 4627) as data format.  JSON-RPC is transport agnostic: it does not specify which transport mechanism must be used. The Deribit API supports both Websocket (preferred) and HTTP (with limitations: subscriptions are not supported over HTTP).  ## Request messages > An example of a request message:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 8066,     \"method\": \"public/ticker\",     \"params\": {         \"instrument\": \"BTC-24AUG18-6500-P\"     } } ```  According to the JSON-RPC sepcification the requests must be JSON objects with the following fields.  |Name|Type|Description| |----|----|-----------| |jsonrpc|string|The version of the JSON-RPC spec: \"2.0\"| |id|integer or string|An identifier of the request. If it is included, then the response will contain the same identifier| |method|string|The method to be invoked| |params|object|The parameters values for the method. The field names must match with the expected parameter names. The parameters that are expected are described in the documentation for the methods, below.|  <aside class=\"warning\"> The JSON-RPC specification describes two features that are currently not supported by the API:  <ul> <li>Specification of parameter values by position</li> <li>Batch requests</li> </ul>  </aside>   ## Response messages > An example of a response message:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 5239,     \"testnet\": false,     \"result\": [         {             \"currency\": \"BTC\",             \"currencyLong\": \"Bitcoin\",             \"minConfirmation\": 2,             \"txFee\": 0.0006,             \"isActive\": true,             \"coinType\": \"BITCOIN\",             \"baseAddress\": null         }     ],     \"usIn\": 1535043730126248,     \"usOut\": 1535043730126250,     \"usDiff\": 2 } ```  The JSON-RPC API always responds with a JSON object with the following fields.   |Name|Type|Description| |----|----|-----------| |id|integer|This is the same id that was sent in the request.| |result|any|If successful, the result of the API call. The format for the result is described with each method.| |error|error object|Only present if there was an error invoking the method. The error object is described below.| |testnet|boolean|Indicates whether the API in use is actually the test API.  <code>false</code> for production server, <code>true</code> for test server.| |usIn|integer|The timestamp when the requests was received (microseconds since the Unix epoch)| |usOut|integer|The timestamp when the response was sent (microseconds since the Unix epoch)| |usDiff|integer|The number of microseconds that was spent handling the request|  <aside class=\"notice\"> The fields <code>testnet</code>, <code>usIn</code>, <code>usOut</code> and <code>usDiff</code> are not part of the JSON-RPC standard.  <p>In order not to clutter the examples they will generally be omitted from the example code.</p> </aside>  > An example of a response with an error:  ```json {     \"jsonrpc\": \"2.0\",     \"id\": 8163,     \"error\": {         \"code\": 11050,         \"message\": \"bad_request\"     },     \"testnet\": false,     \"usIn\": 1535037392434763,     \"usOut\": 1535037392448119,     \"usDiff\": 13356 } ``` In case of an error the response message will contain the error field, with as value an object with the following with the following fields:  |Name|Type|Description |----|----|-----------| |code|integer|A number that indicates the kind of error.| |message|string|A short description that indicates the kind of error.| |data|any|Additional data about the error. This field may be omitted.|  ## Notifications  > An example of a notification:  ```json {     \"jsonrpc\": \"2.0\",     \"method\": \"subscription\",     \"params\": {         \"channel\": \"deribit_price_index.btc_usd\",         \"data\": {             \"timestamp\": 1535098298227,             \"price\": 6521.17,             \"index_name\": \"btc_usd\"         }     } } ```  API users can subscribe to certain types of notifications. This means that they will receive JSON-RPC notification-messages from the server when certain events occur, such as changes to the index price or changes to the order book for a certain instrument.   The API methods [public/subscribe](#public-subscribe) and [private/subscribe](#private-subscribe) are used to set up a subscription. Since HTTP does not support the sending of messages from server to client, these methods are only availble when using the Websocket transport mechanism.  At the moment of subscription a \"channel\" must be specified. The channel determines the type of events that will be received.  See [Subscriptions](#subscriptions) for more details about the channels.  In accordance with the JSON-RPC specification, the format of a notification  is that of a request message without an <code>id</code> field. The value of the <code>method</code> field will always be <code>\"subscription\"</code>. The <code>params</code> field will always be an object with 2 members: <code>channel</code> and <code>data</code>. The value of the <code>channel</code> member is the name of the channel (a string). The value of the <code>data</code> member is an object that contains data  that is specific for the channel.   ## Authentication  > An example of a JSON request with token:  ```json {     \"id\": 5647,     \"method\": \"private/get_subaccounts\",     \"params\": {         \"access_token\": \"67SVutDoVZSzkUStHSuk51WntMNBJ5mh5DYZhwzpiqDF\"     } } ```  The API consists of `public` and `private` methods. The public methods do not require authentication. The private methods use OAuth 2.0 authentication. This means that a valid OAuth access token must be included in the request, which can get achived by calling method [public/auth](#public-auth).  When the token was assigned to the user, it should be passed along, with other request parameters, back to the server:  |Connection type|Access token placement |----|-----------| |**Websocket**|Inside request JSON parameters, as an `access_token` field| |**HTTP (REST)**|Header `Authorization: bearer ```Token``` ` value|  ### Additional authorization method - basic user credentials  <span style=\"color:red\"><b> ! Not recommended - however, it could be useful for quick testing API</b></span></br>  Every `private` method could be accessed by providing, inside HTTP `Authorization: Basic XXX` header, values with user `ClientId` and assigned `ClientSecret` (both values can be found on the API page on the Deribit website) encoded with `Base64`:  <code>Authorization: Basic BASE64(`ClientId` + `:` + `ClientSecret`)</code>   ### Additional authorization method - Deribit signature credentials  The Derbit service provides dedicated authorization method, which harness user generated signature to increase security level for passing request data. Generated value is passed inside `Authorization` header, coded as:  <code>Authorization: deri-hmac-sha256 id=```ClientId```,ts=```Timestamp```,sig=```Signature```,nonce=```Nonce```</code>  where:  |Deribit credential|Description |----|-----------| |*ClientId*|Can be found on the API page on the Deribit website| |*Timestamp*|Time when the request was generated - given as **miliseconds**. It's valid for **60 seconds** since generation, after that time any request with an old timestamp will be rejected.| |*Signature*|Value for signature calculated as described below | |*Nonce*|Single usage, user generated initialization vector for the server token|  The signature is generated by the following formula:  <code> Signature = HEX_STRING( HMAC-SHA256( ClientSecret, StringToSign ) );</code></br>  <code> StringToSign =  Timestamp + \"\\n\" + Nonce + \"\\n\" + RequestData;</code></br>  <code> RequestData =  UPPERCASE(HTTP_METHOD())  + \"\\n\" + URI() + \"\\n\" + RequestBody + \"\\n\";</code></br>   e.g. (using shell with ```openssl``` tool):  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientId=AAAAAAAAAAA</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientSecret=ABCD</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Timestamp=$( date +%s000 )</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Nonce=$( cat /dev/urandom | tr -dc 'a-z0-9' | head -c8 )</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;URI=\"/api/v2/private/get_account_summary?currency=BTC\"</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;HttpMethod=GET</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Body=\"\"</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Signature=$( echo -ne \"${Timestamp}\\n${Nonce}\\n${HttpMethod}\\n${URI}\\n${Body}\\n\" | openssl sha256 -r -hmac \"$ClientSecret\" | cut -f1 -d' ' )</code></br></br> <code>&nbsp;&nbsp;&nbsp;&nbsp;echo $Signature</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;shell output> ea40d5e5e4fae235ab22b61da98121fbf4acdc06db03d632e23c66bcccb90d2c  (**WARNING**: Exact value depends on current timestamp and client credentials</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;curl -s -X ${HttpMethod} -H \"Authorization: deri-hmac-sha256 id=${ClientId},ts=${Timestamp},nonce=${Nonce},sig=${Signature}\" \"https://www.deribit.com${URI}\"</code></br></br>    ### Additional authorization method - signature credentials (WebSocket API)  When connecting through Websocket, user can request for authorization using ```client_credential``` method, which requires providing following parameters (as a part of JSON request):  |JSON parameter|Description |----|-----------| |*grant_type*|Must be **client_signature**| |*client_id*|Can be found on the API page on the Deribit website| |*timestamp*|Time when the request was generated - given as **miliseconds**. It's valid for **60 seconds** since generation, after that time any request with an old timestamp will be rejected.| |*signature*|Value for signature calculated as described below | |*nonce*|Single usage, user generated initialization vector for the server token| |*data*|**Optional** field, which contains any user specific value|  The signature is generated by the following formula:  <code> StringToSign =  Timestamp + \"\\n\" + Nonce + \"\\n\" + Data;</code></br>  <code> Signature = HEX_STRING( HMAC-SHA256( ClientSecret, StringToSign ) );</code></br>   e.g. (using shell with ```openssl``` tool):  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientId=AAAAAAAAAAA</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;ClientSecret=ABCD</code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Timestamp=$( date +%s000 ) # e.g. 1554883365000 </code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Nonce=$( cat /dev/urandom | tr -dc 'a-z0-9' | head -c8 ) # e.g. fdbmmz79 </code></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Data=\"\"</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;Signature=$( echo -ne \"${Timestamp}\\n${Nonce}\\n${Data}\\n\" | openssl sha256 -r -hmac \"$ClientSecret\" | cut -f1 -d' ' )</code></br></br> <code>&nbsp;&nbsp;&nbsp;&nbsp;echo $Signature</code></br></br>  <code>&nbsp;&nbsp;&nbsp;&nbsp;shell output> e20c9cd5639d41f8bbc88f4d699c4baf94a4f0ee320e9a116b72743c449eb994  (**WARNING**: Exact value depends on current timestamp and client credentials</code></br></br>   You can also check the signature value using some online tools like, e.g: [https://codebeautify.org/hmac-generator](https://codebeautify.org/hmac-generator) (but don't forget about adding *newline* after each part of the hashed text and remember that you **should use** it only with your **test credentials**).   Here's a sample JSON request created using the values from the example above:  <code> {                            </br> &nbsp;&nbsp;\"jsonrpc\" : \"2.0\",         </br> &nbsp;&nbsp;\"id\" : 9929,               </br> &nbsp;&nbsp;\"method\" : \"public/auth\",  </br> &nbsp;&nbsp;\"params\" :                 </br> &nbsp;&nbsp;{                        </br> &nbsp;&nbsp;&nbsp;&nbsp;\"grant_type\" : \"client_signature\",   </br> &nbsp;&nbsp;&nbsp;&nbsp;\"client_id\" : \"AAAAAAAAAAA\",         </br> &nbsp;&nbsp;&nbsp;&nbsp;\"timestamp\": \"1554883365000\",        </br> &nbsp;&nbsp;&nbsp;&nbsp;\"nonce\": \"fdbmmz79\",                 </br> &nbsp;&nbsp;&nbsp;&nbsp;\"data\": \"\",                          </br> &nbsp;&nbsp;&nbsp;&nbsp;\"signature\" : \"e20c9cd5639d41f8bbc88f4d699c4baf94a4f0ee320e9a116b72743c449eb994\"  </br> &nbsp;&nbsp;}                        </br> }                            </br> </code>   ### Access scope  When asking for `access token` user can provide the required access level (called `scope`) which defines what type of functionality he/she wants to use, and whether requests are only going to check for some data or also to update them.  Scopes are required and checked for `private` methods, so if you plan to use only `public` information you can stay with values assigned by default.  |Scope|Description |----|-----------| |*account:read*|Access to **account** methods - read only data| |*account:read_write*|Access to **account** methods - allows to manage account settings, add subaccounts, etc.| |*trade:read*|Access to **trade** methods - read only data| |*trade:read_write*|Access to **trade** methods - required to create and modify orders| |*wallet:read*|Access to **wallet** methods - read only data| |*wallet:read_write*|Access to **wallet** methods - allows to withdraw, generate new deposit address, etc.| |*wallet:none*, *account:none*, *trade:none*|Blocked access to specified functionality|    <span style=\"color:red\">**NOTICE:**</span> Depending on choosing an authentication method (```grant type```) some scopes could be narrowed by the server. e.g. when ```grant_type = client_credentials``` and ```scope = wallet:read_write``` it's modified by the server as ```scope = wallet:read```\"   ## JSON-RPC over websocket Websocket is the prefered transport mechanism for the JSON-RPC API, because it is faster and because it can support [subscriptions](#subscriptions) and [cancel on disconnect](#private-enable_cancel_on_disconnect). The code examples that can be found next to each of the methods show how websockets can be used from Python or Javascript/node.js.  ## JSON-RPC over HTTP Besides websockets it is also possible to use the API via HTTP. The code examples for 'shell' show how this can be done using curl. Note that subscriptions and cancel on disconnect are not supported via HTTP.  #Methods   # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Order(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'direction': 'str',
        'reduce_only': 'bool',
        'triggered': 'bool',
        'order_id': 'str',
        'price': 'float',
        'time_in_force': 'str',
        'api': 'bool',
        'order_state': 'str',
        'implv': 'float',
        'advanced': 'str',
        'post_only': 'bool',
        'usd': 'float',
        'stop_price': 'float',
        'order_type': 'str',
        'last_update_timestamp': 'int',
        'original_order_type': 'str',
        'max_show': 'float',
        'profit_loss': 'float',
        'is_liquidation': 'bool',
        'filled_amount': 'float',
        'label': 'str',
        'commission': 'float',
        'amount': 'float',
        'trigger': 'str',
        'instrument_name': 'str',
        'creation_timestamp': 'int',
        'average_price': 'float'
    }

    attribute_map = {
        'direction': 'direction',
        'reduce_only': 'reduce_only',
        'triggered': 'triggered',
        'order_id': 'order_id',
        'price': 'price',
        'time_in_force': 'time_in_force',
        'api': 'api',
        'order_state': 'order_state',
        'implv': 'implv',
        'advanced': 'advanced',
        'post_only': 'post_only',
        'usd': 'usd',
        'stop_price': 'stop_price',
        'order_type': 'order_type',
        'last_update_timestamp': 'last_update_timestamp',
        'original_order_type': 'original_order_type',
        'max_show': 'max_show',
        'profit_loss': 'profit_loss',
        'is_liquidation': 'is_liquidation',
        'filled_amount': 'filled_amount',
        'label': 'label',
        'commission': 'commission',
        'amount': 'amount',
        'trigger': 'trigger',
        'instrument_name': 'instrument_name',
        'creation_timestamp': 'creation_timestamp',
        'average_price': 'average_price'
    }

    def __init__(self, direction=None, reduce_only=None, triggered=None, order_id=None, price=None, time_in_force=None, api=None, order_state=None, implv=None, advanced=None, post_only=None, usd=None, stop_price=None, order_type=None, last_update_timestamp=None, original_order_type=None, max_show=None, profit_loss=None, is_liquidation=None, filled_amount=None, label=None, commission=None, amount=None, trigger=None, instrument_name=None, creation_timestamp=None, average_price=None):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501

        self._direction = None
        self._reduce_only = None
        self._triggered = None
        self._order_id = None
        self._price = None
        self._time_in_force = None
        self._api = None
        self._order_state = None
        self._implv = None
        self._advanced = None
        self._post_only = None
        self._usd = None
        self._stop_price = None
        self._order_type = None
        self._last_update_timestamp = None
        self._original_order_type = None
        self._max_show = None
        self._profit_loss = None
        self._is_liquidation = None
        self._filled_amount = None
        self._label = None
        self._commission = None
        self._amount = None
        self._trigger = None
        self._instrument_name = None
        self._creation_timestamp = None
        self._average_price = None
        self.discriminator = None

        self.direction = direction
        if reduce_only is not None:
            self.reduce_only = reduce_only
        if triggered is not None:
            self.triggered = triggered
        self.order_id = order_id
        self.price = price
        self.time_in_force = time_in_force
        self.api = api
        self.order_state = order_state
        if implv is not None:
            self.implv = implv
        if advanced is not None:
            self.advanced = advanced
        self.post_only = post_only
        if usd is not None:
            self.usd = usd
        if stop_price is not None:
            self.stop_price = stop_price
        self.order_type = order_type
        self.last_update_timestamp = last_update_timestamp
        if original_order_type is not None:
            self.original_order_type = original_order_type
        self.max_show = max_show
        if profit_loss is not None:
            self.profit_loss = profit_loss
        self.is_liquidation = is_liquidation
        if filled_amount is not None:
            self.filled_amount = filled_amount
        self.label = label
        if commission is not None:
            self.commission = commission
        if amount is not None:
            self.amount = amount
        if trigger is not None:
            self.trigger = trigger
        if instrument_name is not None:
            self.instrument_name = instrument_name
        self.creation_timestamp = creation_timestamp
        if average_price is not None:
            self.average_price = average_price

    @property
    def direction(self):
        """Gets the direction of this Order.  # noqa: E501

        direction, `buy` or `sell`  # noqa: E501

        :return: The direction of this Order.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Order.

        direction, `buy` or `sell`  # noqa: E501

        :param direction: The direction of this Order.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        allowed_values = ["buy", "sell"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def reduce_only(self):
        """Gets the reduce_only of this Order.  # noqa: E501

        `true` for reduce-only orders only  # noqa: E501

        :return: The reduce_only of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._reduce_only

    @reduce_only.setter
    def reduce_only(self, reduce_only):
        """Sets the reduce_only of this Order.

        `true` for reduce-only orders only  # noqa: E501

        :param reduce_only: The reduce_only of this Order.  # noqa: E501
        :type: bool
        """

        self._reduce_only = reduce_only

    @property
    def triggered(self):
        """Gets the triggered of this Order.  # noqa: E501

        Whether the stop order has been triggered (Only for stop orders)  # noqa: E501

        :return: The triggered of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._triggered

    @triggered.setter
    def triggered(self, triggered):
        """Sets the triggered of this Order.

        Whether the stop order has been triggered (Only for stop orders)  # noqa: E501

        :param triggered: The triggered of this Order.  # noqa: E501
        :type: bool
        """

        self._triggered = triggered

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501

        Unique order identifier  # noqa: E501

        :return: The order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        Unique order identifier  # noqa: E501

        :param order_id: The order_id of this Order.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def price(self):
        """Gets the price of this Order.  # noqa: E501

        Price in base currency  # noqa: E501

        :return: The price of this Order.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.

        Price in base currency  # noqa: E501

        :param price: The price of this Order.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def time_in_force(self):
        """Gets the time_in_force of this Order.  # noqa: E501

        Order time in force: `\"good_til_cancelled\"`, `\"fill_or_kill\"`, `\"immediate_or_cancel\"`  # noqa: E501

        :return: The time_in_force of this Order.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this Order.

        Order time in force: `\"good_til_cancelled\"`, `\"fill_or_kill\"`, `\"immediate_or_cancel\"`  # noqa: E501

        :param time_in_force: The time_in_force of this Order.  # noqa: E501
        :type: str
        """
        if time_in_force is None:
            raise ValueError("Invalid value for `time_in_force`, must not be `None`")  # noqa: E501
        allowed_values = ["good_til_cancelled", "fill_or_kill", "immediate_or_cancel"]  # noqa: E501
        if time_in_force not in allowed_values:
            raise ValueError(
                "Invalid value for `time_in_force` ({0}), must be one of {1}"  # noqa: E501
                .format(time_in_force, allowed_values)
            )

        self._time_in_force = time_in_force

    @property
    def api(self):
        """Gets the api of this Order.  # noqa: E501

        `true` if created with API  # noqa: E501

        :return: The api of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this Order.

        `true` if created with API  # noqa: E501

        :param api: The api of this Order.  # noqa: E501
        :type: bool
        """
        if api is None:
            raise ValueError("Invalid value for `api`, must not be `None`")  # noqa: E501

        self._api = api

    @property
    def order_state(self):
        """Gets the order_state of this Order.  # noqa: E501

        order state, `\"open\"`, `\"filled\"`, `\"rejected\"`, `\"cancelled\"`, `\"untriggered\"`  # noqa: E501

        :return: The order_state of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_state

    @order_state.setter
    def order_state(self, order_state):
        """Sets the order_state of this Order.

        order state, `\"open\"`, `\"filled\"`, `\"rejected\"`, `\"cancelled\"`, `\"untriggered\"`  # noqa: E501

        :param order_state: The order_state of this Order.  # noqa: E501
        :type: str
        """
        if order_state is None:
            raise ValueError("Invalid value for `order_state`, must not be `None`")  # noqa: E501
        allowed_values = ["open", "filled", "rejected", "cancelled", "untriggered", "triggered"]  # noqa: E501
        if order_state not in allowed_values:
            raise ValueError(
                "Invalid value for `order_state` ({0}), must be one of {1}"  # noqa: E501
                .format(order_state, allowed_values)
            )

        self._order_state = order_state

    @property
    def implv(self):
        """Gets the implv of this Order.  # noqa: E501

        Implied volatility in percent. (Only if `advanced=\"implv\"`)  # noqa: E501

        :return: The implv of this Order.  # noqa: E501
        :rtype: float
        """
        return self._implv

    @implv.setter
    def implv(self, implv):
        """Sets the implv of this Order.

        Implied volatility in percent. (Only if `advanced=\"implv\"`)  # noqa: E501

        :param implv: The implv of this Order.  # noqa: E501
        :type: float
        """

        self._implv = implv

    @property
    def advanced(self):
        """Gets the advanced of this Order.  # noqa: E501

        advanced type: `\"usd\"` or `\"implv\"` (Only for options; field is omitted if not applicable).   # noqa: E501

        :return: The advanced of this Order.  # noqa: E501
        :rtype: str
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this Order.

        advanced type: `\"usd\"` or `\"implv\"` (Only for options; field is omitted if not applicable).   # noqa: E501

        :param advanced: The advanced of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["usd", "implv"]  # noqa: E501
        if advanced not in allowed_values:
            raise ValueError(
                "Invalid value for `advanced` ({0}), must be one of {1}"  # noqa: E501
                .format(advanced, allowed_values)
            )

        self._advanced = advanced

    @property
    def post_only(self):
        """Gets the post_only of this Order.  # noqa: E501

        `true` for post-only orders only  # noqa: E501

        :return: The post_only of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._post_only

    @post_only.setter
    def post_only(self, post_only):
        """Sets the post_only of this Order.

        `true` for post-only orders only  # noqa: E501

        :param post_only: The post_only of this Order.  # noqa: E501
        :type: bool
        """
        if post_only is None:
            raise ValueError("Invalid value for `post_only`, must not be `None`")  # noqa: E501

        self._post_only = post_only

    @property
    def usd(self):
        """Gets the usd of this Order.  # noqa: E501

        Option price in USD (Only if `advanced=\"usd\"`)  # noqa: E501

        :return: The usd of this Order.  # noqa: E501
        :rtype: float
        """
        return self._usd

    @usd.setter
    def usd(self, usd):
        """Sets the usd of this Order.

        Option price in USD (Only if `advanced=\"usd\"`)  # noqa: E501

        :param usd: The usd of this Order.  # noqa: E501
        :type: float
        """

        self._usd = usd

    @property
    def stop_price(self):
        """Gets the stop_price of this Order.  # noqa: E501

        stop price (Only for future stop orders)  # noqa: E501

        :return: The stop_price of this Order.  # noqa: E501
        :rtype: float
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this Order.

        stop price (Only for future stop orders)  # noqa: E501

        :param stop_price: The stop_price of this Order.  # noqa: E501
        :type: float
        """

        self._stop_price = stop_price

    @property
    def order_type(self):
        """Gets the order_type of this Order.  # noqa: E501

        order type, `\"limit\"`, `\"market\"`, `\"stop_limit\"`, `\"stop_market\"`  # noqa: E501

        :return: The order_type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this Order.

        order type, `\"limit\"`, `\"market\"`, `\"stop_limit\"`, `\"stop_market\"`  # noqa: E501

        :param order_type: The order_type of this Order.  # noqa: E501
        :type: str
        """
        if order_type is None:
            raise ValueError("Invalid value for `order_type`, must not be `None`")  # noqa: E501
        allowed_values = ["market", "limit", "stop_market", "stop_limit"]  # noqa: E501
        if order_type not in allowed_values:
            raise ValueError(
                "Invalid value for `order_type` ({0}), must be one of {1}"  # noqa: E501
                .format(order_type, allowed_values)
            )

        self._order_type = order_type

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this Order.  # noqa: E501

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :return: The last_update_timestamp of this Order.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this Order.

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this Order.  # noqa: E501
        :type: int
        """
        if last_update_timestamp is None:
            raise ValueError("Invalid value for `last_update_timestamp`, must not be `None`")  # noqa: E501

        self._last_update_timestamp = last_update_timestamp

    @property
    def original_order_type(self):
        """Gets the original_order_type of this Order.  # noqa: E501

        Original order type. Optional field  # noqa: E501

        :return: The original_order_type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._original_order_type

    @original_order_type.setter
    def original_order_type(self, original_order_type):
        """Sets the original_order_type of this Order.

        Original order type. Optional field  # noqa: E501

        :param original_order_type: The original_order_type of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["market"]  # noqa: E501
        if original_order_type not in allowed_values:
            raise ValueError(
                "Invalid value for `original_order_type` ({0}), must be one of {1}"  # noqa: E501
                .format(original_order_type, allowed_values)
            )

        self._original_order_type = original_order_type

    @property
    def max_show(self):
        """Gets the max_show of this Order.  # noqa: E501

        Maximum amount within an order to be shown to other traders, 0 for invisible order.  # noqa: E501

        :return: The max_show of this Order.  # noqa: E501
        :rtype: float
        """
        return self._max_show

    @max_show.setter
    def max_show(self, max_show):
        """Sets the max_show of this Order.

        Maximum amount within an order to be shown to other traders, 0 for invisible order.  # noqa: E501

        :param max_show: The max_show of this Order.  # noqa: E501
        :type: float
        """
        if max_show is None:
            raise ValueError("Invalid value for `max_show`, must not be `None`")  # noqa: E501

        self._max_show = max_show

    @property
    def profit_loss(self):
        """Gets the profit_loss of this Order.  # noqa: E501

        Profit and loss in base currency.  # noqa: E501

        :return: The profit_loss of this Order.  # noqa: E501
        :rtype: float
        """
        return self._profit_loss

    @profit_loss.setter
    def profit_loss(self, profit_loss):
        """Sets the profit_loss of this Order.

        Profit and loss in base currency.  # noqa: E501

        :param profit_loss: The profit_loss of this Order.  # noqa: E501
        :type: float
        """

        self._profit_loss = profit_loss

    @property
    def is_liquidation(self):
        """Gets the is_liquidation of this Order.  # noqa: E501

        `true` if order was automatically created during liquidation  # noqa: E501

        :return: The is_liquidation of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_liquidation

    @is_liquidation.setter
    def is_liquidation(self, is_liquidation):
        """Sets the is_liquidation of this Order.

        `true` if order was automatically created during liquidation  # noqa: E501

        :param is_liquidation: The is_liquidation of this Order.  # noqa: E501
        :type: bool
        """
        if is_liquidation is None:
            raise ValueError("Invalid value for `is_liquidation`, must not be `None`")  # noqa: E501

        self._is_liquidation = is_liquidation

    @property
    def filled_amount(self):
        """Gets the filled_amount of this Order.  # noqa: E501

        Filled amount of the order. For perpetual and futures the filled_amount is in USD units, for options - in units or corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :return: The filled_amount of this Order.  # noqa: E501
        :rtype: float
        """
        return self._filled_amount

    @filled_amount.setter
    def filled_amount(self, filled_amount):
        """Sets the filled_amount of this Order.

        Filled amount of the order. For perpetual and futures the filled_amount is in USD units, for options - in units or corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :param filled_amount: The filled_amount of this Order.  # noqa: E501
        :type: float
        """

        self._filled_amount = filled_amount

    @property
    def label(self):
        """Gets the label of this Order.  # noqa: E501

        user defined label (up to 32 characters)  # noqa: E501

        :return: The label of this Order.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Order.

        user defined label (up to 32 characters)  # noqa: E501

        :param label: The label of this Order.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def commission(self):
        """Gets the commission of this Order.  # noqa: E501

        Commission paid so far (in base currency)  # noqa: E501

        :return: The commission of this Order.  # noqa: E501
        :rtype: float
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this Order.

        Commission paid so far (in base currency)  # noqa: E501

        :param commission: The commission of this Order.  # noqa: E501
        :type: float
        """

        self._commission = commission

    @property
    def amount(self):
        """Gets the amount of this Order.  # noqa: E501

        It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :return: The amount of this Order.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Order.

        It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :param amount: The amount of this Order.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def trigger(self):
        """Gets the trigger of this Order.  # noqa: E501

        Trigger type (Only for stop orders). Allowed values: `\"index_price\"`, `\"mark_price\"`, `\"last_price\"`.  # noqa: E501

        :return: The trigger of this Order.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Order.

        Trigger type (Only for stop orders). Allowed values: `\"index_price\"`, `\"mark_price\"`, `\"last_price\"`.  # noqa: E501

        :param trigger: The trigger of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["index_price", "mark_price", "last_price"]  # noqa: E501
        if trigger not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger, allowed_values)
            )

        self._trigger = trigger

    @property
    def instrument_name(self):
        """Gets the instrument_name of this Order.  # noqa: E501

        Unique instrument identifier  # noqa: E501

        :return: The instrument_name of this Order.  # noqa: E501
        :rtype: str
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, instrument_name):
        """Sets the instrument_name of this Order.

        Unique instrument identifier  # noqa: E501

        :param instrument_name: The instrument_name of this Order.  # noqa: E501
        :type: str
        """

        self._instrument_name = instrument_name

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Order.  # noqa: E501

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :return: The creation_timestamp of this Order.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Order.

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this Order.  # noqa: E501
        :type: int
        """
        if creation_timestamp is None:
            raise ValueError("Invalid value for `creation_timestamp`, must not be `None`")  # noqa: E501

        self._creation_timestamp = creation_timestamp

    @property
    def average_price(self):
        """Gets the average_price of this Order.  # noqa: E501

        Average fill price of the order  # noqa: E501

        :return: The average_price of this Order.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this Order.

        Average fill price of the order  # noqa: E501

        :param average_price: The average_price of this Order.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
