import json
import re
import mysql.connector
from datetime import datetime

# MySQL Configuration
MYSQL_HOST = 'mysql'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'haproxy_logs'

# Create MySQL connection
def connect_to_db():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Create table
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS haproxy_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            accept_date VARCHAR(10),
            backend_name VARCHAR(50),
            bytes_read INT,
            bytes_uploaded INT,
            client_ip VARCHAR(15),
            client_port INT,
            date_time DATETIME,
            frontend_name VARCHAR(50),
            process_id INT,
            status_code INT,
            server_name VARCHAR(50),
            http_request VARCHAR(500),
            http_request_query_string VARCHAR(500),       
            response_time INT
        )
    """)

# Insert log entry into MySQL
def insert_log(cursor, log_entry):
    cursor.execute("""
        INSERT INTO haproxy_logs (
            accept_date, backend_name, bytes_read, bytes_uploaded, client_ip, client_port,
            date_time, frontend_name, process_id, status_code, server_name,
                   http_request, http_request_query_string, response_time
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        log_entry['accept_date'],
        log_entry['backend_name'],
        log_entry['bytes_read'],
        log_entry['bytes_uploaded'],
        log_entry['client_ip'],
        log_entry['client_port'],
        datetime.strptime(log_entry['date_time'], '%d/%b/%Y:%H:%M:%S.%f'),
        log_entry['frontend_name'],
        log_entry['process_id'],
        log_entry['status_code'],
        log_entry['server_name'],
        log_entry['http_request'],
        log_entry['http_request_query_string'],
        log_entry['response_time']
    ))

# Parse HaProxy logs
def parse_logs(log_file):
    pattern = r'haproxy\[\d+\]: \'(.+)\''
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                log_json = match.group(1)
                log_entry = json.loads(log_json)
                yield log_entry

def main():
    log_file = 'haproxy.log'
    
    # Connect to MySQL
    db = connect_to_db()
    cursor = db.cursor()

    # Create table if not exists
    create_table(cursor)

    # Parse log entries and insert into MySQL
    for log_entry in parse_logs(log_file):
        insert_log(cursor, log_entry)
        db.commit()

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
