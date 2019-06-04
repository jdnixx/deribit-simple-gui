# Withdrawal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**fee** | **float** | Fee in currency | [optional] 
**confirmed_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) of withdrawal confirmation, &#x60;null&#x60; when not confirmed | [optional] 
**amount** | **float** | Amount of funds in given currency | 
**priority** | **float** | Id of priority level | [optional] 
**currency** | **str** | Currency, i.e &#x60;\&quot;BTC\&quot;&#x60;, &#x60;\&quot;ETH\&quot;&#x60; | 
**state** | **str** | Withdrawal state, allowed values : &#x60;unconfirmed&#x60;, &#x60;confirmed&#x60;, &#x60;cancelled&#x60;, &#x60;completed&#x60;, &#x60;interrupted&#x60;, &#x60;rejected&#x60; | 
**address** | **str** | Address in proper format for currency | 
**created_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | [optional] 
**id** | **int** | Withdrawal id in Deribit system | [optional] 
**transaction_id** | **str** | Transaction id in proper format for currency, &#x60;null&#x60; if id is not available | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


