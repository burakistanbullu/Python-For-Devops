import boto3
from datetime import date, timedelta

def get_yesterdays_costs_simple():
    today = date.today()
    yesterday = today - timedelta(days=1)

    ce = boto3.client("ce")

    # Request cost and usage data from AWS Cost Explorer
    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": yesterday.strftime("%Y-%m-%d"),
            "End": today.strftime("%Y-%m-%d"),
        },
        Granularity="DAILY",  # we only need 1-day granularity (yesterday)
        Metrics=["UnblendedCost"],  # basic cost metric
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],  # group cost by AWS service
        Filter={
            # Exclude Credits and Refunds so the costs reflect actual usage
            "Not": {
                "Dimensions": {
                    "Key": "RECORD_TYPE",
                    "Values": ["Credit", "Refund"]
                }
            }
        }
    )

    # Extract the "ResultsByTime" section from the response
    results = response.get("ResultsByTime", [])
    if not results:
        return yesterday, {}  # return empty result if AWS returned nothing

    # "Groups" contains the list of services and their corresponding cost data
    groups = results[0].get("Groups", {})

    service_costs = {}  # dictionary to store cost information per service

    for g in groups:
        service = g["Keys"][0]  # Service name such as "Amazon EC2", "Amazon S3", etc.
        cost = float(g["Metrics"]["UnblendedCost"]["Amount"])
        currency = g["Metrics"]["UnblendedCost"]["Unit"]

        # Add each service's cost data to the dictionary as a key-value pair
        # Key   → Service name (e.g., "Amazon EC2")
        # Value → Dictionary containing cost and currency
        service_costs[service] = {
            "cost": cost,
            "currency": currency
        }

    return yesterday, service_costs


def main():
    day, costs = get_yesterdays_costs_simple()

    if not costs:
        print(f"No cost data found for {day}.")
        return

    print(f"AWS service costs for {day}:\n")

    total = 0

    # Sort services by their cost in descending order
    # costs.items()    → turns dict into list of (service, data) tuples
    # key=lambda ...   → sort by cost value inside the inner dict
    for service, data in sorted(costs.items(), key=lambda x: x[1]["cost"], reverse=True):
        # Format output: left-align service name, show cost with 4 decimals
        print(f"{service:<40} {data['cost']:.4f} {data['currency']}")
        total += data['cost']

    print("\nTotal:", round(total, 4), data["currency"])


if __name__ == "__main__":
    main()
