import os
import sys
import datetime
import meraki
from pprint import pprint

api_key = os.getenv("MERAKI_API_KEY") #get os env API key

def instantiateAPI(api_key):
    return meraki.DashboardAPI(api_key, suppress_logging=True)


def organizations(dashboard, org_name):
    orgs = dashboard.organizations.getOrganizations()
    for value in orgs:
        if value["name"] == org_name:
            return value["id"]
        else:
            print('Organisation name under your API key does not exist!')
            sys.exit()

def networks(dashboard, org_id):
    return dashboard.organizations.getOrganizationNetworks(org_id)

def main():
    print(f'getNetworks with your Organisation name {datetime.datetime.now()}')
    org_name = input("Input the name of your organisation: ")
    dashboard = instantiateAPI(api_key) #instantiate client API
    org_id = organizations(dashboard, org_name) #makes getOrganisations call, and returns org_id
    print(f'Your org_name {org_name} has an org_id of {org_id}')
    print(f'Outputting network information for {org_name} org: \n')
    pprint(networks(dashboard, org_id)) #makes getNetworks call with org_id 

if __name__ == "__main__":
    main()


