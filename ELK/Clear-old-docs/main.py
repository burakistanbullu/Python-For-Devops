from elasticsearch import Elasticsearch
from datetime import datetime, timedelta, timezone

ELASTIC_PASSWORD = "MyDevPassword!" 

# Create the Elasticsearch client to connect to the cluster
client = Elasticsearch(
    "https://buraklab.local:30008",     
    basic_auth=("elastic", ELASTIC_PASSWORD),
    verify_certs=False,
    ssl_show_warn=False
)

index_name = "my_test_index"
twodays_ago = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()

# Define the query to find documents older than two days
query = {
    "range": {
        "created": {
            "lt": twodays_ago 
        }
    }
}

# Count documents matching the query
count_resp = client.count(index=index_name, query=query)
print(f"Documents to delete: {count_resp['count']}")

# Delete documents if any match the query
if count_resp["count"] > 0:
    delete_resp = client.delete_by_query(
        index=index_name,
        query=query,
        conflicts="proceed",
        refresh=True
    )
    print("Delete response:")
    print(delete_resp)
else:
    print("Nothing to delete.")
