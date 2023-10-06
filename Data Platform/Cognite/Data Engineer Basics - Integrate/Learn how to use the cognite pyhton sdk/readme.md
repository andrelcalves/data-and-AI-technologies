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