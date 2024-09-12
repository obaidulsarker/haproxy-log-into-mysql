# 1. Haproxy Log format: please update following log-format value in /etc/haproxy.cfg file
--------------------------------------------------------------
log-format '{"accept_date":"%ms","backend_name":"%b","backend_queue":"%bq","backend_source_ip":"%bi","backend_source_port":"%bp","backend_connections":"%bc","bytes_read":"%B","bytes_uploaded":"%U","captured_request_cookie":"%CC","captured_request_headers_clf":"%hrl","captured_request_headers":"%hr","captured_response_cookie":"%CS","captured_response_headers_clf":"%hsl","captured_response_headers":"%hs","client_ip":"%ci","client_port":"%cp","connection_handshake_time":"%Th","date_time":"%t","frontend_connections":"%fc","frontend_ip":"%fi","frontend_log_counter":"%lc","frontend_name":"%f","frontend_name_transport":"%ft","frontend_port":"%fp","gmt_date_time":"%T","hostname":"%H","http_method":"%HM","http_request":"%r","http_request_query_string":"%HQ","http_request_path":"%HP","http_request_uri":"%HU","http_version":"%HV","idle_time":"%Ti","local_date_time":"%Tl","process_connections":"%ac","process_id":"%pid","request_counter":"%rt","response_time":"%Tr","retries":"%rc","server_connections":"%sc","server_ip":"%si","server_name":"%s","server_port":"%sp","server_queue":"%sq","ssl_ciphers":"%sslc","ssl_version":"%sslv","status_code":"%ST","tc":"%Tc","termination_state":"%ts","termination_state_with_cookie_status":"%tsc","timestamp":"%Ts","tq":"%Tq","tt":"%Tt","tw":"%Tw","unique_id":"%ID"}'

------------------------------------------------------------------------------

# 2. Steps to run:
## 2.1 Place the HaProxy log data in a file called haproxy.log.
## 2.2 Build and run the Docker containers:
#### docker-compose up --build

3. Check mysql data
#### docker ps 
# docker-compose exec -it mysql bash
#### mysql -u root -p
#### mysql> show databases;
#### mysql> use haproxy_logs;
#### mysql> show tables;
#### mysql> SELECT * FROM haproxy_logs;