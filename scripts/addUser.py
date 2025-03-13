#!/usr/bin/env python
S

import sys
import os
from mlflow.server import get_app_client

os.environ["MLFLOW_TRACKING_USERNAME"] = "mladmin"
os.environ["MLFLOW_TRACKING_PASSWzchen2025031420@AlanCS"

username = sys.argv[1]
pwd = sys.argv[2]

isAdmin = False
if len(sys.argv) > 3:
    isAdmin = bool(sys.argv[3])

tracking_uri = "http://localhost:5000/"

auth_client = get_app_client("basic-auth", tracking_uri=tracking_uri)
auth_client.create_user(username=username, password=pwd)
auth_client.update_user_admin(username=username, is_admin=isAdmin)

print(f"User {username} created.")