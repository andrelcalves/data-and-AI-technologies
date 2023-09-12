Multiple Choice
1)
Which of the following data engineering capabilities simplifies the work of data engineers on the Databricks Lakehouse Platform? Select three responses.

Flexible machine learning development solutions
x SQL and Python development compatibility
Automatic deployment and data operationsServerless cluster startup times
x End-to-end data pipeline visibility

Multiple Choice
2)
Many organizations use a variety of open-source and proprietary tools for data orchestration, but these tools often have their own limitations. To address the orchestration needs of these organizations, Databricks developed Databricks Workflows.

 

Which of the following is a benefit of using Databricks Workflows for orchestration purposes? Select two responses.

 

Databricks Workflows provides multiple-task workflow functionality only for Delta Live Tables workloadsDatabricks Workflows provides Git-backed version control capabilities to notebooksDatabricks Workflows supports workloads across multiple cloud service providers and toolsDatabricks Workflows supports tasks for data ingestion, data engineering, machine learning, and business intelligence (BI)Databricks Workflows supports automating workloads as long as they are not in notebooks
Single Choice
3)
It can be challenging for a data lakehouse to provide both performance and scalability for all of its query-based workloads to the standards of a data warehouse and a data lake. As a result, Databricks has introduced a technology built atop Apache Spark to further speed up and scale these varied workloads.

 

Which of the following technologies is being described in the above statement? Select one response.

 


Unity Catalog

AutoML

AutoML

Photon

Delta Lake
Multiple Choice
4)
The Databricks Lakehouse Platform architecture consists of a control plane and a data plane.

 

Which of the following resources exists within the Databricks control plane? Select two responses.

 

Cloud object storageCluster configurationsServerless compute resourcesClassic compute resourcesNotebooks
Single Choice
5)
Which of the following describes how the Databricks Lakehouse Platform makes data governance simpler? Select one response.


Unity Catalog provides a different governance solution for each major Databricks Lakehouse Platform Service.

Unity Catalog provides a different governance solution for each workload.

Unity Catalog provides a different governance solution for each cloud.

Unity Catalog provides a single governance solution across workload types and clouds.

Unity Catalog provides a single governance solution fully managed by the Databricks team.
Single Choice
6)
 Which of the following Databricks Lakehouse Platform services or capabilities provides a data warehousing experience to its users? Select one response.


Data Science and Engineering Workspace

Unity Catalog

Delta Lake

Databricks SQL

Databricks Machine Learning
Multiple Choice
7)
Which of the following correctly describes how a specific capability of the Databricks Lakehouse Platform supports a data streaming pattern? Select three responses.

Delta Live Tables processes ETL pipelines on streaming data with advanced monitoring mechanisms.Databricks Workflows automatically passes data from task to task in regular microbatches.Auto Loader continuously and incrementally ingests streaming data.MLflow ingests its automatic experiment tracking data into a stream for continuous monitoring.Structured Streaming enables stream-based machine learning inference.
Multiple Choice
8)
Maintaining and improving data quality is a major goal of modern data engineering.

 

Which of the following contributes directly to high levels of data quality within the Databricks Lakehouse Platform? Select two responses.

 

Simplified machine learning model servingTable schema evolutionBusiness intelligence (BI) tool integrationsApache Spark’s data format flexibilityData expectations enforcement
Multiple Choice
9)
Which of the following compute resources is available in the Databricks Lakehouse Platform? Select two responses.

Serverless Databricks SQL warehousesOn-premises clustersServerless clustersClassic clustersLocal Databricks SQL warehouses
Multiple Choice
10)
Data organizations need specialized environments designed specifically for machine learning workloads.

 

Which of the following is made available by Databricks as part of Databricks Machine Learning to support machine learning workloads? Select four responses.

 

Lakehouse-specific deep learning frameworksSupport for distributed model training on big dataBuilt-in real-time model servingOptimized and preconfigured machine learning frameworksBuilt-in automated machine learning development
Single Choice
11)
Data sharing has traditionally been performed by proprietary vendor solutions, SSH File Transfer Protocol (SFTP), or cloud-specific solutions. However, each of these sharing tools and solutions comes with its own set of limitations. As a result, Databricks helped to develop the solution, Delta Sharing.

 

Which of the following describes Delta Sharing as a solution for data sharing? Select one response.

 


Delta Sharing is a multicloud, open-source solution to securely and efficiently share live data from the lakehouse to any external system.

Delta Sharing is a multicloud, open-source solution for distributing data across a number of compute resources for efficient data shuffling.

Delta Sharing is a multicloud, proprietary solution for efficiently copying and transferring data from the lakehouse to any external system.

Delta Sharing is a multicloud, open-source solution to share data between Databricks workspaces within a single Databricks account.

Delta Sharing is a multicloud, proprietary solution to securely and efficiently share data while maintaining control of the source data.
Multiple Choice
12)
Which of the following is a security feature made available in the Databricks Lakehouse Platform by Unity Catalog? Select two responses.

 

Fine-grained access control on data objectsWorkspace-specific identity managementWorkspace-specific data metastoresDatabricks SQL warehouse access controlSingle-source-of-truth identity management
Multiple Choice
13)
 Which of the following is a benefit of the Databricks Lakehouse Platform being designed to support all data and artificial intelligence (AI) workloads? Select four responses.

Data analysts, data engineers, and data scientists can easily collaborate within a single platform.Data workloads can be automatically scaled when needed.Analysts can easily integrate their favorite business intelligence (BI) tools for further analysis.There is increased need for multiple, specialist platform administrators to maintain each component of the unified platform.Data teams can all utilize secure data from a single source to deliver reliable, consistent results across workloads at scale.
Multiple Choice
14)
A data architect is evaluating data warehousing solutions for their organization to use. As a part of this, the architect is considering the Databricks Lakehouse Platform.

 

Which of the following is a benefit of using the Databricks Lakehouse Platform for warehousing? Select four responses.

 

Engineering capabilities supporting warehouse source dataBuilt-in governance for single-source-of-truth dataLocal development software to integrate with other capabilitiesA rich ecosystem of business intelligence (BI) integrationsBest available price/performance
Single Choice
15)
Which of the following describes the motivation for the creation of the data lakehouse? Select one response.


Organizations needed a single, flexible, high-performance system to support data, analytics, and machine learning workloads.

Organizations needed a reliable data management system with transactional guarantees for their structured data.

Organizations needed to reduce the costs of storing their open-format data files in the cloud.

Organizations needed to be able to develop increasingly complex machine learning workloads using a simple, SQL-based solution.

Organizations needed a way to scale their data lake workloads without investing in additional on-premises hardware.
Single Choice
16)
Unity Catalog offers improved Lakehouse data object governance and organization capabilities for data segregation.

Which of the following is a consequence of using Unity Catalog to manage, organize and segregate data objects? Select one response.


Table metadata is required

Complete data object referencing requires three levels

Data in tables and views must be stored in external storage locations

Views are made available outside of their schemas (databases)

Catalogs exist within schemas (databases)
Single Choice
17)
Which of the following do Databricks SQL users experience when using serverless Databricks SQL warehouses rather than classic Databricks SQL warehouses? Select one response.

 


Performance degradation on long-running queries

Increased total cost of use

Availability of Photon

Expedited environment startup

Availability of automatic scaling
Single Choice
18)
While the Databricks Lakehouse Platform provides support for many types of data, analytics, and machine learning workloads, some organizations prefer to continue using other preferred vendors for use cases like data ingestion, data transformation, business intelligence, and machine learning.


Databricks cannot be used alongside other big data tools and platforms.

Databricks can use cloud service provider capabilities to efficiently share data with other data tools and platforms.

Databricks can be integrated directly with a large number of Databricks partners.

Databricks can be used on-premises to allow for secure, in-house integrations.

Databricks can be used locally to allow developers to manually integrate with other systems.
Multiple Choice
19)
Which of the following describes what challenges a data organization would likely face when migrating from a data warehouse to a data lake? Select two responses.

There are increased cloud storage costs in a data lake.There are increased data reliability issues in a data lake.There are increased performance speeds in a data lake.There are increased security and privacy concerns in a data lake.There are increased data quality guarantees in a data lake
Single Choice
20)
One of the foundational technologies provided by the Databricks Lakehouse Platform is an open-source, file-based storage format that provides a number of benefits. These benefits include ACID transaction guarantees, scalable data and metadata handling, audit history and time travel, table schema enforcement and schema evolution, support for deletes/updates/merges, and unified streaming and batch data processing.

 

Which of the following technologies is being described in the above statement? Select one response.

 


Delta Lake

Unity Catalog

Apache Spark

Photon

MLflow
Multiple Choice
21)
Which of the following architecture benefits is provided directly by the Databricks Lakehouse Platform? Select three responses.

Efficient on-premises optimized hardwareAvailable on and across multiple cloudsBuilt on open source and open standardsUnified security and governance approach for all data assetsScalable, redundant cloud-based data storage
Single Choice
22)
In the past, a lot of data engineering resources needed to be contributed to the development of tooling and other mechanisms for creating and managing data workloads. In response, Databricks developed and released a declarative ETL framework so data engineers can focus on helping their organizations get value from their data

 

Which of the following technologies is being described above? Select one response.

 


Delta Live Tables

Autologging

Databricks Jobs

Delta Lake

Databricks SQL Queries
Single Choice
23)
Which of the following lists the relational entities in order from largest (most coarse) to smallest (most granular) within their hierarchy? Select one response.

 


Catalog → Metastore → Schema (Database) → Table

Metastore → Catalog → Schema (Database) → Table

Schema (Database) → Metastore → Catalog → Table

Metastore → Catalog → Table → Schema (Database)

Schema (Database) → Catalog → Table → Metastore
Multiple Choice
24)
Which of the following is a common problem within a data lake architecture that can be easily solved by using the Databricks Lakehouse Platform? Select three responses.

 

Ineffective partitioningToo many small filesLack of cloud service integrationsLack of ACID transaction supportInability to use open-source data formats
Multiple Choice
25)
In which of the following ways do serverless compute resources differ from classic compute resources within the Databricks Lakehouse Platform? Select two responses.

They exist within the customer cloud accountThey are always running and reserved for a single, specific customer when neededThey are located within the cloudThey result in lower costs by not overprovisioningThey exist within the Databricks cloud account