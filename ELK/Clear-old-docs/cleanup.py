from elasticsearch import Elasticsearch
from datetime import datetime, timedelta, timezone

ELASTIC_PASSWORD = "MyDevPassword!" 

# Define the index name and the time threshold
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

# Create the Elasticsearch client to connect to the cluster
try:
    client = Elasticsearch(
        "https://buraklab.local:30008",
        basic_auth=("elastic", ELASTIC_PASSWORD),
        verify_certs=False,
        ssl_show_warn=False,
    )
    print("Successfully connected to Elasticsearch.")
except Exception as e:
    print("Error connecting to Elasticsearch:", e)
    exit(1)



# Count matching documents
try:
    count_resp = client.count(index=index_name, query=query)
    to_delete = count_resp["count"]
    print(f"Documents to delete: {to_delete}")
except Exception as e:
    print("Error executing count query:", e)
    exit(1)

# Delete documents
if to_delete > 0:
    try:
        delete_resp = client.delete_by_query(
            index=index_name,
            query=query,
            conflicts="proceed",
            refresh=True
        )
        print("Delete response:")
        print(delete_resp)
    except Exception as e:
        print("Error during delete_by_query:", e)
else:
    print("Nothing to delete.")