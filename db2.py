import ibm_db

# Connection details — replace with your actual values
dsn_hostname = "your_hostname.databases.appdomain.cloud"  # e.g. dashdb-txn-someid.databases.appdomain.cloud
dsn_uid = "your_user"       # e.g. bluadmin
dsn_pwd = "your_password"
dsn_port = "50001"          # Usually 50001 for Db2 Warehouse
dsn_database = "BLUDB"      # Db2 Warehouse default database
dsn_security = "SSL"        # SSL required for Db2 Warehouse

# Build DSN
dsn = (
    f"DATABASE={dsn_database};"
    f"HOSTNAME={dsn_hostname};"
    f"PORT={dsn_port};"
    f"PROTOCOL=TCPIP;"
    f"UID={dsn_uid};"
    f"PWD={dsn_pwd};"
    f"SECURITY={dsn_security};"
)

try:
    # Connect
    conn = ibm_db.connect(dsn, "", "")
    print("✅ Connection successful!")

    # Query
    sql = "SELECT * FROM cpbCORAPROD.TURN FETCH FIRST 1 ROW ONLY"

    stmt = ibm_db.exec_immediate(conn, sql)

    result = ibm_db.fetch_assoc(stmt)
    if result:
        print("Row fetched:", result)
    else:
        print("No rows returned.")

    # Close connection
    ibm_db.close(conn)

except Exception as e:
    print("❌ Error:", e)
