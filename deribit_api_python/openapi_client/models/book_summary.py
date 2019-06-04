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


class BookSummary(object):
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
        'underlying_index': 'str',
        'volume': 'float',
        'volume_usd': 'float',
        'underlying_price': 'float',
        'bid_price': 'float',
        'open_interest': 'float',
        'quote_currency': 'str',
        'high': 'float',
        'estimated_delivery_price': 'float',
        'last': 'float',
        'mid_price': 'float',
        'interest_rate': 'float',
        'funding_8h': 'float',
        'mark_price': 'float',
        'ask_price': 'float',
        'instrument_name': 'str',
        'low': 'float',
        'base_currency': 'str',
        'creation_timestamp': 'int',
        'current_funding': 'float'
    }

    attribute_map = {
        'underlying_index': 'underlying_index',
        'volume': 'volume',
        'volume_usd': 'volume_usd',
        'underlying_price': 'underlying_price',
        'bid_price': 'bid_price',
        'open_interest': 'open_interest',
        'quote_currency': 'quote_currency',
        'high': 'high',
        'estimated_delivery_price': 'estimated_delivery_price',
        'last': 'last',
        'mid_price': 'mid_price',
        'interest_rate': 'interest_rate',
        'funding_8h': 'funding_8h',
        'mark_price': 'mark_price',
        'ask_price': 'ask_price',
        'instrument_name': 'instrument_name',
        'low': 'low',
        'base_currency': 'base_currency',
        'creation_timestamp': 'creation_timestamp',
        'current_funding': 'current_funding'
    }

    def __init__(self, underlying_index=None, volume=None, volume_usd=None, underlying_price=None, bid_price=None, open_interest=None, quote_currency=None, high=None, estimated_delivery_price=None, last=None, mid_price=None, interest_rate=None, funding_8h=None, mark_price=None, ask_price=None, instrument_name=None, low=None, base_currency=None, creation_timestamp=None, current_funding=None):  # noqa: E501
        """BookSummary - a model defined in OpenAPI"""  # noqa: E501

        self._underlying_index = None
        self._volume = None
        self._volume_usd = None
        self._underlying_price = None
        self._bid_price = None
        self._open_interest = None
        self._quote_currency = None
        self._high = None
        self._estimated_delivery_price = None
        self._last = None
        self._mid_price = None
        self._interest_rate = None
        self._funding_8h = None
        self._mark_price = None
        self._ask_price = None
        self._instrument_name = None
        self._low = None
        self._base_currency = None
        self._creation_timestamp = None
        self._current_funding = None
        self.discriminator = None

        if underlying_index is not None:
            self.underlying_index = underlying_index
        self.volume = volume
        if volume_usd is not None:
            self.volume_usd = volume_usd
        if underlying_price is not None:
            self.underlying_price = underlying_price
        self.bid_price = bid_price
        self.open_interest = open_interest
        self.quote_currency = quote_currency
        self.high = high
        if estimated_delivery_price is not None:
            self.estimated_delivery_price = estimated_delivery_price
        self.last = last
        self.mid_price = mid_price
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if funding_8h is not None:
            self.funding_8h = funding_8h
        self.mark_price = mark_price
        self.ask_price = ask_price
        self.instrument_name = instrument_name
        self.low = low
        if base_currency is not None:
            self.base_currency = base_currency
        self.creation_timestamp = creation_timestamp
        if current_funding is not None:
            self.current_funding = current_funding

    @property
    def underlying_index(self):
        """Gets the underlying_index of this BookSummary.  # noqa: E501

        Name of the underlying future, or `'index_price'` (options only)  # noqa: E501

        :return: The underlying_index of this BookSummary.  # noqa: E501
        :rtype: str
        """
        return self._underlying_index

    @underlying_index.setter
    def underlying_index(self, underlying_index):
        """Sets the underlying_index of this BookSummary.

        Name of the underlying future, or `'index_price'` (options only)  # noqa: E501

        :param underlying_index: The underlying_index of this BookSummary.  # noqa: E501
        :type: str
        """

        self._underlying_index = underlying_index

    @property
    def volume(self):
        """Gets the volume of this BookSummary.  # noqa: E501

        The total 24h traded volume (in base currency)  # noqa: E501

        :return: The volume of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this BookSummary.

        The total 24h traded volume (in base currency)  # noqa: E501

        :param volume: The volume of this BookSummary.  # noqa: E501
        :type: float
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def volume_usd(self):
        """Gets the volume_usd of this BookSummary.  # noqa: E501

        Volume in usd (futures only)  # noqa: E501

        :return: The volume_usd of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._volume_usd

    @volume_usd.setter
    def volume_usd(self, volume_usd):
        """Sets the volume_usd of this BookSummary.

        Volume in usd (futures only)  # noqa: E501

        :param volume_usd: The volume_usd of this BookSummary.  # noqa: E501
        :type: float
        """

        self._volume_usd = volume_usd

    @property
    def underlying_price(self):
        """Gets the underlying_price of this BookSummary.  # noqa: E501

        underlying price for implied volatility calculations (options only)  # noqa: E501

        :return: The underlying_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._underlying_price

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this BookSummary.

        underlying price for implied volatility calculations (options only)  # noqa: E501

        :param underlying_price: The underlying_price of this BookSummary.  # noqa: E501
        :type: float
        """

        self._underlying_price = underlying_price

    @property
    def bid_price(self):
        """Gets the bid_price of this BookSummary.  # noqa: E501

        The current best bid price, `null` if there aren't any bids  # noqa: E501

        :return: The bid_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._bid_price

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this BookSummary.

        The current best bid price, `null` if there aren't any bids  # noqa: E501

        :param bid_price: The bid_price of this BookSummary.  # noqa: E501
        :type: float
        """
        if bid_price is None:
            raise ValueError("Invalid value for `bid_price`, must not be `None`")  # noqa: E501

        self._bid_price = bid_price

    @property
    def open_interest(self):
        """Gets the open_interest of this BookSummary.  # noqa: E501

        The total amount of outstanding contracts in the corresponding amount units. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :return: The open_interest of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._open_interest

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this BookSummary.

        The total amount of outstanding contracts in the corresponding amount units. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :param open_interest: The open_interest of this BookSummary.  # noqa: E501
        :type: float
        """
        if open_interest is None:
            raise ValueError("Invalid value for `open_interest`, must not be `None`")  # noqa: E501

        self._open_interest = open_interest

    @property
    def quote_currency(self):
        """Gets the quote_currency of this BookSummary.  # noqa: E501

        Quote currency  # noqa: E501

        :return: The quote_currency of this BookSummary.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this BookSummary.

        Quote currency  # noqa: E501

        :param quote_currency: The quote_currency of this BookSummary.  # noqa: E501
        :type: str
        """
        if quote_currency is None:
            raise ValueError("Invalid value for `quote_currency`, must not be `None`")  # noqa: E501

        self._quote_currency = quote_currency

    @property
    def high(self):
        """Gets the high of this BookSummary.  # noqa: E501

        Price of the 24h highest trade  # noqa: E501

        :return: The high of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this BookSummary.

        Price of the 24h highest trade  # noqa: E501

        :param high: The high of this BookSummary.  # noqa: E501
        :type: float
        """
        if high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501

        self._high = high

    @property
    def estimated_delivery_price(self):
        """Gets the estimated_delivery_price of this BookSummary.  # noqa: E501

        Estimated delivery price, in USD (futures only). For more details, see Documentation > General > Expiration Price  # noqa: E501

        :return: The estimated_delivery_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._estimated_delivery_price

    @estimated_delivery_price.setter
    def estimated_delivery_price(self, estimated_delivery_price):
        """Sets the estimated_delivery_price of this BookSummary.

        Estimated delivery price, in USD (futures only). For more details, see Documentation > General > Expiration Price  # noqa: E501

        :param estimated_delivery_price: The estimated_delivery_price of this BookSummary.  # noqa: E501
        :type: float
        """

        self._estimated_delivery_price = estimated_delivery_price

    @property
    def last(self):
        """Gets the last of this BookSummary.  # noqa: E501

        The price of the latest trade, `null` if there weren't any trades  # noqa: E501

        :return: The last of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this BookSummary.

        The price of the latest trade, `null` if there weren't any trades  # noqa: E501

        :param last: The last of this BookSummary.  # noqa: E501
        :type: float
        """
        if last is None:
            raise ValueError("Invalid value for `last`, must not be `None`")  # noqa: E501

        self._last = last

    @property
    def mid_price(self):
        """Gets the mid_price of this BookSummary.  # noqa: E501

        The average of the best bid and ask, `null` if there aren't any asks or bids  # noqa: E501

        :return: The mid_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._mid_price

    @mid_price.setter
    def mid_price(self, mid_price):
        """Sets the mid_price of this BookSummary.

        The average of the best bid and ask, `null` if there aren't any asks or bids  # noqa: E501

        :param mid_price: The mid_price of this BookSummary.  # noqa: E501
        :type: float
        """
        if mid_price is None:
            raise ValueError("Invalid value for `mid_price`, must not be `None`")  # noqa: E501

        self._mid_price = mid_price

    @property
    def interest_rate(self):
        """Gets the interest_rate of this BookSummary.  # noqa: E501

        Interest rate used in implied volatility calculations (options only)  # noqa: E501

        :return: The interest_rate of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this BookSummary.

        Interest rate used in implied volatility calculations (options only)  # noqa: E501

        :param interest_rate: The interest_rate of this BookSummary.  # noqa: E501
        :type: float
        """

        self._interest_rate = interest_rate

    @property
    def funding_8h(self):
        """Gets the funding_8h of this BookSummary.  # noqa: E501

        Funding 8h (perpetual only)  # noqa: E501

        :return: The funding_8h of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._funding_8h

    @funding_8h.setter
    def funding_8h(self, funding_8h):
        """Sets the funding_8h of this BookSummary.

        Funding 8h (perpetual only)  # noqa: E501

        :param funding_8h: The funding_8h of this BookSummary.  # noqa: E501
        :type: float
        """

        self._funding_8h = funding_8h

    @property
    def mark_price(self):
        """Gets the mark_price of this BookSummary.  # noqa: E501

        The current instrument market price  # noqa: E501

        :return: The mark_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this BookSummary.

        The current instrument market price  # noqa: E501

        :param mark_price: The mark_price of this BookSummary.  # noqa: E501
        :type: float
        """
        if mark_price is None:
            raise ValueError("Invalid value for `mark_price`, must not be `None`")  # noqa: E501

        self._mark_price = mark_price

    @property
    def ask_price(self):
        """Gets the ask_price of this BookSummary.  # noqa: E501

        The current best ask price, `null` if there aren't any asks  # noqa: E501

        :return: The ask_price of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._ask_price

    @ask_price.setter
    def ask_price(self, ask_price):
        """Sets the ask_price of this BookSummary.

        The current best ask price, `null` if there aren't any asks  # noqa: E501

        :param ask_price: The ask_price of this BookSummary.  # noqa: E501
        :type: float
        """
        if ask_price is None:
            raise ValueError("Invalid value for `ask_price`, must not be `None`")  # noqa: E501

        self._ask_price = ask_price

    @property
    def instrument_name(self):
        """Gets the instrument_name of this BookSummary.  # noqa: E501

        Unique instrument identifier  # noqa: E501

        :return: The instrument_name of this BookSummary.  # noqa: E501
        :rtype: str
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, instrument_name):
        """Sets the instrument_name of this BookSummary.

        Unique instrument identifier  # noqa: E501

        :param instrument_name: The instrument_name of this BookSummary.  # noqa: E501
        :type: str
        """
        if instrument_name is None:
            raise ValueError("Invalid value for `instrument_name`, must not be `None`")  # noqa: E501

        self._instrument_name = instrument_name

    @property
    def low(self):
        """Gets the low of this BookSummary.  # noqa: E501

        Price of the 24h lowest trade, `null` if there weren't any trades  # noqa: E501

        :return: The low of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this BookSummary.

        Price of the 24h lowest trade, `null` if there weren't any trades  # noqa: E501

        :param low: The low of this BookSummary.  # noqa: E501
        :type: float
        """
        if low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501

        self._low = low

    @property
    def base_currency(self):
        """Gets the base_currency of this BookSummary.  # noqa: E501

        Base currency  # noqa: E501

        :return: The base_currency of this BookSummary.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this BookSummary.

        Base currency  # noqa: E501

        :param base_currency: The base_currency of this BookSummary.  # noqa: E501
        :type: str
        """

        self._base_currency = base_currency

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this BookSummary.  # noqa: E501

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :return: The creation_timestamp of this BookSummary.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this BookSummary.

        The timestamp (seconds since the Unix epoch, with millisecond precision)  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this BookSummary.  # noqa: E501
        :type: int
        """
        if creation_timestamp is None:
            raise ValueError("Invalid value for `creation_timestamp`, must not be `None`")  # noqa: E501

        self._creation_timestamp = creation_timestamp

    @property
    def current_funding(self):
        """Gets the current_funding of this BookSummary.  # noqa: E501

        Current funding (perpetual only)  # noqa: E501

        :return: The current_funding of this BookSummary.  # noqa: E501
        :rtype: float
        """
        return self._current_funding

    @current_funding.setter
    def current_funding(self, current_funding):
        """Sets the current_funding of this BookSummary.

        Current funding (perpetual only)  # noqa: E501

        :param current_funding: The current_funding of this BookSummary.  # noqa: E501
        :type: float
        """

        self._current_funding = current_funding

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
        if not isinstance(other, BookSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
