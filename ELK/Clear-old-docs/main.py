from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "MyDevPassword!"

client = Elasticsearch(
    "https://buraklab.local:30008",       # <-- note https
    basic_auth=("elastic", ELASTIC_PASSWORD),
    verify_certs=False,
    ssl_show_warn=False
)



index_stats = client.indices.stats( index="my_test_index" )
print(index_stats)

doc_count = index_stats['indices']['my_test_index']['total']['docs']['count']

#print(f"Document count in 'my_test_index': {doc_count}")
