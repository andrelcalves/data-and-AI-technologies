This material will provide you with the know-how and skills to use the tool Cognite Spark Datasource, enabling CDF connection to Spark and Databricks.

Steps to follow:
The course will walk you through the below steps:

How to access Databricks
Practical example:
Work with assets, events, and time-series metadata
Work with data points and files

!["Spark Data Source"](img/spark_data_source.png)

The practical example is split into two parts. Part 1 introduces the resource types (assets, events, and time series). Part 2 introduces datapoints and files. Each part is split into sections covering different topics like aggregations, displaying data, and transforming data.

For every section, you will be asked to: 

Read the information in the course in that section
Run the code in the Python tutorial notebook
Return to the course and answer the check your knowledge questions before proceeding to the next section


## Spark, Databricks and Cognite Spark Data source

### Spark   
What is Spark?

* Spark is a unified analytics engine for large-scale data processing
* It runs on a cluster of computer(s)
* It can read from and write to just about anything
* It’s open source and free to use
* Wildly popular and successful

Why would you need Spark?

* You need to process large amounts of data, where the RAM of one computer is not enough
* You need a convenient and efficient way to transform data
* You prefer the Spark API You need to read/write data from/to external storage
* You need to do machine learning or data engineering using all the nice features in Spark

Spark allows you to perform queries in parallel, thus increasing performance. Spark will process your query and hand it out to a set of executors. These executors can query the API in parallel for each part of the data, each executor using its own cursor. The API handles parallel queries and therefore you get a large speedup on large datasets.

### Databricks
What is Databricks?

* The company was started by Spark founders, they know how to run Spark clusters
* Clusters can be created on-demand, with auto-scaling, auto-termination
* Hosted notebooks are included in their service making collaboration easy
* Users, groups, permissions built-in, secrets are supported
* Login via Azure Active Directory, guest users can be added
* JDBC/ODBC connectivity for business intelligence tools like Power BI

What can you do with Databricks?

* Develop and run Spark code in a notebook, using Python, Scala, SQL or R
* Explore data and collaborate with others
* Run analysis on large amounts of data in a scalable way
* Run ETL jobs on a schedule

When would you use Databricks instead of other tools?

* When your company has an existing subscription that you can use
* You want to run code faster than your computer can handle
* You want to make use of some of Spark’s data science functionality in combination with CDF

!["DataBricks"](img/spark_databricks.png)

Spark is a software running on clusters of computers enabling large-scale data processing. While Databricks is a software that makes it easy to set up and manage these clusters and addition to facilitate collaboration with hosted notebooks. Cognite Spark Datasource is a tool developed by Cognite enabling Spark to write and read from CDF.

client secret: ``` wtA8Q~RJ~puY798LmaoZimEAWUL_plEVKqJj7c8q ```
 
You would need access to Databricks to follow the steps going forward. Please note that you need to have access to a Databricks Enterprise version to continue with the course exercises!

Note: If you don't have access to an enterprise version, kindly proceed by following the course without performing the hands-on.

### Importing Notebook

The next step is to import the practical example notebook into Databricks.

Download the .ipynb file from the summary section below and follow the steps to import it as a notebook to Databricks. 

Import a notebook
You can import an external notebook from a URL or a file.

* Click Workspace Icon Workspace in the sidebar. Do one of the following:
* Next to any folder, click the Menu Dropdown on the right side of the text and select Import.
* In the Workspace or a user folder, click Down Caret and select Import. 
Import notebook
* Upload the .ipynb file that you downloaded from the summary section below.
* Click Import.


### Cluster in Databrics

#### Cluster

