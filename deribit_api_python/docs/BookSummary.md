# BookSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_index** | **str** | Name of the underlying future, or &#x60;&#39;index_price&#39;&#x60; (options only) | [optional] 
**volume** | **float** | The total 24h traded volume (in base currency) | 
**volume_usd** | **float** | Volume in usd (futures only) | [optional] 
**underlying_price** | **float** | underlying price for implied volatility calculations (options only) | [optional] 
**bid_price** | **float** | The current best bid price, &#x60;null&#x60; if there aren&#39;t any bids | 
**open_interest** | **float** | The total amount of outstanding contracts in the corresponding amount units. For perpetual and futures the amount is in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. | 
**quote_currency** | **str** | Quote currency | 
**high** | **float** | Price of the 24h highest trade | 
**estimated_delivery_price** | **float** | Estimated delivery price, in USD (futures only). For more details, see Documentation &gt; General &gt; Expiration Price | [optional] 
**last** | **float** | The price of the latest trade, &#x60;null&#x60; if there weren&#39;t any trades | 
**mid_price** | **float** | The average of the best bid and ask, &#x60;null&#x60; if there aren&#39;t any asks or bids | 
**interest_rate** | **float** | Interest rate used in implied volatility calculations (options only) | [optional] 
**funding_8h** | **float** | Funding 8h (perpetual only) | [optional] 
**mark_price** | **float** | The current instrument market price | 
**ask_price** | **float** | The current best ask price, &#x60;null&#x60; if there aren&#39;t any asks | 
**instrument_name** | **str** | Unique instrument identifier | 
**low** | **float** | Price of the 24h lowest trade, &#x60;null&#x60; if there weren&#39;t any trades | 
**base_currency** | **str** | Base currency | [optional] 
**creation_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**current_funding** | **float** | Current funding (perpetual only) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


