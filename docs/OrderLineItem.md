# OrderLineItem
> squareconnect.models.order_line_item

### Description

Represents a line item in an order. Each line item describes a different product to purchase, with its own quantity and price details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique ID that identifies the line item only within this order.  This field is read-only. | [optional] 
**name** | **str** | The name of the line item. | [optional] 
**quantity** | **str** | The quantity purchased, formatted as a decimal number. For example: &#x60;\&quot;3\&quot;&#x60;.  Line items with a &#x60;quantity_unit&#x60; can have non-integer quantities. For example: &#x60;\&quot;1.70000\&quot;&#x60;.  Orders Hub and older versions of Connect do not support non-integer quantities. See [Decimal quantities with Orders hub and older versions of Connect](/more-apis/orders/overview#decimal-quantities). | 
**quantity_unit** | [**OrderQuantityUnit**](OrderQuantityUnit.md) | The unit and precision that this line item&#39;s quantity is measured in. | [optional] 
**note** | **str** | The note of the line item. | [optional] 
**catalog_object_id** | **str** | The [CatalogItemVariation](#type-catalogitemvariation) id applied to this line item. | [optional] 
**variation_name** | **str** | The name of the variation applied to this line item. | [optional] 
**modifiers** | [**list[OrderLineItemModifier]**](OrderLineItemModifier.md) | The [CatalogModifier](#type-catalogmodifier)s applied to this line item. | [optional] 
**taxes** | [**list[OrderLineItemTax]**](OrderLineItemTax.md) | A list of taxes applied to this line item. On read or retrieve, this list includes both item-level taxes and any order-level taxes apportioned to this item. When creating an Order, set your item-level taxes in this list. | [optional] 
**discounts** | [**list[OrderLineItemDiscount]**](OrderLineItemDiscount.md) | A list of discounts applied to this line item. On read or retrieve, this list includes both item-level discounts and any order-level discounts apportioned to this item. When creating an Order, set your item-level discounts in this list. | [optional] 
**base_price_money** | [**Money**](Money.md) | The base price for a single unit of the line item. | [optional] 
**variation_total_price_money** | [**Money**](Money.md) | The total price of all item variations sold in this line item. Calculated as &#x60;base_price_money&#x60; multiplied by &#x60;quantity&#x60;. Does not include modifiers. | [optional] 
**gross_sales_money** | [**Money**](Money.md) | The amount of money made in gross sales for this line item. Calculated as the sum of the variation&#39;s total price and each modifier&#39;s total price.  This field is read-only. | [optional] 
**total_tax_money** | [**Money**](Money.md) | The total tax amount of money to collect for the line item.  This field is read-only. | [optional] 
**total_discount_money** | [**Money**](Money.md) | The total discount amount of money to collect for the line item.  This field is read-only. | [optional] 
**total_money** | [**Money**](Money.md) | The total amount of money to collect for this line item.  This field is read-only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


