from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthDeviceCode
from datetime import datetime, timedelta, timezone
from matplotlib import pyplot as plt

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

#Collect Data Points from CDF
#As an example, the following 4 sensors, in the form of time series, were chosen in an effort to estimate the output pressure of a suction cooler.
#Input variables
#FT: Input Flow Rate
#PT: Input Pressure
#TT: Input Temperature
#Output variable
#PT: Output Pressure

#The time series external IDs are defined below:

in_ts_exids = ["pi:160182", "pi:160697", "pi:160882"]
out_ts_exid = "pi:160696"

ts_exids = [*in_ts_exids, out_ts_exid]
train_start_date = datetime(2018, 8, 1, tzinfo=timezone.utc)
train_end_date = train_start_date + timedelta(days=30)

datapoints_df = client.time_series.data.retrieve_dataframe(
    external_id=ts_exids,
    aggregates="average",
    granularity="1m",
    start=train_start_date,
    end=train_end_date,
    include_aggregate_name=False,
    uniform_index=True,
)
datapoints_df = datapoints_df.interpolate().dropna()
datapoints_df.head()

cols = datapoints_df.columns 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
for ax, col in zip(axes.flat, cols):
    ax.plot(datapoints_df[col])

plt.show()

#When we ask for data, and some intervals do not have any values, Cognite Data Fusion is simply not returning anything. 
#We do not want any such gaps in our dataframe, so we specify the argument uniform_index=True which makes sure that the index is evenly spaced with gaps of exactly 1 minute.
#We then proceed to interpolate any missing values with linear interpolation and use .dropna() to get rid of any missing values at the very start- and end of the data (interpolate only works with gaps that are enclosed with actual data).
#Note that without the include_aggregate_name=False option, the aggregate name, "average", would have been appended to the external id to form a unique column name. This is a handy option when fetching various aggregates for the same time series.































