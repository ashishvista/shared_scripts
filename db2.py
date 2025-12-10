ALTER TABLE orders
ALTER COLUMN order_time SET DATA TYPE TIMESTAMP WITH TIME ZONE;

dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

CAST(
        TO_TIMESTAMP_TZ(REPLACE(?, 'Z', '+00:00'))
        AS TIMESTAMP
    )