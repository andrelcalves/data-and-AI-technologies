In the previous section, you learned how to fetch and explore the data already in CDF. In this section, you will learn how to create, update, insert, and delete data in CDF.

Every Cognite resource type in CDF has a function that creates it. E.g., AssetsAPI.create to create assets, TimeSeriesAPI.create to create time series, EventsAPI.create to create events, etc. This course will use assets as an example of creating resources in CDF. However, creating resources works the same across all resources, so if you know how to create one, you know how to create all.

Let's look at how to create assets. When looking at the documentation of AssetsAPI.create, you see that the only parameter to pass is Asset or list of assets to create. Only passing this parameter means that you have to create the Asset objects you want to have in CDF locally. If you have more than one asset, then you should collect them in a list. The Asset class is found in cognite.client.data_classes.assets and was described in the General concepts of Cognite Python SDK lesson. Here is an example of creating two assets with name=”asset1” and “asset2”.

from cognite.client import CogniteClient
from cognite.client.data_classes import Asset
c = CogniteClient()
assets = [Asset(name="asset1"), Asset(name="asset2")]
c.assets.create(assets)
 

When creating all the different resources, you can manually contextualize the data. E.g., you can set the parent_id parameter for assets or asset_id for time series.

Note that when creating multiple assets, it is best to add all the assets you want to create in a single list and pass this list to the create function. Using create in a loop is inefficient. 

Hot tip for large asset hierarchies

When you have a lot of assets to create, you need to create them in order so that a parent asset is created before its children. If you don't do this, the API will give you an error message. This can be quite cumbersome if you have half a million assets to create. Luckily, there is special handling for this in the SDK. Use the AssetsAPI.create_hierarchy to do so automatically!

Overview of update
Every Cognite resource type in CDF also has an update function. This function allows you to update already existing data. These functions, like the create functions, work the same across all resources, so when you know one, you know all.

Let's look at how to update events. In the documentation you see that EventsAPI.update takes one parameter: item (Union[Event, EventUpdate, Sequence[Union[Event, EventUpdate]]]) – Event(s) to update. The Event object is the object representing events in CDF, so passing the updated Event object to EventsAPI.update allows you to update said event. Here is an example of how to update the description of an event: 

from cognite.client import CogniteClient
c = CogniteClient()
event = c.events.retrieve(id=1)
event.description = "New description"
res = c.events.update(event)
 

The EventUpdate object allows you to do a partial update of an event without having to fetch the entire event. The equivalent object exists for all other resources, e.g., AssetUpdate for assets, TimeSeriesUpdate for time series, etc. 

Here is an example of updating the description and adding a new field to metadata:

from cognite.client import CogniteClient
from cognite.client.data_classes import EventUpdate
c = CogniteClient()
my_update = EventUpdate(id=1).description.set("New description").metadata.add({"key": "value"})
res = c.events.update(my_update)
 

Just as with create, when updating multiple resources, it is best to add all the updates to a list and then pass it to the update function.

Note: not all fields can be updated, e.g., is_string in a time series is not updatable. For example, you have to delete and recreate your time series if you created it with is_string = True, but wanted is_string = False. Assets can't be moved across asset hierarchies, i.e. changing from/to a different root is impossible.

When creating data points, you have to use an insert function. Three functions allow you to insert data points:

TimeSeriesAPI.data.insert
TimeSeriesAPI.data.insert_multiple
TimeSeriesAPI.data.insert_dataframe
insert allows you to insert lists of data points, where each data point is a tuple (or dictionary) with timestamp and value. Here is an example of how to insert data points into a time series with id = 1 and id = 2. Note that each data point is a tuple in this example:

from cognite.client import CogniteClient
c = CogniteClient()
# with datetime objects
datapoints = [(datetime(2018,1,1), 1000), (datetime(2018,1,2), 2000)]
c.datapoints.insert(datapoints, id=1)
# with ms since epoch
datapoints = [(150000000000, 1000), (160000000000, 2000)]
c.datapoints.insert(datapoints, id=2)
 

For insert_multiple, one has to pass a list of dictionaries where each dictionary contains the external id and data points. Note that each data point is a dictionary in this example:

from cognite.client import CogniteClient
c = CogniteClient()

datapoints = []
# with datetime objects and external id
datapoints.append({"externalId": "1", "datapoints": [{"timestamp": datetime(2018,1,1), "value": 1000},
...                    {"timestamp": datetime(2018,1,2), "value": 2000}]})
# with ms since epoch and id
datapoints.append({"id": 1, "datapoints": [{"timestamp": 150000000000, "value": 1000},
...                    {"timestamp": 160000000000, "value": 2000}]})

c.datapoints.insert_multiple(datapoints)
 

If you have a pandas data frame with data points you want to add to a time series, the SDK has a function for this specific use case. This function takes in three parameters:

dataframe (pandas.DataFrame) – Pandas DataFrame Object containing the time series.
external_id_headers (bool) – Set to True if the column headers are external ids rather than internal ids. Defaults to True.
dropna (bool) – Set to True to skip NaNs in the given DataFrame, applied per column.

Overview of delete
 

The last function of this section is the delete function where you have to pass the ids (or external ids) of the resources you want to delete to the function. However, some resources have extra parameters: for example, AssetsAPI.delete, TimeSeriesAPI.delete, and EventsAPI.delete have the parameter ignore_unknown_ids, which Ignores the ids and external ids that are not found rather than throwing an exception.  This is great way to make sure something is deleted without the fear of exceptions beings raised. AssetsAPI.delete has the parameter recursive, which, when set to True, recursively deletes the whole asset subtrees under given ids.

Here is an example of how to delete 4 assets with id = 1,2 and 3, and external id = “foo”:

from cognite.client import CogniteClient
c = CogniteClient()
c.assets.delete(id=[1,2,3], external_id="foo")