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


class Instrument(object):
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
        'quote_currency': 'str',
        'kind': 'str',
        'tick_size': 'float',
        'contract_size': 'int',
        'is_active': 'bool',
        'option_type': 'str',
        'min_trade_amount': 'float',
        'instrument_name': 'str',
        'settlement_period': 'str',
        'strike': 'float',
        'base_currency': 'str',
        'creation_timestamp': 'int',
        'expiration_timestamp': 'int'
    }

    attribute_map = {
        'quote_currency': 'quote_currency',
        'kind': 'kind',
        'tick_size': 'tick_size',
        'contract_size': 'contract_size',
        'is_active': 'is_active',
        'option_type': 'option_type',
        'min_trade_amount': 'min_trade_amount',
        'instrument_name': 'instrument_name',
        'settlement_period': 'settlement_period',
        'strike': 'strike',
        'base_currency': 'base_currency',
        'creation_timestamp': 'creation_timestamp',
        'expiration_timestamp': 'expiration_timestamp'
    }

    def __init__(self, quote_currency=None, kind=None, tick_size=None, contract_size=None, is_active=None, option_type=None, min_trade_amount=None, instrument_name=None, settlement_period=None, strike=None, base_currency=None, creation_timestamp=None, expiration_timestamp=None):  # noqa: E501
        """Instrument - a model defined in OpenAPI"""  # noqa: E501

        self._quote_currency = None
        self._kind = None
        self._tick_size = None
        self._contract_size = None
        self._is_active = None
        self._option_type = None
        self._min_trade_amount = None
        self._instrument_name = None
        self._settlement_period = None
        self._strike = None
        self._base_currency = None
        self._creation_timestamp = None
        self._expiration_timestamp = None
        self.discriminator = None

        self.quote_currency = quote_currency
        self.kind = kind
        self.tick_size = tick_size
        self.contract_size = contract_size
        self.is_active = is_active
        if option_type is not None:
            self.option_type = option_type
        self.min_trade_amount = min_trade_amount
        self.instrument_name = instrument_name
        self.settlement_period = settlement_period
        if strike is not None:
            self.strike = strike
        self.base_currency = base_currency
        self.creation_timestamp = creation_timestamp
        self.expiration_timestamp = expiration_timestamp

    @property
    def quote_currency(self):
        """Gets the quote_currency of this Instrument.  # noqa: E501

        The currency in which the instrument prices are quoted.  # noqa: E501

        :return: The quote_currency of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this Instrument.

        The currency in which the instrument prices are quoted.  # noqa: E501

        :param quote_currency: The quote_currency of this Instrument.  # noqa: E501
        :type: str
        """
        if quote_currency is None:
            raise ValueError("Invalid value for `quote_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["USD"]  # noqa: E501
        if quote_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `quote_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_currency, allowed_values)
            )

        self._quote_currency = quote_currency

    @property
    def kind(self):
        """Gets the kind of this Instrument.  # noqa: E501

        Instrument kind, `\"future\"` or `\"option\"`  # noqa: E501

        :return: The kind of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Instrument.

        Instrument kind, `\"future\"` or `\"option\"`  # noqa: E501

        :param kind: The kind of this Instrument.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["future", "option"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def tick_size(self):
        """Gets the tick_size of this Instrument.  # noqa: E501

        specifies minimal price change and, as follows, the number of decimal places for instrument prices  # noqa: E501

        :return: The tick_size of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._tick_size

    @tick_size.setter
    def tick_size(self, tick_size):
        """Sets the tick_size of this Instrument.

        specifies minimal price change and, as follows, the number of decimal places for instrument prices  # noqa: E501

        :param tick_size: The tick_size of this Instrument.  # noqa: E501
        :type: float
        """
        if tick_size is None:
            raise ValueError("Invalid value for `tick_size`, must not be `None`")  # noqa: E501

        self._tick_size = tick_size

    @property
    def contract_size(self):
        """Gets the contract_size of this Instrument.  # noqa: E501

        Contract size for instrument  # noqa: E501

        :return: The contract_size of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this Instrument.

        Contract size for instrument  # noqa: E501

        :param contract_size: The contract_size of this Instrument.  # noqa: E501
        :type: int
        """
        if contract_size is None:
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def is_active(self):
        """Gets the is_active of this Instrument.  # noqa: E501

        Indicates if the instrument can currently be traded.  # noqa: E501

        :return: The is_active of this Instrument.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Instrument.

        Indicates if the instrument can currently be traded.  # noqa: E501

        :param is_active: The is_active of this Instrument.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def option_type(self):
        """Gets the option_type of this Instrument.  # noqa: E501

        The option type (only for options)  # noqa: E501

        :return: The option_type of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this Instrument.

        The option type (only for options)  # noqa: E501

        :param option_type: The option_type of this Instrument.  # noqa: E501
        :type: str
        """
        allowed_values = ["call", "put"]  # noqa: E501
        if option_type not in allowed_values:
            raise ValueError(
                "Invalid value for `option_type` ({0}), must be one of {1}"  # noqa: E501
                .format(option_type, allowed_values)
            )

        self._option_type = option_type

    @property
    def min_trade_amount(self):
        """Gets the min_trade_amount of this Instrument.  # noqa: E501

        Minimum amount for trading. For perpetual and futures - in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :return: The min_trade_amount of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._min_trade_amount

    @min_trade_amount.setter
    def min_trade_amount(self, min_trade_amount):
        """Sets the min_trade_amount of this Instrument.

        Minimum amount for trading. For perpetual and futures - in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.  # noqa: E501

        :param min_trade_amount: The min_trade_amount of this Instrument.  # noqa: E501
        :type: float
        """
        if min_trade_amount is None:
            raise ValueError("Invalid value for `min_trade_amount`, must not be `None`")  # noqa: E501

        self._min_trade_amount = min_trade_amount

    @property
    def instrument_name(self):
        """Gets the instrument_name of this Instrument.  # noqa: E501

        Unique instrument identifier  # noqa: E501

        :return: The instrument_name of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, instrument_name):
        """Sets the instrument_name of this Instrument.

        Unique instrument identifier  # noqa: E501

        :param instrument_name: The instrument_name of this Instrument.  # noqa: E501
        :type: str
        """
        if instrument_name is None:
            raise ValueError("Invalid value for `instrument_name`, must not be `None`")  # noqa: E501

        self._instrument_name = instrument_name

    @property
    def settlement_period(self):
        """Gets the settlement_period of this Instrument.  # noqa: E501

        The settlement period.  # noqa: E501

        :return: The settlement_period of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this Instrument.

        The settlement period.  # noqa: E501

        :param settlement_period: The settlement_period of this Instrument.  # noqa: E501
        :type: str
        """
        if settlement_period is None:
            raise ValueError("Invalid value for `settlement_period`, must not be `None`")  # noqa: E501
        allowed_values = ["month", "week", "perpetual"]  # noqa: E501
        if settlement_period not in allowed_values:
            raise ValueError(
                "Invalid value for `settlement_period` ({0}), must be one of {1}"  # noqa: E501
                .format(settlement_period, allowed_values)
            )

        self._settlement_period = settlement_period

    @property
    def strike(self):
        """Gets the strike of this Instrument.  # noqa: E501

        The strike value. (only for options)  # noqa: E501

        :return: The strike of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this Instrument.

        The strike value. (only for options)  # noqa: E501

        :param strike: The strike of this Instrument.  # noqa: E501
        :type: float
        """

        self._strike = strike

    @property
    def base_currency(self):
        """Gets the base_currency of this Instrument.  # noqa: E501

        The underlying currency being traded.  # noqa: E501

        :return: The base_currency of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this Instrument.

        The underlying currency being traded.  # noqa: E501

        :param base_currency: The base_currency of this Instrument.  # noqa: E501
        :type: str
        """
        if base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["BTC", "ETH"]  # noqa: E501
        if base_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `base_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(base_currency, allowed_values)
            )

        self._base_currency = base_currency

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Instrument.  # noqa: E501

        The time when the instrument was first created (milliseconds)  # noqa: E501

        :return: The creation_timestamp of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Instrument.

        The time when the instrument was first created (milliseconds)  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this Instrument.  # noqa: E501
        :type: int
        """
        if creation_timestamp is None:
            raise ValueError("Invalid value for `creation_timestamp`, must not be `None`")  # noqa: E501

        self._creation_timestamp = creation_timestamp

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this Instrument.  # noqa: E501

        The time when the instrument will expire (milliseconds)  # noqa: E501

        :return: The expiration_timestamp of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this Instrument.

        The time when the instrument will expire (milliseconds)  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this Instrument.  # noqa: E501
        :type: int
        """
        if expiration_timestamp is None:
            raise ValueError("Invalid value for `expiration_timestamp`, must not be `None`")  # noqa: E501

        self._expiration_timestamp = expiration_timestamp

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
        if not isinstance(other, Instrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
