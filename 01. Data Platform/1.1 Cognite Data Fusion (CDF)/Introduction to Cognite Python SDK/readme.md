# Introduction to Cognite Python SDK
You will work hands-on with live data from the Valhall Oil Platform in the North Sea.

CDF project: publicdata
Google Colab: https://colab.research.google.com/drive/1ipzGTLQnYUWoBbxOerX_A6CxdcnyCrBt#offline=true&sandboxMode=true


## Assets

Read the information below detailing the types of asset searches, and run the code yourself in the Colab tutorial notebook. The code in this section is found under Section 2 of the Colab Notebook. After running the code, try it out yourself with the question below!

There are thousands of Assets in CDF, we will have a look at a few examples of list and search possibilities.

List Assets
The client.assets.list(limit=5) function retrieves the first `limit` number of assets, and returns them as an AssetList. This function is mainly useful when retrieving all assets from a small tenant.

client.assets.list(limit=5)
Search Assets
Generally, we would want to search for one or more specific assets and apply filters when retrieving records. The client.assets.search() function allows you to search by a specific property of the asset, including its name, description, and more.

Fuzzy Search by Name
Before searching, we will decide on which asset we want to explore.

Some example asset names are:

23-HA-9103
23-PV-92538
23-VG-9101
After choosing an asset to search for, a fuzzy search will generate a list of assets that approximately match the search. The search by name includes results that are similar in name, but not necessarily an exact match.

asset_name = "23-HA-9103" 
assets = client.assets.search(name=asset_name)
 

Retrieve a specific asset
If you want to retrieve one particular asset, you need to know either its ID or its external ID. Here we fetch 

identifier = "WMT:23-HA-9103"
client.assets.retrieve(external_id=identifier)

## Events

Read the information below detailing the types of events searches, and run the code yourself in the Colab tutorial notebook. The code in this section is found under Section 3 of the Colab Notebook.

Alerts and work orders monitor heavy assets in the industrial world and they are crucial to avoid downtime. Alerts generated from sensors and control systems are stored in CDF as events. The same is true for maintenance work orders. 

There are typically millions of Events in CDF, so we will only have a look at a few examples. As for assets, we can search for events, but will not look at that in this training. If you want to read more about event functionalities, you can read here. 

List Events
The client.events.list(limit=5) the function retrieves the first `limit` events, and returns them as EventList. This function is mainly useful when retrieving all events from a small tenant.

client.events.list(limit=5) 
 


## What is the purpose of a fuzzy search? 

    [ ]Find data with no specifications
    [X]Find data that approximately match specifications 
    [ ]Find data that exactly match specifications

Example:
Fuzzy Search by name
The search by name includes results that are similar in name, but not an exact match.

```
asset_name = "23-HA-9103"
assets = client.assets.search(asset_name)
print(assets[:3])
```

## What is the purpose of filtering? 

    [X]Find data that exactly match specifications
    [ ]Find data with no specifications
    [ ]Find data that approximately match specification


Retrieve a specific asset
The client.assets.retrieve() interface provides the same information for one specific asset based 

```
indetifier =  "WMT:23-HA-9103"
asset = client.assets.retrieve(external_id = indetifier)
print(f"Name: {asset.name}, description: {asset.description}")
```

## What is the description of asset 23-FE-9106A?
(You will need to run some code to answer this question)

    [X]1ST STAGE COMPRESSOR LUBE OIL HEATER
    [ ]1ST STAGE COMPRESSOR GAS SEAL FILTER A
    [ ]1ST STAGE COMPRESSOR LUBE OIL FILTER B
    [ ]1ST STAGE COMPRESSOR NITROGEN FILTER B

## How many children does asset 23-PDT-92530 have?

(You will need to run some code to answer this question)

    [ ]2
    [X]3
    [ ]4
    [ ]7

Example: 
```
asset_name =  "WMT:23-PDT-92530"
subtree = client.assets.retrieve_subtree(external_id = asset_name) 
 # Remove the root asset from the list of assets to count only the childs
subtree.remove(asset_name)
print(len(subtree))
```