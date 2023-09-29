from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthDeviceCode

TENANT_ID = "48d5043c-cf70-4c49-881c-c638f5796997"
CLIENT_ID = "1b90ede3-271e-401b-81a0-a4d52bea3273"
BASE_URL = "https://api.cognitedata.com"

oauth_provider = OAuthDeviceCode(
    authority_url=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_id=CLIENT_ID,
    scopes=[f"{BASE_URL}/.default"],
)
client = CogniteClient(
    ClientConfig(
        client_name="Cognite Academy: Intro to PySDK",
        base_url=BASE_URL,
        project="publicdata",
        credentials=oauth_provider,
    )
)

#Asset themselves are organized into asset hierarchies
#For example, one asset can represent a water pump that is part of a larger subsystem on an oil platform asset.
#At the top of each asset hierarchy is a root asset (for example, an oil platform). 
#Each project can have multiple root assets, and all assets under the root asset must have a name and a parent asset.
#asset_id =  5482096081057609
#subtree = client.assets.retrieve_subtree(id=asset_id) 
#print(subtree[:5])

#asset_name =  "WMT:23-PDT-92530"
#subtree = client.assets.retrieve_subtree(external_id = asset_name) 
 # Remove the root asset from the list of assets to count only the childs
#subtree.remove(asset_name)
#print(len(subtree))



#asset_name =  "23-PI-96145"
#asset_id =  1418893254875430

#subtree = client.assets.retrieve_subtree(id = asset_id)
 # Remove the root asset from the list of assets to count only
#subtree.remove(asset_name)
#print(len(subtree))

# 2 - 0

#asset_id =  2539007469802785

#subtree = client.assets.retrieve_subtree(id = asset_id)
 # Remove the root asset from the list of assets to count only
#subtree.remove(asset_name)
#print(subtree)

# 6 - N

asset_id = 8230264121219051
subtree = client.assets.retrieve_subtree(id = asset_id)
print(subtree)

# 9 - R
#COG-D1NNER!
















