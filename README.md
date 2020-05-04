Elasticsearch health status.

`es_status --host <host or ip> --port <port> --https <enable httpsi if persent>`

Examples:

`es_status --host localhost --port 9200`
`http://locahost:9200/_cluster/health`

`es_status --host 1.2.3.4 --port 9300 --https`
`https://1.2.3.4:9300/_cluster/health`

