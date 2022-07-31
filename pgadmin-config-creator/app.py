import json
import os
import time

# quit if config file already exists
if os.path.exists("/config/servers.json"):
    print("/config/servers.json already exists.")
else:
    # open json file in docker volume
    with open("/config/servers.json", "w") as f:
        print("created " + f.name)
        # template json string
        template_string = (
            '{"Servers": {"1": {"Name": "DavinciResolve", '
            '"Group": "Servers", "Port": 5432, "Username": '
            '"postgres", "Host": "postgres", "SSLMode": "prefer", "MaintenanceDB": "postgres"}}}'
        )
        data = json.loads(template_string)
        # fix username
        data["Servers"]["1"]["Username"] = os.getenv("POSTGRES_USER")
        print("Printing json to file...")
        print(data)
        # update config file
        json.dump(data, f, indent=2)

print("Done. Sleeping...")

# Sleep until GHA Healthchecks are complete.
# I'm sure there's a better way to get this to not
# stall a docker-compose up --wait, but I don't know
# what it is
time.sleep(125)
