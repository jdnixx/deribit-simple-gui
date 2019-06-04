# openapi_client.PrivateApi

All URIs are relative to *https://www.deribit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_add_to_address_book_get**](PrivateApi.md#private_add_to_address_book_get) | **GET** /private/add_to_address_book | Adds new entry to address book of given type
[**private_buy_get**](PrivateApi.md#private_buy_get) | **GET** /private/buy | Places a buy order for an instrument.
[**private_cancel_all_by_currency_get**](PrivateApi.md#private_cancel_all_by_currency_get) | **GET** /private/cancel_all_by_currency | Cancels all orders by currency, optionally filtered by instrument kind and/or order type.
[**private_cancel_all_by_instrument_get**](PrivateApi.md#private_cancel_all_by_instrument_get) | **GET** /private/cancel_all_by_instrument | Cancels all orders by instrument, optionally filtered by order type.
[**private_cancel_all_get**](PrivateApi.md#private_cancel_all_get) | **GET** /private/cancel_all | This method cancels all users orders and stop orders within all currencies and instrument kinds.
[**private_cancel_get**](PrivateApi.md#private_cancel_get) | **GET** /private/cancel | Cancel an order, specified by order id
[**private_cancel_transfer_by_id_get**](PrivateApi.md#private_cancel_transfer_by_id_get) | **GET** /private/cancel_transfer_by_id | Cancel transfer
[**private_cancel_withdrawal_get**](PrivateApi.md#private_cancel_withdrawal_get) | **GET** /private/cancel_withdrawal | Cancels withdrawal request
[**private_change_subaccount_name_get**](PrivateApi.md#private_change_subaccount_name_get) | **GET** /private/change_subaccount_name | Change the user name for a subaccount
[**private_close_position_get**](PrivateApi.md#private_close_position_get) | **GET** /private/close_position | Makes closing position reduce only order .
[**private_create_deposit_address_get**](PrivateApi.md#private_create_deposit_address_get) | **GET** /private/create_deposit_address | Creates deposit address in currency
[**private_create_subaccount_get**](PrivateApi.md#private_create_subaccount_get) | **GET** /private/create_subaccount | Create a new subaccount
[**private_disable_cancel_on_disconnect_get**](PrivateApi.md#private_disable_cancel_on_disconnect_get) | **GET** /private/disable_cancel_on_disconnect | Disable Cancel On Disconnect for the connection. This does not change the default account setting.
[**private_disable_tfa_for_subaccount_get**](PrivateApi.md#private_disable_tfa_for_subaccount_get) | **GET** /private/disable_tfa_for_subaccount | Disable two factor authentication for a subaccount.
[**private_disable_tfa_with_recovery_code_get**](PrivateApi.md#private_disable_tfa_with_recovery_code_get) | **GET** /private/disable_tfa_with_recovery_code | Disables TFA with one time recovery code
[**private_edit_get**](PrivateApi.md#private_edit_get) | **GET** /private/edit | Change price, amount and/or other properties of an order.
[**private_enable_cancel_on_disconnect_get**](PrivateApi.md#private_enable_cancel_on_disconnect_get) | **GET** /private/enable_cancel_on_disconnect | Enable Cancel On Disconnect for the connection. This does not change the default account setting.
[**private_get_account_summary_get**](PrivateApi.md#private_get_account_summary_get) | **GET** /private/get_account_summary | Retrieves user account summary.
[**private_get_address_book_get**](PrivateApi.md#private_get_address_book_get) | **GET** /private/get_address_book | Retrieves address book of given type
[**private_get_current_deposit_address_get**](PrivateApi.md#private_get_current_deposit_address_get) | **GET** /private/get_current_deposit_address | Retrieve deposit address for currency
[**private_get_deposits_get**](PrivateApi.md#private_get_deposits_get) | **GET** /private/get_deposits | Retrieve the latest users deposits
[**private_get_email_language_get**](PrivateApi.md#private_get_email_language_get) | **GET** /private/get_email_language | Retrieves the language to be used for emails.
[**private_get_margins_get**](PrivateApi.md#private_get_margins_get) | **GET** /private/get_margins | Get margins for given instrument, amount and price.
[**private_get_new_announcements_get**](PrivateApi.md#private_get_new_announcements_get) | **GET** /private/get_new_announcements | Retrieves announcements that have not been marked read by the user.
[**private_get_open_orders_by_currency_get**](PrivateApi.md#private_get_open_orders_by_currency_get) | **GET** /private/get_open_orders_by_currency | Retrieves list of user&#39;s open orders.
[**private_get_open_orders_by_instrument_get**](PrivateApi.md#private_get_open_orders_by_instrument_get) | **GET** /private/get_open_orders_by_instrument | Retrieves list of user&#39;s open orders within given Instrument.
[**private_get_order_history_by_currency_get**](PrivateApi.md#private_get_order_history_by_currency_get) | **GET** /private/get_order_history_by_currency | Retrieves history of orders that have been partially or fully filled.
[**private_get_order_history_by_instrument_get**](PrivateApi.md#private_get_order_history_by_instrument_get) | **GET** /private/get_order_history_by_instrument | Retrieves history of orders that have been partially or fully filled.
[**private_get_order_margin_by_ids_get**](PrivateApi.md#private_get_order_margin_by_ids_get) | **GET** /private/get_order_margin_by_ids | Retrieves initial margins of given orders
[**private_get_order_state_get**](PrivateApi.md#private_get_order_state_get) | **GET** /private/get_order_state | Retrieve the current state of an order.
[**private_get_position_get**](PrivateApi.md#private_get_position_get) | **GET** /private/get_position | Retrieve user position.
[**private_get_positions_get**](PrivateApi.md#private_get_positions_get) | **GET** /private/get_positions | Retrieve user positions.
[**private_get_settlement_history_by_currency_get**](PrivateApi.md#private_get_settlement_history_by_currency_get) | **GET** /private/get_settlement_history_by_currency | Retrieves settlement, delivery and bankruptcy events that have affected your account.
[**private_get_settlement_history_by_instrument_get**](PrivateApi.md#private_get_settlement_history_by_instrument_get) | **GET** /private/get_settlement_history_by_instrument | Retrieves public settlement, delivery and bankruptcy events filtered by instrument name
[**private_get_subaccounts_get**](PrivateApi.md#private_get_subaccounts_get) | **GET** /private/get_subaccounts | Get information about subaccounts
[**private_get_transfers_get**](PrivateApi.md#private_get_transfers_get) | **GET** /private/get_transfers | Adds new entry to address book of given type
[**private_get_user_trades_by_currency_and_time_get**](PrivateApi.md#private_get_user_trades_by_currency_and_time_get) | **GET** /private/get_user_trades_by_currency_and_time | Retrieve the latest user trades that have occurred for instruments in a specific currency symbol and within given time range.
[**private_get_user_trades_by_currency_get**](PrivateApi.md#private_get_user_trades_by_currency_get) | **GET** /private/get_user_trades_by_currency | Retrieve the latest user trades that have occurred for instruments in a specific currency symbol.
[**private_get_user_trades_by_instrument_and_time_get**](PrivateApi.md#private_get_user_trades_by_instrument_and_time_get) | **GET** /private/get_user_trades_by_instrument_and_time | Retrieve the latest user trades that have occurred for a specific instrument and within given time range.
[**private_get_user_trades_by_instrument_get**](PrivateApi.md#private_get_user_trades_by_instrument_get) | **GET** /private/get_user_trades_by_instrument | Retrieve the latest user trades that have occurred for a specific instrument.
[**private_get_user_trades_by_order_get**](PrivateApi.md#private_get_user_trades_by_order_get) | **GET** /private/get_user_trades_by_order | Retrieve the list of user trades that was created for given order
[**private_get_withdrawals_get**](PrivateApi.md#private_get_withdrawals_get) | **GET** /private/get_withdrawals | Retrieve the latest users withdrawals
[**private_logout_get**](PrivateApi.md#private_logout_get) | **GET** /private/logout | Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
[**private_remove_from_address_book_get**](PrivateApi.md#private_remove_from_address_book_get) | **GET** /private/remove_from_address_book | Adds new entry to address book of given type
[**private_sell_get**](PrivateApi.md#private_sell_get) | **GET** /private/sell | Places a sell order for an instrument.
[**private_set_announcement_as_read_get**](PrivateApi.md#private_set_announcement_as_read_get) | **GET** /private/set_announcement_as_read | Marks an announcement as read, so it will not be shown in &#x60;get_new_announcements&#x60;.
[**private_set_email_for_subaccount_get**](PrivateApi.md#private_set_email_for_subaccount_get) | **GET** /private/set_email_for_subaccount | Assign an email address to a subaccount. User will receive an email with confirmation link.
[**private_set_email_language_get**](PrivateApi.md#private_set_email_language_get) | **GET** /private/set_email_language | Changes the language to be used for emails.
[**private_set_password_for_subaccount_get**](PrivateApi.md#private_set_password_for_subaccount_get) | **GET** /private/set_password_for_subaccount | Set the password for the subaccount
[**private_submit_transfer_to_subaccount_get**](PrivateApi.md#private_submit_transfer_to_subaccount_get) | **GET** /private/submit_transfer_to_subaccount | Transfer funds to a subaccount.
[**private_submit_transfer_to_user_get**](PrivateApi.md#private_submit_transfer_to_user_get) | **GET** /private/submit_transfer_to_user | Transfer funds to a another user.
[**private_subscribe_get**](PrivateApi.md#private_subscribe_get) | **GET** /private/subscribe | Subscribe to one or more channels.
[**private_toggle_deposit_address_creation_get**](PrivateApi.md#private_toggle_deposit_address_creation_get) | **GET** /private/toggle_deposit_address_creation | Enable or disable deposit address creation
[**private_toggle_notifications_from_subaccount_get**](PrivateApi.md#private_toggle_notifications_from_subaccount_get) | **GET** /private/toggle_notifications_from_subaccount | Enable or disable sending of notifications for the subaccount.
[**private_toggle_subaccount_login_get**](PrivateApi.md#private_toggle_subaccount_login_get) | **GET** /private/toggle_subaccount_login | Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.
[**private_unsubscribe_get**](PrivateApi.md#private_unsubscribe_get) | **GET** /private/unsubscribe | Unsubscribe from one or more channels.
[**private_withdraw_get**](PrivateApi.md#private_withdraw_get) | **GET** /private/withdraw | Creates a new withdrawal request


# **private_add_to_address_book_get**
> object private_add_to_address_book_get(currency, type, address, name, tfa=tfa)

Adds new entry to address book of given type

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type
address = 'address_example' # str | Address in currency format, it must be in address book
name = 'Main address' # str | Name of address book entry
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_add_to_address_book_get(currency, type, address, name, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_add_to_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **name** | **str**| Name of address book entry | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_buy_get**
> object private_buy_get(instrument_name, amount, type=type, label=label, price=price, time_in_force=time_in_force, max_show=max_show, post_only=post_only, reduce_only=reduce_only, stop_price=stop_price, trigger=trigger, advanced=advanced)

Places a buy order for an instrument.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
amount = 3.4 # float | It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH
type = 'type_example' # str | The order type, default: `\"limit\"` (optional)
label = 'label_example' # str | user defined label for the order (maximum 32 characters) (optional)
price = 3.4 # float | <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p> (optional)
time_in_force = 'good_til_cancelled' # str | <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul> (optional) (default to 'good_til_cancelled')
max_show = 1 # float | Maximum amount within an order to be shown to other customers, `0` for invisible order (optional) (default to 1)
post_only = True # bool | <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p> (optional) (default to True)
reduce_only = False # bool | If `true`, the order is considered reduce-only which is intended to only reduce a current position (optional) (default to False)
stop_price = 3.4 # float | Stop price, required for stop limit orders (Only for stop orders) (optional)
trigger = 'trigger_example' # str | Defines trigger type, required for `\"stop_limit\"` order type (optional)
advanced = 'advanced_example' # str | Advanced option order type. (Only for options) (optional)

try:
    # Places a buy order for an instrument.
    api_response = api_instance.private_buy_get(instrument_name, amount, type=type, label=label, price=price, time_in_force=time_in_force, max_show=max_show, post_only=post_only, reduce_only=reduce_only, stop_price=stop_price, trigger=trigger, advanced=advanced)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_buy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **amount** | **float**| It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH | 
 **type** | **str**| The order type, default: &#x60;\&quot;limit\&quot;&#x60; | [optional] 
 **label** | **str**| user defined label for the order (maximum 32 characters) | [optional] 
 **price** | **float**| &lt;p&gt;The order price in base currency (Only for limit and stop_limit orders)&lt;/p&gt; &lt;p&gt;When adding order with advanced&#x3D;usd, the field price should be the option price value in USD.&lt;/p&gt; &lt;p&gt;When adding order with advanced&#x3D;implv, the field price should be a value of implied volatility in percentages. For example,  price&#x3D;100, means implied volatility of 100%&lt;/p&gt; | [optional] 
 **time_in_force** | **str**| &lt;p&gt;Specifies how long the order remains in effect. Default &#x60;\&quot;good_til_cancelled\&quot;&#x60;&lt;/p&gt; &lt;ul&gt; &lt;li&gt;&#x60;\&quot;good_til_cancelled\&quot;&#x60; - unfilled order remains in order book until cancelled&lt;/li&gt; &lt;li&gt;&#x60;\&quot;fill_or_kill\&quot;&#x60; - execute a transaction immediately and completely or not at all&lt;/li&gt; &lt;li&gt;&#x60;\&quot;immediate_or_cancel\&quot;&#x60; - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;good_til_cancelled&#39;]
 **max_show** | **float**| Maximum amount within an order to be shown to other customers, &#x60;0&#x60; for invisible order | [optional] [default to 1]
 **post_only** | **bool**| &lt;p&gt;If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.&lt;/p&gt; &lt;p&gt;Only valid in combination with time_in_force&#x3D;&#x60;\&quot;good_til_cancelled\&quot;&#x60;&lt;/p&gt; | [optional] [default to True]
 **reduce_only** | **bool**| If &#x60;true&#x60;, the order is considered reduce-only which is intended to only reduce a current position | [optional] [default to False]
 **stop_price** | **float**| Stop price, required for stop limit orders (Only for stop orders) | [optional] 
 **trigger** | **str**| Defines trigger type, required for &#x60;\&quot;stop_limit\&quot;&#x60; order type | [optional] 
 **advanced** | **str**| Advanced option order type. (Only for options) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_all_by_currency_get**
> object private_cancel_all_by_currency_get(currency, kind=kind, type=type)

Cancels all orders by currency, optionally filtered by instrument kind and/or order type.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
type = 'type_example' # str | Order type - limit, stop or all, default - `all` (optional)

try:
    # Cancels all orders by currency, optionally filtered by instrument kind and/or order type.
    api_response = api_instance.private_cancel_all_by_currency_get(currency, kind=kind, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_all_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **type** | **str**| Order type - limit, stop or all, default - &#x60;all&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_all_by_instrument_get**
> object private_cancel_all_by_instrument_get(instrument_name, type=type)

Cancels all orders by instrument, optionally filtered by order type.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
type = 'type_example' # str | Order type - limit, stop or all, default - `all` (optional)

try:
    # Cancels all orders by instrument, optionally filtered by order type.
    api_response = api_instance.private_cancel_all_by_instrument_get(instrument_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_all_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **type** | **str**| Order type - limit, stop or all, default - &#x60;all&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_all_get**
> object private_cancel_all_get()

This method cancels all users orders and stop orders within all currencies and instrument kinds.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # This method cancels all users orders and stop orders within all currencies and instrument kinds.
    api_response = api_instance.private_cancel_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_all_get: %s\n" % e)
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

# **private_cancel_get**
> object private_cancel_get(order_id)

Cancel an order, specified by order id

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
order_id = 'ETH-100234' # str | The order id

try:
    # Cancel an order, specified by order id
    api_response = api_instance.private_cancel_get(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_transfer_by_id_get**
> object private_cancel_transfer_by_id_get(currency, id, tfa=tfa)

Cancel transfer

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
id = 12 # int | Id of transfer
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Cancel transfer
    api_response = api_instance.private_cancel_transfer_by_id_get(currency, id, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_transfer_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **id** | **int**| Id of transfer | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cancel_withdrawal_get**
> object private_cancel_withdrawal_get(currency, id)

Cancels withdrawal request

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
id = 1 # float | The withdrawal id

try:
    # Cancels withdrawal request
    api_response = api_instance.private_cancel_withdrawal_get(currency, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_cancel_withdrawal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **id** | **float**| The withdrawal id | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_change_subaccount_name_get**
> object private_change_subaccount_name_get(sid, name)

Change the user name for a subaccount

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
name = 'newUserName' # str | The new user name

try:
    # Change the user name for a subaccount
    api_response = api_instance.private_change_subaccount_name_get(sid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_change_subaccount_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **name** | **str**| The new user name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_close_position_get**
> object private_close_position_get(instrument_name, type, price=price)

Makes closing position reduce only order .

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
type = 'type_example' # str | The order type
price = 3.4 # float | Optional price for limit order. (optional)

try:
    # Makes closing position reduce only order .
    api_response = api_instance.private_close_position_get(instrument_name, type, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_close_position_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **type** | **str**| The order type | 
 **price** | **float**| Optional price for limit order. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_create_deposit_address_get**
> object private_create_deposit_address_get(currency)

Creates deposit address in currency

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Creates deposit address in currency
    api_response = api_instance.private_create_deposit_address_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_create_deposit_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_create_subaccount_get**
> object private_create_subaccount_get()

Create a new subaccount

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Create a new subaccount
    api_response = api_instance.private_create_subaccount_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_create_subaccount_get: %s\n" % e)
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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Disable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_disable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_disable_cancel_on_disconnect_get: %s\n" % e)
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

# **private_disable_tfa_for_subaccount_get**
> object private_disable_tfa_for_subaccount_get(sid)

Disable two factor authentication for a subaccount.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount

try:
    # Disable two factor authentication for a subaccount.
    api_response = api_instance.private_disable_tfa_for_subaccount_get(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_disable_tfa_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_disable_tfa_with_recovery_code_get**
> object private_disable_tfa_with_recovery_code_get(password, code)

Disables TFA with one time recovery code

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
password = 'password_example' # str | The password for the subaccount
code = 'code_example' # str | One time recovery code

try:
    # Disables TFA with one time recovery code
    api_response = api_instance.private_disable_tfa_with_recovery_code_get(password, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_disable_tfa_with_recovery_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the subaccount | 
 **code** | **str**| One time recovery code | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_edit_get**
> object private_edit_get(order_id, amount, price, post_only=post_only, advanced=advanced, stop_price=stop_price)

Change price, amount and/or other properties of an order.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
order_id = 'ETH-100234' # str | The order id
amount = 3.4 # float | It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH
price = 3.4 # float | <p>The order price in base currency.</p> <p>When editing an option order with advanced=usd, the field price should be the option price value in USD.</p> <p>When editing an option order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p>
post_only = True # bool | <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p> (optional) (default to True)
advanced = 'advanced_example' # str | Advanced option order type. If you have posted an advanced option order, it is necessary to re-supply this parameter when editing it (Only for options) (optional)
stop_price = 3.4 # float | Stop price, required for stop limit orders (Only for stop orders) (optional)

try:
    # Change price, amount and/or other properties of an order.
    api_response = api_instance.private_edit_get(order_id, amount, price, post_only=post_only, advanced=advanced, stop_price=stop_price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_edit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id | 
 **amount** | **float**| It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH | 
 **price** | **float**| &lt;p&gt;The order price in base currency.&lt;/p&gt; &lt;p&gt;When editing an option order with advanced&#x3D;usd, the field price should be the option price value in USD.&lt;/p&gt; &lt;p&gt;When editing an option order with advanced&#x3D;implv, the field price should be a value of implied volatility in percentages. For example,  price&#x3D;100, means implied volatility of 100%&lt;/p&gt; | 
 **post_only** | **bool**| &lt;p&gt;If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.&lt;/p&gt; &lt;p&gt;Only valid in combination with time_in_force&#x3D;&#x60;\&quot;good_til_cancelled\&quot;&#x60;&lt;/p&gt; | [optional] [default to True]
 **advanced** | **str**| Advanced option order type. If you have posted an advanced option order, it is necessary to re-supply this parameter when editing it (Only for options) | [optional] 
 **stop_price** | **float**| Stop price, required for stop limit orders (Only for stop orders) | [optional] 

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Enable Cancel On Disconnect for the connection. This does not change the default account setting.
    api_response = api_instance.private_enable_cancel_on_disconnect_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_enable_cancel_on_disconnect_get: %s\n" % e)
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

# **private_get_account_summary_get**
> object private_get_account_summary_get(currency, extended=extended)

Retrieves user account summary.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
extended = false # bool | Include additional fields (optional)

try:
    # Retrieves user account summary.
    api_response = api_instance.private_get_account_summary_get(currency, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_account_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **extended** | **bool**| Include additional fields | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_address_book_get**
> object private_get_address_book_get(currency, type)

Retrieves address book of given type

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type

try:
    # Retrieves address book of given type
    api_response = api_instance.private_get_address_book_get(currency, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_current_deposit_address_get**
> object private_get_current_deposit_address_get(currency)

Retrieve deposit address for currency

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol

try:
    # Retrieve deposit address for currency
    api_response = api_instance.private_get_current_deposit_address_get(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_current_deposit_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_deposits_get**
> object private_get_deposits_get(currency, count=count, offset=offset)

Retrieve the latest users deposits

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Retrieve the latest users deposits
    api_response = api_instance.private_get_deposits_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_deposits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_email_language_get**
> object private_get_email_language_get()

Retrieves the language to be used for emails.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves the language to be used for emails.
    api_response = api_instance.private_get_email_language_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_email_language_get: %s\n" % e)
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

# **private_get_margins_get**
> object private_get_margins_get(instrument_name, amount, price)

Get margins for given instrument, amount and price.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
amount = 1 # float | Amount, integer for future, float for option. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH.
price = 3.4 # float | Price

try:
    # Get margins for given instrument, amount and price.
    api_response = api_instance.private_get_margins_get(instrument_name, amount, price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_margins_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **amount** | **float**| Amount, integer for future, float for option. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. | 
 **price** | **float**| Price | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_new_announcements_get**
> object private_get_new_announcements_get()

Retrieves announcements that have not been marked read by the user.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves announcements that have not been marked read by the user.
    api_response = api_instance.private_get_new_announcements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_new_announcements_get: %s\n" % e)
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

# **private_get_open_orders_by_currency_get**
> object private_get_open_orders_by_currency_get(currency, kind=kind, type=type)

Retrieves list of user's open orders.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
type = 'type_example' # str | Order type, default - `all` (optional)

try:
    # Retrieves list of user's open orders.
    api_response = api_instance.private_get_open_orders_by_currency_get(currency, kind=kind, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_open_orders_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **type** | **str**| Order type, default - &#x60;all&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_open_orders_by_instrument_get**
> object private_get_open_orders_by_instrument_get(instrument_name, type=type)

Retrieves list of user's open orders within given Instrument.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
type = 'type_example' # str | Order type, default - `all` (optional)

try:
    # Retrieves list of user's open orders within given Instrument.
    api_response = api_instance.private_get_open_orders_by_instrument_get(instrument_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_open_orders_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **type** | **str**| Order type, default - &#x60;all&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_order_history_by_currency_get**
> object private_get_order_history_by_currency_get(currency, kind=kind, count=count, offset=offset, include_old=include_old, include_unfilled=include_unfilled)

Retrieves history of orders that have been partially or fully filled.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
count = 56 # int | Number of requested items, default - `20` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)
include_old = false # bool | Include in result orders older than 2 days, default - `false` (optional)
include_unfilled = false # bool | Include in result fully unfilled closed orders, default - `false` (optional)

try:
    # Retrieves history of orders that have been partially or fully filled.
    api_response = api_instance.private_get_order_history_by_currency_get(currency, kind=kind, count=count, offset=offset, include_old=include_old, include_unfilled=include_unfilled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_order_history_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 
 **include_old** | **bool**| Include in result orders older than 2 days, default - &#x60;false&#x60; | [optional] 
 **include_unfilled** | **bool**| Include in result fully unfilled closed orders, default - &#x60;false&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_order_history_by_instrument_get**
> object private_get_order_history_by_instrument_get(instrument_name, count=count, offset=offset, include_old=include_old, include_unfilled=include_unfilled)

Retrieves history of orders that have been partially or fully filled.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
count = 56 # int | Number of requested items, default - `20` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)
include_old = false # bool | Include in result orders older than 2 days, default - `false` (optional)
include_unfilled = false # bool | Include in result fully unfilled closed orders, default - `false` (optional)

try:
    # Retrieves history of orders that have been partially or fully filled.
    api_response = api_instance.private_get_order_history_by_instrument_get(instrument_name, count=count, offset=offset, include_old=include_old, include_unfilled=include_unfilled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_order_history_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 
 **include_old** | **bool**| Include in result orders older than 2 days, default - &#x60;false&#x60; | [optional] 
 **include_unfilled** | **bool**| Include in result fully unfilled closed orders, default - &#x60;false&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_order_margin_by_ids_get**
> object private_get_order_margin_by_ids_get(ids)

Retrieves initial margins of given orders

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
ids = ['ids_example'] # list[str] | Ids of orders

try:
    # Retrieves initial margins of given orders
    api_response = api_instance.private_get_order_margin_by_ids_get(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_order_margin_by_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| Ids of orders | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_order_state_get**
> object private_get_order_state_get(order_id)

Retrieve the current state of an order.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
order_id = 'ETH-100234' # str | The order id

try:
    # Retrieve the current state of an order.
    api_response = api_instance.private_get_order_state_get(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_order_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_position_get**
> object private_get_position_get(instrument_name)

Retrieve user position.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name

try:
    # Retrieve user position.
    api_response = api_instance.private_get_position_get(instrument_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_position_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_positions_get**
> object private_get_positions_get(currency, kind=kind)

Retrieve user positions.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | 
kind = 'kind_example' # str | Kind filter on positions (optional)

try:
    # Retrieve user positions.
    api_response = api_instance.private_get_positions_get(currency, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **kind** | **str**| Kind filter on positions | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_settlement_history_by_currency_get**
> object private_get_settlement_history_by_currency_get(currency, type=type, count=count)

Retrieves settlement, delivery and bankruptcy events that have affected your account.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Settlement type (optional)
count = 56 # int | Number of requested items, default - `20` (optional)

try:
    # Retrieves settlement, delivery and bankruptcy events that have affected your account.
    api_response = api_instance.private_get_settlement_history_by_currency_get(currency, type=type, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_settlement_history_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Settlement type | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_settlement_history_by_instrument_get**
> object private_get_settlement_history_by_instrument_get(instrument_name, type=type, count=count)

Retrieves public settlement, delivery and bankruptcy events filtered by instrument name

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
type = 'type_example' # str | Settlement type (optional)
count = 56 # int | Number of requested items, default - `20` (optional)

try:
    # Retrieves public settlement, delivery and bankruptcy events filtered by instrument name
    api_response = api_instance.private_get_settlement_history_by_instrument_get(instrument_name, type=type, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_settlement_history_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **type** | **str**| Settlement type | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;20&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_subaccounts_get**
> object private_get_subaccounts_get(with_portfolio=with_portfolio)

Get information about subaccounts

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
with_portfolio = True # bool |  (optional)

try:
    # Get information about subaccounts
    api_response = api_instance.private_get_subaccounts_get(with_portfolio=with_portfolio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_subaccounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_portfolio** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_transfers_get**
> object private_get_transfers_get(currency, count=count, offset=offset)

Adds new entry to address book of given type

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_get_transfers_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_transfers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_user_trades_by_currency_and_time_get**
> object private_get_user_trades_by_currency_and_time_get(currency, start_timestamp, end_timestamp, kind=kind, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest user trades that have occurred for instruments in a specific currency symbol and within given time range.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest user trades that have occurred for instruments in a specific currency symbol and within given time range.
    api_response = api_instance.private_get_user_trades_by_currency_and_time_get(currency, start_timestamp, end_timestamp, kind=kind, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_user_trades_by_currency_and_time_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **start_timestamp** | **int**| The earliest timestamp to return result for | 
 **end_timestamp** | **int**| The most recent timestamp to return result for | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_user_trades_by_currency_get**
> object private_get_user_trades_by_currency_get(currency, kind=kind, start_id=start_id, end_id=end_id, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest user trades that have occurred for instruments in a specific currency symbol.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
kind = 'kind_example' # str | Instrument kind, if not provided instruments of all kinds are considered (optional)
start_id = 'start_id_example' # str | The ID number of the first trade to be returned (optional)
end_id = 'end_id_example' # str | The ID number of the last trade to be returned (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest user trades that have occurred for instruments in a specific currency symbol.
    api_response = api_instance.private_get_user_trades_by_currency_get(currency, kind=kind, start_id=start_id, end_id=end_id, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_user_trades_by_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **kind** | **str**| Instrument kind, if not provided instruments of all kinds are considered | [optional] 
 **start_id** | **str**| The ID number of the first trade to be returned | [optional] 
 **end_id** | **str**| The ID number of the last trade to be returned | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_user_trades_by_instrument_and_time_get**
> object private_get_user_trades_by_instrument_and_time_get(instrument_name, start_timestamp, end_timestamp, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest user trades that have occurred for a specific instrument and within given time range.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_timestamp = 1536569522277 # int | The earliest timestamp to return result for
end_timestamp = 1536569522277 # int | The most recent timestamp to return result for
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest user trades that have occurred for a specific instrument and within given time range.
    api_response = api_instance.private_get_user_trades_by_instrument_and_time_get(instrument_name, start_timestamp, end_timestamp, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_user_trades_by_instrument_and_time_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **start_timestamp** | **int**| The earliest timestamp to return result for | 
 **end_timestamp** | **int**| The most recent timestamp to return result for | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_user_trades_by_instrument_get**
> object private_get_user_trades_by_instrument_get(instrument_name, start_seq=start_seq, end_seq=end_seq, count=count, include_old=include_old, sorting=sorting)

Retrieve the latest user trades that have occurred for a specific instrument.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
start_seq = 56 # int | The sequence number of the first trade to be returned (optional)
end_seq = 56 # int | The sequence number of the last trade to be returned (optional)
count = 56 # int | Number of requested items, default - `10` (optional)
include_old = True # bool | Include trades older than 7 days, default - `false` (optional)
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the latest user trades that have occurred for a specific instrument.
    api_response = api_instance.private_get_user_trades_by_instrument_get(instrument_name, start_seq=start_seq, end_seq=end_seq, count=count, include_old=include_old, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_user_trades_by_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **start_seq** | **int**| The sequence number of the first trade to be returned | [optional] 
 **end_seq** | **int**| The sequence number of the last trade to be returned | [optional] 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **include_old** | **bool**| Include trades older than 7 days, default - &#x60;false&#x60; | [optional] 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_user_trades_by_order_get**
> object private_get_user_trades_by_order_get(order_id, sorting=sorting)

Retrieve the list of user trades that was created for given order

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
order_id = 'ETH-100234' # str | The order id
sorting = 'sorting_example' # str | Direction of results sorting (`default` value means no sorting, results will be returned in order in which they left the database) (optional)

try:
    # Retrieve the list of user trades that was created for given order
    api_response = api_instance.private_get_user_trades_by_order_get(order_id, sorting=sorting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_user_trades_by_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id | 
 **sorting** | **str**| Direction of results sorting (&#x60;default&#x60; value means no sorting, results will be returned in order in which they left the database) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_get_withdrawals_get**
> object private_get_withdrawals_get(currency, count=count, offset=offset)

Retrieve the latest users withdrawals

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
count = 56 # int | Number of requested items, default - `10` (optional)
offset = 10 # int | The offset for pagination, default - `0` (optional)

try:
    # Retrieve the latest users withdrawals
    api_response = api_instance.private_get_withdrawals_get(currency, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_get_withdrawals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **count** | **int**| Number of requested items, default - &#x60;10&#x60; | [optional] 
 **offset** | **int**| The offset for pagination, default - &#x60;0&#x60; | [optional] 

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))

try:
    # Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled
    api_instance.private_logout_get()
except ApiException as e:
    print("Exception when calling PrivateApi->private_logout_get: %s\n" % e)
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

# **private_remove_from_address_book_get**
> object private_remove_from_address_book_get(currency, type, address, tfa=tfa)

Adds new entry to address book of given type

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
type = 'type_example' # str | Address book type
address = 'address_example' # str | Address in currency format, it must be in address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Adds new entry to address book of given type
    api_response = api_instance.private_remove_from_address_book_get(currency, type, address, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_remove_from_address_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **type** | **str**| Address book type | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_sell_get**
> object private_sell_get(instrument_name, amount, type=type, label=label, price=price, time_in_force=time_in_force, max_show=max_show, post_only=post_only, reduce_only=reduce_only, stop_price=stop_price, trigger=trigger, advanced=advanced)

Places a sell order for an instrument.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
instrument_name = 'BTC-PERPETUAL' # str | Instrument name
amount = 3.4 # float | It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH
type = 'type_example' # str | The order type, default: `\"limit\"` (optional)
label = 'label_example' # str | user defined label for the order (maximum 32 characters) (optional)
price = 3.4 # float | <p>The order price in base currency (Only for limit and stop_limit orders)</p> <p>When adding order with advanced=usd, the field price should be the option price value in USD.</p> <p>When adding order with advanced=implv, the field price should be a value of implied volatility in percentages. For example,  price=100, means implied volatility of 100%</p> (optional)
time_in_force = 'good_til_cancelled' # str | <p>Specifies how long the order remains in effect. Default `\"good_til_cancelled\"`</p> <ul> <li>`\"good_til_cancelled\"` - unfilled order remains in order book until cancelled</li> <li>`\"fill_or_kill\"` - execute a transaction immediately and completely or not at all</li> <li>`\"immediate_or_cancel\"` - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled</li> </ul> (optional) (default to 'good_til_cancelled')
max_show = 1 # float | Maximum amount within an order to be shown to other customers, `0` for invisible order (optional) (default to 1)
post_only = True # bool | <p>If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.</p> <p>Only valid in combination with time_in_force=`\"good_til_cancelled\"`</p> (optional) (default to True)
reduce_only = False # bool | If `true`, the order is considered reduce-only which is intended to only reduce a current position (optional) (default to False)
stop_price = 3.4 # float | Stop price, required for stop limit orders (Only for stop orders) (optional)
trigger = 'trigger_example' # str | Defines trigger type, required for `\"stop_limit\"` order type (optional)
advanced = 'advanced_example' # str | Advanced option order type. (Only for options) (optional)

try:
    # Places a sell order for an instrument.
    api_response = api_instance.private_sell_get(instrument_name, amount, type=type, label=label, price=price, time_in_force=time_in_force, max_show=max_show, post_only=post_only, reduce_only=reduce_only, stop_price=stop_price, trigger=trigger, advanced=advanced)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_sell_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_name** | **str**| Instrument name | 
 **amount** | **float**| It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH | 
 **type** | **str**| The order type, default: &#x60;\&quot;limit\&quot;&#x60; | [optional] 
 **label** | **str**| user defined label for the order (maximum 32 characters) | [optional] 
 **price** | **float**| &lt;p&gt;The order price in base currency (Only for limit and stop_limit orders)&lt;/p&gt; &lt;p&gt;When adding order with advanced&#x3D;usd, the field price should be the option price value in USD.&lt;/p&gt; &lt;p&gt;When adding order with advanced&#x3D;implv, the field price should be a value of implied volatility in percentages. For example,  price&#x3D;100, means implied volatility of 100%&lt;/p&gt; | [optional] 
 **time_in_force** | **str**| &lt;p&gt;Specifies how long the order remains in effect. Default &#x60;\&quot;good_til_cancelled\&quot;&#x60;&lt;/p&gt; &lt;ul&gt; &lt;li&gt;&#x60;\&quot;good_til_cancelled\&quot;&#x60; - unfilled order remains in order book until cancelled&lt;/li&gt; &lt;li&gt;&#x60;\&quot;fill_or_kill\&quot;&#x60; - execute a transaction immediately and completely or not at all&lt;/li&gt; &lt;li&gt;&#x60;\&quot;immediate_or_cancel\&quot;&#x60; - execute a transaction immediately, and any portion of the order that cannot be immediately filled is cancelled&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;good_til_cancelled&#39;]
 **max_show** | **float**| Maximum amount within an order to be shown to other customers, &#x60;0&#x60; for invisible order | [optional] [default to 1]
 **post_only** | **bool**| &lt;p&gt;If true, the order is considered post-only. If the new price would cause the order to be filled immediately (as taker), the price will be changed to be just below the bid.&lt;/p&gt; &lt;p&gt;Only valid in combination with time_in_force&#x3D;&#x60;\&quot;good_til_cancelled\&quot;&#x60;&lt;/p&gt; | [optional] [default to True]
 **reduce_only** | **bool**| If &#x60;true&#x60;, the order is considered reduce-only which is intended to only reduce a current position | [optional] [default to False]
 **stop_price** | **float**| Stop price, required for stop limit orders (Only for stop orders) | [optional] 
 **trigger** | **str**| Defines trigger type, required for &#x60;\&quot;stop_limit\&quot;&#x60; order type | [optional] 
 **advanced** | **str**| Advanced option order type. (Only for options) | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_announcement_as_read_get**
> object private_set_announcement_as_read_get(announcement_id)

Marks an announcement as read, so it will not be shown in `get_new_announcements`.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
announcement_id = 3.4 # float | the ID of the announcement

try:
    # Marks an announcement as read, so it will not be shown in `get_new_announcements`.
    api_response = api_instance.private_set_announcement_as_read_get(announcement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_set_announcement_as_read_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **float**| the ID of the announcement | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_email_for_subaccount_get**
> object private_set_email_for_subaccount_get(sid, email)

Assign an email address to a subaccount. User will receive an email with confirmation link.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
email = 'subaccount_1@email.com' # str | The email address for the subaccount

try:
    # Assign an email address to a subaccount. User will receive an email with confirmation link.
    api_response = api_instance.private_set_email_for_subaccount_get(sid, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_set_email_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **email** | **str**| The email address for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_email_language_get**
> object private_set_email_language_get(language)

Changes the language to be used for emails.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
language = 'en' # str | The abbreviated language name. Valid values include `\"en\"`, `\"ko\"`, `\"zh\"`

try:
    # Changes the language to be used for emails.
    api_response = api_instance.private_set_email_language_get(language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_set_email_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| The abbreviated language name. Valid values include &#x60;\&quot;en\&quot;&#x60;, &#x60;\&quot;ko\&quot;&#x60;, &#x60;\&quot;zh\&quot;&#x60; | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_set_password_for_subaccount_get**
> object private_set_password_for_subaccount_get(sid, password)

Set the password for the subaccount

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
password = 'password_example' # str | The password for the subaccount

try:
    # Set the password for the subaccount
    api_response = api_instance.private_set_password_for_subaccount_get(sid, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_set_password_for_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **password** | **str**| The password for the subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_submit_transfer_to_subaccount_get**
> object private_submit_transfer_to_subaccount_get(currency, amount, destination)

Transfer funds to a subaccount.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 1 # int | Id of destination subaccount

try:
    # Transfer funds to a subaccount.
    api_response = api_instance.private_submit_transfer_to_subaccount_get(currency, amount, destination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_submit_transfer_to_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **amount** | **float**| Amount of funds to be transferred | 
 **destination** | **int**| Id of destination subaccount | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_submit_transfer_to_user_get**
> object private_submit_transfer_to_user_get(currency, amount, destination, tfa=tfa)

Transfer funds to a another user.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
amount = 3.4 # float | Amount of funds to be transferred
destination = 'destination_example' # str | Destination address from address book
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Transfer funds to a another user.
    api_response = api_instance.private_submit_transfer_to_user_get(currency, amount, destination, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_submit_transfer_to_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **amount** | **float**| Amount of funds to be transferred | 
 **destination** | **str**| Destination address from address book | 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to subscribe to.

try:
    # Subscribe to one or more channels.
    api_response = api_instance.private_subscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_subscribe_get: %s\n" % e)
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

# **private_toggle_deposit_address_creation_get**
> object private_toggle_deposit_address_creation_get(currency, state)

Enable or disable deposit address creation

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
state = True # bool | 

try:
    # Enable or disable deposit address creation
    api_response = api_instance.private_toggle_deposit_address_creation_get(currency, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_toggle_deposit_address_creation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **state** | **bool**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_toggle_notifications_from_subaccount_get**
> object private_toggle_notifications_from_subaccount_get(sid, state)

Enable or disable sending of notifications for the subaccount.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
state = True # bool | enable (`true`) or disable (`false`) notifications

try:
    # Enable or disable sending of notifications for the subaccount.
    api_response = api_instance.private_toggle_notifications_from_subaccount_get(sid, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_toggle_notifications_from_subaccount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **state** | **bool**| enable (&#x60;true&#x60;) or disable (&#x60;false&#x60;) notifications | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_toggle_subaccount_login_get**
> object private_toggle_subaccount_login_get(sid, state)

Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
sid = 56 # int | The user id for the subaccount
state = 'state_example' # str | enable or disable login.

try:
    # Enable or disable login for a subaccount. If login is disabled and a session for the subaccount exists, this session will be terminated.
    api_response = api_instance.private_toggle_subaccount_login_get(sid, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_toggle_subaccount_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **int**| The user id for the subaccount | 
 **state** | **str**| enable or disable login. | 

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
channels = ['channels_example'] # list[str] | A list of channels to unsubscribe from.

try:
    # Unsubscribe from one or more channels.
    api_response = api_instance.private_unsubscribe_get(channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_unsubscribe_get: %s\n" % e)
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

# **private_withdraw_get**
> object private_withdraw_get(currency, address, amount, priority=priority, tfa=tfa)

Creates a new withdrawal request

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
api_instance = openapi_client.PrivateApi(openapi_client.ApiClient(configuration))
currency = 'currency_example' # str | The currency symbol
address = 'address_example' # str | Address in currency format, it must be in address book
amount = 3.4 # float | Amount of funds to be withdrawn
priority = 'priority_example' # str | Withdrawal priority, optional for BTC, default: `high` (optional)
tfa = 'tfa_example' # str | TFA code, required when TFA is enabled for current account (optional)

try:
    # Creates a new withdrawal request
    api_response = api_instance.private_withdraw_get(currency, address, amount, priority=priority, tfa=tfa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->private_withdraw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency symbol | 
 **address** | **str**| Address in currency format, it must be in address book | 
 **amount** | **float**| Amount of funds to be withdrawn | 
 **priority** | **str**| Withdrawal priority, optional for BTC, default: &#x60;high&#x60; | [optional] 
 **tfa** | **str**| TFA code, required when TFA is enabled for current account | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

