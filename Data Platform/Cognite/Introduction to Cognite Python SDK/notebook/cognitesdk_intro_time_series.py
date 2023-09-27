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

#Time Series with their corresponding datapoints contains the bulk of information in the CDF. 
# Time Series are generally linked to an asset through the asset_id field. 
# The time_series.list() method has a variety of filters, all are listed in the SDK. 
asset_id =  5482096081057609

subtree = client.assets.retrieve_subtree(id=asset_id) 

all_timeseries = subtree.time_series() 
print(f"{len(all_timeseries)} time series linked in subtree") 
print(all_timeseries[:5])
print(client.assets.retrieve(id=all_timeseries[0].asset_id))

#View data points for a specific time series
#Now that we have a list of all of the time series connected with our asset subtree, we can retrieve data points for a few of them.

# A Datapoint in the CDF is stored as a key-value pair, with key being the timestamp and value of course being the value - like a sensor reading. 
# The timestamp is the time since epoch, given in milliseconds. 

print("Datapoint:")
print(client.time_series.data.retrieve(external_id="pi:160184", start="10d-ago", end="now", limit=10))













