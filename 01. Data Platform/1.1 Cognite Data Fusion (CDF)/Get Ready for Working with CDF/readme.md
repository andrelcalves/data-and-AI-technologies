# Get Read for Working With CDF

A data set is a container for data objects. 
A data set has metada with information about the data it contains.
Data sets group and track data by its source

## Login to cognite

https://fusion.cognite.com

Enter _cognite-learn_ as a domain name

![Data Set](img/Data%20Set.png)

To define which data objects belong to a data set, you specify the relevant dataSetId field for each data object. You can read more about data sets here!

During this course, you will create data sets according to the data sources you identified in the use case modeling. You will create two data sets, one for AvevaNet data and one for IFSDB data.

Navigate to Use the Data Catalog (under the Explore category).

Click + Create data set and create a new data set and name it "FirstnameBirthyear-AvevaNet", like Sofie1994-AvevaNet. Add a description and click Create and Done.

DatasetID 5569098741613000

# Working with CDF: Integrate

Ingest data from a source system to CDF and the transform it to CDF Data Model with built-in tranformation tool.

Refresh:

1.  Which CDF resource type is a document that contains information that is related to one or more assets?   
Answer: Assets
2.  Which resource type is a digital representation of objects from the physical world?   
Answer: Assets
3.  Which resource type includes information about something that happens over a period of time?   
Answer: Events

1. First we will upload a CSV file to RAW, this CSV file contain all asset information from AvevaNet data source.

Step 1: Download the CSV file
The first step is to upload a file into Cognite RAW, so we can use this file to transform it into assets.

Download assets.csv
(scroll down to the bottom of the page to the downloadable content)
This CSV file contains information that we will use to make assets and build the asset hierarchy.
On a customer project, this is often how the assets are loaded into CDF the first time, via a data dump. Data pipelines are then often built to make sure that changes in their assets are reflected in CDF as well (we will not do this in this course). 

Step 2: Upload the CSV file to staging area 
Log in to the project in CDF (if you haven't already)

Navigate to Prepare data for transformation under the Integrate module. 

![Prepare data](img/prepare%20data%20for%20transformation.png)

Click the + (plus) button to create a database and name it FirstnameBirthyear (for example, Sofie1994). 

Create a table by clicking on the + Create Table button under the name of your database, and name it assets.

Upload the assets.csv file
Choose the option "I don't know the primary key" when uploading.
(After creating your table, there is a blue Upload CSV button that you can click. You can either drag the file into that window or click in to upload the CSV file. Then click Confirm Upload.)

When the file is uploaded, you will take a look at the data in the Raw Explorer. This information might not tell you much, and it often doesn’t, but for the subject matter experts, this makes a lot of sense.

Why do we do this?

We need to upload this file to be able to create the assets and the asset hierarchy. Without this, we will not be able to see how the different components on the oil platform (presented by assets) are connected.

## Asset Transformation

Now we want to complete the following steps to transform the CSV-file into assets.

Navigate to Transform data under the Integrate module (if you cannot access it, try to refresh the page).


![Transformation](img/transformation%20data.png)

Click + Create button to create a new transformation and use FirstNameBirthYear-Assets (for example Sofie1994-Assets) as a name. A unique external ID for your transformation will be generated automatically.

From the Restrict access to the transformation drop-down, search for and select the FirstnameBirthyear-AvevaNet dataset you created in the previous course. Then, click Next step.

![Transformation](img/transformation%20data%20create.png)

Fill out the following to create your Assets transformation.
Target data model: CDF resource types 
Target resource type: Asset hierarchy
Action: Create or Update
For incoming NULL values on updates: Keep existing values (Default)

Click Create.
Click Switch to SQL Editor.

![SQL Editor](img/sql%20editor.png)

 Create a query (or copy the query below) to fit your data into the target schema.
OBS! Remember to replace 1234567890 with your dataset id ( for the FirstnameBirthyear-AvevaNet data set) and FirstnameBirthyear with your first name and birth year.

SELECT
concat('AndreAlves1979:',loc) as externalId,
IF(parent_loc='' OR parent_loc IS NULL, '', concat('AndreAlves1979:',parent_loc)) AS parentExternalId,
CAST(lastUpdatedTime AS STRING) AS name,
to_metadata(*) AS metadata,
description AS description,
5569098741613000 AS dataSetId
FROM `AndreAlves1979`.assets

## Complete data set documentation

Navigate to Use the Data Catalog under Explore and find your data set.

By clicking the name of the data set, you enter it and find an overview of it. It should now show you that it contains 36




Click three dots -> Edit from the upper right corner.

![Data SetEdit](img/dataset%20edit.png)
 
We want to fill out as much information here as possible to add documentation for the data set.
1. Document data extraction: Click on the section. Type in 'AvevaNet' as Source, and select your database and assets table. Then click Save.

2. Document data transformations: Click on the section. We have not used any external transformations, so there is no need to fill out anything there. Select the CDF SQL transformation that has been used. Then click Save.

3. Add documentation: Click on the section. It is optional to fill out the Owner name and Owner email, but a data set should have a responsible owner. You can also choose to make your data set Governed. There is no need to upload documents, but those should have been uploaded here if we had some relevant documents. Then click Save.
Click Done to update your data set. 


### Events

Now we will move on to events. 
First, create a new data set named FirstnameBirthyear-IFSDB. You can do this under the Manage button as you did in the Get ready for Working with CDF course.
(Note: This dataset has a different id than the AvevaNet data set, so remember to use the right dataset id going forward!)





