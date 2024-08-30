import json
import os
import time

# get environment variables
postgres_user = os.getenv("POSTGRES_USER")
pgadmin_email = os.getenv("PGADMIN_DEFAULT_EMAIL")
pgadmin_password = os.getenv("PGADMIN_DEFAULT_PASSWORD")


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
            '"postgres", "Host": "postgres", "SSLMode": "prefer", "MaintenanceDB": "postgres"}},'
            '"Credentials": {"email": "%s", "password": "%s"}}' % (pgadmin_email, pgadmin_password)
        )
        data = json.loads(template_string)
        # fix username
        data["Servers"]["1"]["Username"] = postgres_user
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
