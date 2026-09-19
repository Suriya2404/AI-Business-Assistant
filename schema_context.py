SCHEMA = """
DATABASE: Olist E-Commerce

TABLE: customers
- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

TABLE: orders
- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date

TABLE: order_items
- order_id
- order_item_id
- product_id
- seller_id
- shipping_limit_date
- price
- freight_value

TABLE: payments
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

TABLE: reviews
- review_record_id
- review_id
- order_id
- review_score
- review_comment_title
- review_comment_message
- review_creation_date
- review_answer_timestamp

TABLE: products
- product_id
- product_category_name
- product_name_lenght
- product_description_lenght
- product_photos_qty
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

TABLE: sellers
- seller_id
- seller_zip_code_prefix
- seller_city
- seller_state

TABLE: categories
- product_category_name
- product_category_name_english

RELATIONSHIPS:

customers.customer_id → orders.customer_id

orders.order_id → order_items.order_id

orders.order_id → payments.order_id

orders.order_id → reviews.order_id

order_items.product_id → products.product_id

order_items.seller_id → sellers.seller_id

products.product_category_name → categories.product_category_name
"""