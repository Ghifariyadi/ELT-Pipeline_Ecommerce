{{ config(
    alias = 'voucher_effectiveness',
    materialized = 'table'
) }}

WITH voucher_usage AS (
    SELECT
        voucher_code,
        COUNT(transaction_id) AS total_usage,
        SUM(final_amount) AS total_gmv_with_voucher,
        SUM(admin_fee) AS total_admin_fee,
        ROUND(AVG(final_amount), 2) AS avg_order_value_with_voucher,
        ROUND(SUM(amount) - SUM(final_amount), 2) AS total_discount
    FROM {{ ref('transactions') }}
    WHERE voucher_code IS NOT NULL
    GROUP BY voucher_code
),

voucher_contribution AS (
    SELECT
        v.voucher_code,
        v.total_usage,
        v.total_gmv_with_voucher,
        v.avg_order_value_with_voucher,
        v.total_discount,
        ROUND((v.total_gmv_with_voucher * 100.0) / NULLIF(SUM(t.final_amount) OVER(), 0), 2) AS gmv_contribution_pct
    FROM voucher_usage v
    JOIN {{ ref('transactions') }} t ON v.voucher_code = t.voucher_code
)

SELECT *
FROM voucher_contribution
ORDER BY total_usage DESC
