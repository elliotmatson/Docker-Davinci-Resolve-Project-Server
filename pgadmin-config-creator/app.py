import json
import os
import time

with open('/config/servers.json', 'w') as f:
    print("created " + f.name)
    template_string = '{"Servers": {"1": {"Name": "DavinciResolve", "Group": "Servers", "Port": 5432, "Username": "postgres", "Host": "postgres", "SSLMode": "prefer", "MaintenanceDB": "postgres"}}}'
    data = json.loads(template_string)
    data["Servers"]["1"]["Username"]=os.getenv("POSTGRES_USER")
    print("printing json to file...")
    print(data)
    json.dump(data, f, indent=2)
# sleep until GHA Healthchecks are complete
time.sleep(125)

