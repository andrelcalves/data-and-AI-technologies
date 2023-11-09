# Introduction to CDF & Grafana
## Congnite Data Source for Grafana

Cognite Data Source for Grafana is a plugin availble at grafana plugins page at [grafana.com](grafana.com).

### Install the Cognite Data Source for Grafana
#### Summary
OBS! Grafana is a third-party visualization tool, that gets updated outside of our control. Grafana will most likely look slightly different in the video, but we try to keep the instructions underneath as up-to-date as we can!


To install the Cognite Data Source for Grafana, 

1.  Navigate to grafana.com, and create your Grafana Cloud Account with user credentials linked to the Azure AD group. For publicdata, your credentials are the same as you use to sign in to Cognite Hub and Cognite Learn.
2.  Log in to your Grafana instance.
3.  Navigate to Connections -> Add new connection and search for Cognite Data Fusion.
4.  Click Install via grafana.com and this opens a new tab. From the new tab, click install plugin. Close the tab and go back to your Grafana instance (you might have to refresh your tab). 

### Generate the client secret

In this lesson, you will generate the client secret needed in the course to perform the hands-on tasks.

* By clicking the create client secret button, you can generate the client secret that will be valid for 30 days from the generation date.
* You can copy the whole client secret via copy to clipboard icon beside the secret and paste it.
* Save the client secret in a secure way as you'd do with a password.
* Use the same client secret and do not generate a new one until your first one gets invalid or expires.
* Please contact support@cognite.com if you have any issues with the client secret.

client secrect: 4.s8Q~2INbA3_fhhShlB3M64ZZnHYeFKaj5N~bwE

### Configure the Cognite Data Source for Grafana

#### Summary
To add Cognite Data Source to your Grafana instance:

1.  Navigate to Connections -> Data Sources from your dashboard and click Add data source.
2.  Search for the Cognite Data Fusion data source and click Select.
Now, let's configure the data source. 
3.  Enter the project name as publicdata and api.cognitedata.com as API Host.
4.  Disable Forward OAuth identity if not disabled.
5.  Enable OAuth2 client credentials.
6.  Fill in the following credentials.
 Token URL: 
 https://login.microsoftonline.com/48d5043c-cf70-4c49-881c-c638f5796997/oauth2/v2.0/token
 Client Id: 1b90ede3-271e-401b-81a0-a4d52bea3273
7.  Enter your client secret 
 Scope: https://api.cognitedata.com/.default
8.  Then Click Save & Test to validate your Cognite credentials. It says your Cognite credentials are valid and we are good to go.

### Plot time series

#### Summary
Now that we have added the Cognite Data Source, let's go through how to create a dashboard with timeseries data from Cognite Data Fusion (CDF)

 1. Let's start by creating a dashboard. Click on Dashboards in the left sidebar and click New and New dashboard. 

2.  From the dashboard view, add visualization.

3. Select the data source you created. Most likely named either publicdata or Cognite Data Fusion. 

4.  The query constructor tab below the chart allows you to choose how you want to select timeseries for the dashboard: 
Timeseries search option - Fetches data from a specific time series based on name or description
Timeseries from Asset option- Fetches data from time series related to a specific asset based on the name or description of the asset.
Timeseries Custom Query option - Fetches timeseries that match a query you input.
5. In this example, we know which timeseries we want to visualize so we use the Timeseries search option to search for the timerseries. Let's go ahead and type pi:160885 in the external id field. 

6. You can also specify the aggregation and granularity for the query. By default, the aggregation is average and the granularity is calculated based on the time interval selected for the chart. We will use average aggregation and hour for granularity.

7. The time series matching our selection should be rendered in the chart area. If necessary, you can adjust the time frame in the top right corner of the chart area to show the relevant period. In this example, we want to visualize data from the previous year.

#### Introduction to custom queries

#### Summary
You can use the Custom Query tab if you want more fine-grained control of which time series you are fetching. You can use a combination of arithmetic operations and functions to define your query, and use a special syntax to fetch synthetic time series (STS).

Let's go ahead and visualize a specific time series by using its assetID. For example: ts{assetIds=[5231415482805125]}. The query requests a time series where the assetID equals this number, 5231415482805125.

### Adding events as annotations

Summary
You will now learn how to visualize events as annotations on your dashboard. In this exercise, We will visualize workorder events as annotations on the timeseries dashboard from the previous example.

1.  Navigate to your dashboard's settings, and select Annotations from the left side.
2.  Click Add Annotation Query
3.  To name your annotations, type Workorders.
4.  Select your CDF project in the Data Source field
5.  Specify the query to fetch and filter events from CDF. For example: events{assetIds=[5231415482805125], type="Workorder"}. The query filters on assetID and type.
6.  Save your changes and return to the dashboard.
7.  Now, your workorder events appear as annotations on your dashboard!