# Learn how to use the cognite pyhton sdk

## List()

We can use list() to list data from any resource type (assets, datasets, events, timeseries, sequences, labels, relashionships) in CDF.

For default the number of itens return in list is 25, to return all the data you must use limit=none

```
client.data_set.list() 
client.data_set.list(limit=5)
client.assets.list() 
client.events.list()
```

### Filters, we can applie filter using Label

the firts one filter is label, for example you can applied labels to your assets and than find by the lables. We must define labels in the resources types before using this filters.

```
from cognite.client.data_classes import LabelFilter

client.assets.list(label=LabelFilter(contains_all=["Region]),limit=5)
or
client.assets.list(label=LabelFilter(contains_any=["NORDIC","BALTIC"]))
```

### Another filter is using metadata


You can define some properties in the metadata to filter your require items

```
# First get some metadata keys to ispect
client.asset.list(limit=5).to_pandas()['metadata'][4]

# Get the asset list satisfying metadata filter
client.asset.list(metadata={'ELC_STATUS_ID':'1211'},limit=5)
```

### Others filters
```
client.data_set.list(write_protected=False)
client.labels.list(limit=5,name="NORDIC") # labels with NORDIC name
client.assets.list(root=True) # assets that are root
client.time_series.list(is_step=True,limit=5) # time series stepwise attribute
client.events.list(start_time={"max":15000000},limit=5)
```

### Iterate over the list
```
for data_set in c.data_sets:
    print(data_set.name) # do something with the data_set
```

When list is too big, then use chunk_size parameter to get the list in chunks
```
for data_set_list in c.data_sets(chunk_size:5)
    print([x.name for x data_set_list]) # do something with the data_set_list
```

## Searching in CDF

Another function that each resource type has is the search function. search is used for data exploration and human-centric use cases, not for programs. This is because search uses fuzzy search, a technique that uses measures of similarity to find data related to the search term. In other words, the matches will be approximate. This means that the matching and ordering of results will change over time. If stable and exact matches are required, use the list function.

Let's take the AssetsAPI.search function as the example in this section. We recommend looking at the documentation for the other search functions, such as the TimeSeriesAPI.search, EventsAPI.search, etc. The parameters in AssetsAPI.search you're able to use are:

name (str) – Fuzzy match on name.
description (str) – Fuzzy match on description.
query (str) – Whitespace-separated terms to search for in Assets. It does a best-effort fuzzy search in relevant fields (currently name and description) for variations of any search terms, and orders the results by relevance.
filter (Union[AssetFilter, Dict]) – Filter to apply. It performs an exact match on these fields.
limit (int) – Maximum number of results to return.
So you can do a fuzzy search on name and description (and both) while using filter to perform exact matches (and limit to limit the number of instances to return, as you have seen for all the other functions).

Searching for something specific doesn't necessarily mean your search has to be equally specific. Sometimes you only recall parts of the data in CDF. We’ll show you the different ways you can search, and various filters to narrow down the results.

You use the name keyword argument to do a single-field fuzzy search on the name. e.g. client.assets.search(name="23-HA-9114",limit=5).
You use the query keyword argument to do a multiple-field fuzzy search.
For an exact search, you can use the filter keyword argument e.g. client.time_series.search(filter={"asset_ids":[275122214623185]}).
You can also use other keyword arguments to help narrow down your search results; see the docstrings or the SDK documentation for more info.

## Retrieve

The last functions to fetch data we will look at in this course are the retrieve and retrieve_multiple functions. Use these functions when you know the ids or external ids of the resources you want to retrieve. The retrieve function is also used when you want to retrieve data points from a time series. For example, you want to retrieve a time series with the id = 1234 and external id = “some_external_id”. To retrieve this time series, you can run 

```
client.time_series.retrieve(id=1234)
client.time_series.retrieve(external_id="some_external_id")
You can retrieve data points using the retrieve function: client.time_series.data.retrieve.
```

In addition to id and external_id, the other parameters you may pass are:

start (Union[int, str, datetime]) – Inclusive start, defaults to 1970-01-01 if not given
end (Union[int, str, datetime]) – Exclusive end, defaults to "now" if not given
aggregates (str | List[str]) – Single aggregate or list of aggregates to return
granularity (str) – The granularity to fetch aggregates at. e.g., ‘1s’, ‘2h’ or ‘10d’.
include_outside_points (bool) – Whether or not to include outside points, only valid when fetching raw datapoints (not aggregated)
ignore_unknown_ids (bool) – Ignore ids and external ids that are not found rather than throwing an exception.
limit (int) – Maximum number of data points to return per time series. Note that it defaults to no limit.
Note that both start and end allow you to pass an integer, a string, or a datetime object. The integer you can pass a UNIX timestamp, with millisecond accuracy. The string you're able to pass are ones like “now”, “1d-ago”, “2w-ago”, etc. The datetime objects are documented here, note that naive datetimes, i.e. ones without a timezone, are assumed to be local time (Python standard interpretation). To alleviate any doubt, always pass timezone-aware datetimes or convert to a UNIX timestamp yourself.

If you want the data points between 2022-01-01 and now, for example, you'll have to run:

```
from datetime import datetime, timezone

dps = client.time_series.data.retrieve(id=1234, start=datetime(2022, 1, 1, tzinfo=timezone.utc), end="now")
 ```

Since all objects have the method to_pandas(), we can use the fact that the pandas data frames have the method plot(). We can, therefore, easily plot this section of the time series, by running:

```
dps.to_pandas().plot()
``` 

The retrieve datapoints endpoint is very flexible, and a lot of different queries can be made. Many different patterns can be found by checking out the documentation for further examples, such as adding aggregates and if you want different aggregates for different time series.

We have broken up the videos on the retrieval functions into three parts:

### Retrieve Part 1

#### Example 01

```
# list all datasets
c.data_set.list()
# than retrieve a specific dataset using de dataset ID
c.data_set.retrieve(id=5548572851312583)
```

#### Example 02

```
# get an example of sequence id
c.sequences.list()[0].id
# than retrieve a specific sequence using ID
c.sequences.retrieve(id=7648572851312583, start=0, end=None)
```

#### Example 03

```
# if od timeseries
c.datapoints.retrieve(id=16865456145, start="8w-ago", end="now")
```

We can also retreive different objects with mutiple id or external ids as showing below

```
client.data_sets.retrieve_multiple(ids=[2452112635370053,5272329852941732])

client.data_set.retrieve_mutiple(external_ids=["OID/VAL/Assets","VAL/FILES/PNIDS"])

```

Use of igonere_unknown_ids=True to ignore external_ids that doesn't match


```
client.data_set.retrieve_mutiple(external_ids=["OID/VAL/Assets","VAL/FILES/PNIDS","TESTE N EXEISTE"], ignore_unknown_ids=True)
```

## Retrieve Part 02

Retrieve all items related to an asset 

```
c.asset.retrieve_subtree(id=671154545454)
```

or

```
asset_obj = c.asset.retrive(id=671154545454)
# direct children of a specific asset
asset_obj.children()
# get the parent of a asset
asset_obj.parent()

#get events of a specific asset
asset_obj.events()
# get files of a specific asset
asset_obj.files()
# sequences
asset_obj.sequences()
# timeseries
asset_obj.time_series()
```

### Retrieve aggreated data

```
c.datapoints.retrieve_dataframe(external_id=['',''],
    start="10w-ago",
    end="now",
    aggregates=["avarage","sum"],
    granulality="1h"
)
```

### Retrieve latest datapoint

```
c.datapoints.retrieve_latest(external_id='pi:163657', before='5w-ago')[0]
```
