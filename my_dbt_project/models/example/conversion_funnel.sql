{{ config(
    alias = 'conversion_funnel',
    materialized='table'
) }}

WITH funnel_steps AS (
    SELECT
        user_id,
        COUNT(CASE WHEN step = 'open_app' THEN 1 END) AS opened_app,
        COUNT(CASE WHEN step = 'browse_product' THEN 1 END) AS browsed_product,
        COUNT(CASE WHEN step = 'add_to_cart' THEN 1 END) AS added_to_cart,
        COUNT(CASE WHEN step = 'checkout' THEN 1 END) AS checkout,
        COUNT(CASE WHEN step = 'purchase' THEN 1 END) AS completed_purchase
    FROM {{ ref('events') }}  -- reference the events table
    GROUP BY user_id
)

SELECT
    COUNT(DISTINCT user_id) AS total_users,  -- total distinct users
    SUM(opened_app) AS opened_app_users,  -- total users who opened the app
    SUM(browsed_product) AS browsed_product_users,  -- total users who browsed a product
    SUM(added_to_cart) AS added_to_cart_users,  -- total users who added items to the cart
    SUM(checkout) AS checkout_users,  -- total users who reached checkout
    SUM(completed_purchase) AS completed_purchase_users,  -- total users who completed a purchase
    ROUND(
        (SUM(completed_purchase) * 1.0 / NULLIF(SUM(opened_app), 0)) * 100, 2
    ) AS conversion_rate_pct  -- conversion rate from opened app to purchase
FROM funnel_steps 
