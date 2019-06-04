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


class Settlement(object):
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
        'session_profit_loss': 'float',
        'mark_price': 'float',
        'funding': 'float',
        'socialized': 'float',
        'session_bankrupcy': 'float',
        'timestamp': 'int',
        'profit_loss': 'float',
        'funded': 'float',
        'index_price': 'float',
        'session_tax': 'float',
        'session_tax_rate': 'float',
        'instrument_name': 'str',
        'position': 'float',
        'type': 'str'
    }

    attribute_map = {
        'session_profit_loss': 'session_profit_loss',
        'mark_price': 'mark_price',
        'funding': 'funding',
        'socialized': 'socialized',
        'session_bankrupcy': 'session_bankrupcy',
        'timestamp': 'timestamp',
        'profit_loss': 'profit_loss',
        'funded': 'funded',
        'index_price': 'index_price',
        'session_tax': 'session_tax',
        'session_tax_rate': 'session_tax_rate',
        'instrument_name': 'instrument_name',
        'position': 'position',
        'type': 'type'
    }

    def __init__(self, session_profit_loss=None, mark_price=None, funding=None, socialized=None, session_bankrupcy=None, timestamp=None, profit_loss=None, funded=None, index_price=None, session_tax=None, session_tax_rate=None, instrument_name=None, position=None, type=None):  # noqa: E501
        """Settlement - a model defined in OpenAPI"""  # noqa: E501

        self._session_profit_loss = None
        self._mark_price = None
        self._funding = None
        self._socialized = None
        self._session_bankrupcy = None
        self._timestamp = None
        self._profit_loss = None
        self._funded = None
        self._index_price = None
        self._session_tax = None
        self._session_tax_rate = None
        self._instrument_name = None
        self._position = None
        self._type = None
        self.discriminator = None

        self.session_profit_loss = session_profit_loss
        if mark_price is not None:
            self.mark_price = mark_price
        self.funding = funding
        if socialized is not None:
            self.socialized = socialized
        if session_bankrupcy is not None:
            self.session_bankrupcy = session_bankrupcy
        self.timestamp = timestamp
        if profit_loss is not None:
            self.profit_loss = profit_loss
        if funded is not None:
            self.funded = funded
        self.index_price = index_price
        if session_tax is not None:
            self.session_tax = session_tax
        if session_tax_rate is not None:
            self.session_tax_rate = session_tax_rate
        self.instrument_name = instrument_name
        self.position = position
        self.type = type

    @property
    def session_profit_loss(self):
        """Gets the session_profit_loss of this Settlement.  # noqa: E501

        total value of session profit and losses (in base currency)  # noqa: E501

        :return: The session_profit_loss of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._session_profit_loss

    @session_profit_loss.setter
    def session_profit_loss(self, session_profit_loss):
        """Sets the session_profit_loss of this Settlement.

        total value of session profit and losses (in base currency)  # noqa: E501

        :param session_profit_loss: The session_profit_loss of this Settlement.  # noqa: E501
        :type: float
        """
        if session_profit_loss is None:
            raise ValueError("Invalid value for `session_profit_loss`, must not be `None`")  # noqa: E501

        self._session_profit_loss = session_profit_loss

    @property
    def mark_price(self):
        """Gets the mark_price of this Settlement.  # noqa: E501

        mark price for at the settlement time (in quote currency; settlement and delivery only)  # noqa: E501

        :return: The mark_price of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this Settlement.

        mark price for at the settlement time (in quote currency; settlement and delivery only)  # noqa: E501

        :param mark_price: The mark_price of this Settlement.  # noqa: E501
        :type: float
        """

        self._mark_price = mark_price

    @property
    def funding(self):
        """Gets the funding of this Settlement.  # noqa: E501

        funding (in base currency ; settlement for perpetual product only)  # noqa: E501

        :return: The funding of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this Settlement.

        funding (in base currency ; settlement for perpetual product only)  # noqa: E501

        :param funding: The funding of this Settlement.  # noqa: E501
        :type: float
        """
        if funding is None:
            raise ValueError("Invalid value for `funding`, must not be `None`")  # noqa: E501

        self._funding = funding

    @property
    def socialized(self):
        """Gets the socialized of this Settlement.  # noqa: E501

        the amount of the socialized losses (in base currency; bankruptcy only)  # noqa: E501

        :return: The socialized of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._socialized

    @socialized.setter
    def socialized(self, socialized):
        """Sets the socialized of this Settlement.

        the amount of the socialized losses (in base currency; bankruptcy only)  # noqa: E501

        :param socialized: The socialized of this Settlement.  # noqa: E501
        :type: float
        """

        self._socialized = socialized

    @property
    def session_bankrupcy(self):
        """Gets the session_bankrupcy of this Settlement.  # noqa: E501

        value of session bankrupcy (in base currency; bankruptcy only)  # noqa: E501

        :return: The session_bankrupcy of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._session_bankrupcy

    @session_bankrupcy.setter
    def session_bankrupcy(self, session_bankrupcy):
        """Sets the session_bankrupcy of this Settlement.

        value of session bankrupcy (in base currency; bankruptcy only)  # noqa: E501

        :param session_bankrupcy: The session_bankrupcy of this Settlement.  # noqa: E501
        :type: float
        """

        self._session_bankrupcy = session_bankrupcy

    @property
    def timestamp(self):
        """Gets the timestamp of this Settlement.  # noqa: E501

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :return: The timestamp of this Settlement.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Settlement.

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :param timestamp: The timestamp of this Settlement.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def profit_loss(self):
        """Gets the profit_loss of this Settlement.  # noqa: E501

        profit and loss (in base currency; settlement and delivery only)  # noqa: E501

        :return: The profit_loss of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._profit_loss

    @profit_loss.setter
    def profit_loss(self, profit_loss):
        """Sets the profit_loss of this Settlement.

        profit and loss (in base currency; settlement and delivery only)  # noqa: E501

        :param profit_loss: The profit_loss of this Settlement.  # noqa: E501
        :type: float
        """

        self._profit_loss = profit_loss

    @property
    def funded(self):
        """Gets the funded of this Settlement.  # noqa: E501

        funded amount (bankruptcy only)  # noqa: E501

        :return: The funded of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._funded

    @funded.setter
    def funded(self, funded):
        """Sets the funded of this Settlement.

        funded amount (bankruptcy only)  # noqa: E501

        :param funded: The funded of this Settlement.  # noqa: E501
        :type: float
        """

        self._funded = funded

    @property
    def index_price(self):
        """Gets the index_price of this Settlement.  # noqa: E501

        underlying index price at time of event (in quote currency; settlement and delivery only)  # noqa: E501

        :return: The index_price of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this Settlement.

        underlying index price at time of event (in quote currency; settlement and delivery only)  # noqa: E501

        :param index_price: The index_price of this Settlement.  # noqa: E501
        :type: float
        """
        if index_price is None:
            raise ValueError("Invalid value for `index_price`, must not be `None`")  # noqa: E501

        self._index_price = index_price

    @property
    def session_tax(self):
        """Gets the session_tax of this Settlement.  # noqa: E501

        total amount of paid taxes/fees (in base currency; bankruptcy only)  # noqa: E501

        :return: The session_tax of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._session_tax

    @session_tax.setter
    def session_tax(self, session_tax):
        """Sets the session_tax of this Settlement.

        total amount of paid taxes/fees (in base currency; bankruptcy only)  # noqa: E501

        :param session_tax: The session_tax of this Settlement.  # noqa: E501
        :type: float
        """

        self._session_tax = session_tax

    @property
    def session_tax_rate(self):
        """Gets the session_tax_rate of this Settlement.  # noqa: E501

        rate of paid texes/fees (in base currency; bankruptcy only)  # noqa: E501

        :return: The session_tax_rate of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._session_tax_rate

    @session_tax_rate.setter
    def session_tax_rate(self, session_tax_rate):
        """Sets the session_tax_rate of this Settlement.

        rate of paid texes/fees (in base currency; bankruptcy only)  # noqa: E501

        :param session_tax_rate: The session_tax_rate of this Settlement.  # noqa: E501
        :type: float
        """

        self._session_tax_rate = session_tax_rate

    @property
    def instrument_name(self):
        """Gets the instrument_name of this Settlement.  # noqa: E501

        instrument name (settlement and delivery only)  # noqa: E501

        :return: The instrument_name of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, instrument_name):
        """Sets the instrument_name of this Settlement.

        instrument name (settlement and delivery only)  # noqa: E501

        :param instrument_name: The instrument_name of this Settlement.  # noqa: E501
        :type: str
        """
        if instrument_name is None:
            raise ValueError("Invalid value for `instrument_name`, must not be `None`")  # noqa: E501

        self._instrument_name = instrument_name

    @property
    def position(self):
        """Gets the position of this Settlement.  # noqa: E501

        position size (in quote currency; settlement and delivery only)  # noqa: E501

        :return: The position of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Settlement.

        position size (in quote currency; settlement and delivery only)  # noqa: E501

        :param position: The position of this Settlement.  # noqa: E501
        :type: float
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def type(self):
        """Gets the type of this Settlement.  # noqa: E501

        The type of settlement. `settlement`, `delivery` or `bankruptcy`.  # noqa: E501

        :return: The type of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Settlement.

        The type of settlement. `settlement`, `delivery` or `bankruptcy`.  # noqa: E501

        :param type: The type of this Settlement.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["settlement", "delivery", "bankruptcy"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, Settlement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
