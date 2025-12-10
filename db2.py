ALTER TABLE orders
ALTER COLUMN order_time SET DATA TYPE TIMESTAMP WITH TIME ZONE;

dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")