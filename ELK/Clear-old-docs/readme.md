# Elasticsearch Old Document Cleanup Script

This script connects to an Elasticsearch cluster, counts documents older than a specified time (default: 2 day), and deletes them safely using delete_by_query.

*Time format of documents is : "2025-12-04T14:57:35.509Z"*

## Requirements

-   Python 3.8+
-   elasticsearch Python client
    -   Install via:
        ```bash
        pip install elasticsearch
        ```

## Configuration

**Update the following values in the script as needed:**

-   ELASTIC_PASSWORD : Elasticsearch password for the elastic user
-   index_name : Name of the index to clean up
-   days : Number of days to keep (default is 1 day old)
-   Elasticsearch URL : Cluster endpoint to connect to

**What the Script Does**
-   Connects to your Elasticsearch cluster.
-   Calculates a timestamp (now - 2 day).
-   Builds a range query to find documents where created < timestamp.
-   Uses the count API to show how many documents match.
-   Deletes those documents using delete_by_query (if count > 0).
-   Prints results for visibility.