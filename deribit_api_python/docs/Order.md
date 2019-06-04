# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | direction, &#x60;buy&#x60; or &#x60;sell&#x60; | 
**reduce_only** | **bool** | &#x60;true&#x60; for reduce-only orders only | [optional] 
**triggered** | **bool** | Whether the stop order has been triggered (Only for stop orders) | [optional] 
**order_id** | **str** | Unique order identifier | 
**price** | **float** | Price in base currency | 
**time_in_force** | **str** | Order time in force: &#x60;\&quot;good_til_cancelled\&quot;&#x60;, &#x60;\&quot;fill_or_kill\&quot;&#x60;, &#x60;\&quot;immediate_or_cancel\&quot;&#x60; | 
**api** | **bool** | &#x60;true&#x60; if created with API | 
**order_state** | **str** | order state, &#x60;\&quot;open\&quot;&#x60;, &#x60;\&quot;filled\&quot;&#x60;, &#x60;\&quot;rejected\&quot;&#x60;, &#x60;\&quot;cancelled\&quot;&#x60;, &#x60;\&quot;untriggered\&quot;&#x60; | 
**implv** | **float** | Implied volatility in percent. (Only if &#x60;advanced&#x3D;\&quot;implv\&quot;&#x60;) | [optional] 
**advanced** | **str** | advanced type: &#x60;\&quot;usd\&quot;&#x60; or &#x60;\&quot;implv\&quot;&#x60; (Only for options; field is omitted if not applicable).  | [optional] 
**post_only** | **bool** | &#x60;true&#x60; for post-only orders only | 
**usd** | **float** | Option price in USD (Only if &#x60;advanced&#x3D;\&quot;usd\&quot;&#x60;) | [optional] 
**stop_price** | **float** | stop price (Only for future stop orders) | [optional] 
**order_type** | **str** | order type, &#x60;\&quot;limit\&quot;&#x60;, &#x60;\&quot;market\&quot;&#x60;, &#x60;\&quot;stop_limit\&quot;&#x60;, &#x60;\&quot;stop_market\&quot;&#x60; | 
**last_update_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**original_order_type** | **str** | Original order type. Optional field | [optional] 
**max_show** | **float** | Maximum amount within an order to be shown to other traders, 0 for invisible order. | 
**profit_loss** | **float** | Profit and loss in base currency. | [optional] 
**is_liquidation** | **bool** | &#x60;true&#x60; if order was automatically created during liquidation | 
**filled_amount** | **float** | Filled amount of the order. For perpetual and futures the filled_amount is in USD units, for options - in units or corresponding cryptocurrency contracts, e.g., BTC or ETH. | [optional] 
**label** | **str** | user defined label (up to 32 characters) | 
**commission** | **float** | Commission paid so far (in base currency) | [optional] 
**amount** | **float** | It represents the requested order size. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. | [optional] 
**trigger** | **str** | Trigger type (Only for stop orders). Allowed values: &#x60;\&quot;index_price\&quot;&#x60;, &#x60;\&quot;mark_price\&quot;&#x60;, &#x60;\&quot;last_price\&quot;&#x60;. | [optional] 
**instrument_name** | **str** | Unique instrument identifier | [optional] 
**creation_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**average_price** | **float** | Average fill price of the order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


