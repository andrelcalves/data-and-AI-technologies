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

#token_info = client.iam.token.inspect()  # 'iam' stands for: Identity and Access Management

# Print out CDF projects we have access to:
#[project.url_name for project in token_info.projects]




#Retrieving a list of Assets
#The command client.assets.list(limit=5) retrieves the first limit number of assets, and returns it as an AssetList.

print(client.assets.list(limit=5))

#Search for Assets
#The client.assets.search() function allows you to search by a specific property of the asset, including its name, description, etc.

print(client.assets.search("compressor", limit=3))

#Fuzzy Search by name
#The search by name includes results that are similar in name, but not an exact match.

asset_name = "23-HA-9103"
assets = client.assets.search(asset_name)
print(assets[:3])

#Retrieve a specific asset
#The client.assets.retrieve() interface provides the same information for one specific asset based on the provided ID or external ID.

indetifier =  "WMT:23-HA-9103"
asset = client.assets.retrieve(external_id = indetifier)
print(f"Name: {asset.name}, description: {asset.description}")


indetifier =  2011813110741085
asset = client.assets.retrieve(id = indetifier)
print(f"Name: {asset.name}, description: {asset.description}")


