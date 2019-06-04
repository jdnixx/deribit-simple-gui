# Deposit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**state** | **str** | Deposit state, allowed values : &#x60;pending&#x60;, &#x60;completed&#x60;, &#x60;rejected&#x60;, &#x60;replaced&#x60; | 
**received_timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**currency** | **str** | Currency, i.e &#x60;\&quot;BTC\&quot;&#x60;, &#x60;\&quot;ETH\&quot;&#x60; | 
**address** | **str** | Address in proper format for currency | 
**amount** | **float** | Amount of funds in given currency | 
**transaction_id** | **str** | Transaction id in proper format for currency, &#x60;null&#x60; if id is not available | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


