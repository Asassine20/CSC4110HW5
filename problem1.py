# Revision 1 BEGIN 2024-02-07
## Begin Andrew Sassine here (2024-02-07)

import random
import json
from datetime import datetime, timedelta

# Data Collector Method
def generate_user_data(number_of_users):
    user_data = {}
    for user_id in range(1, number_of_users + 1):
        username = f"user{user_id}"
        password = f"pass{random.randint(1000, 9999)}"
        birthdate = (datetime.now() - timedelta(days=random.randint(5000, 30000))).date().isoformat()
        address = f"1234 Main St, City{random.randint(1, 5)}, State{random.randint(1, 50)}"
        social_security_number = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
        product_purchased = {
            "order_id": f"ID-{random.randint(10000, 99999)}",
            "vendor": f"Vendor{random.randint(1, 10)}",
            "product_id": f"ID-{random.randint(100, 999)}",
            "quantity": random.randint(1, 10),
            "date_of_order": (datetime.now() - timedelta(days=random.randint(1, 365))).date().isoformat(),
            "region": f"Region{random.randint(1, 5)}"
        }
        salesperson = f"Salesperson{random.randint(1, 10)}"
        user_data[user_id] = [username, password, birthdate, address, social_security_number, product_purchased, salesperson]
    return user_data

# Search Engine
def search_user_data(user_data, search_term):
    results = {key: value for key, value in user_data.items() if search_term in str(value)}
    return results

user_data = generate_user_data(100)  # Generate data for 100 users

# Example search - Find users in "State1"
search_results = search_user_data(user_data, "State1")
print(json.dumps(search_results, indent=4))  # Print search results

## End Andrew Sassine here (2024-02-07)
# Revision 1 FINAL DATE 2024-02-07
