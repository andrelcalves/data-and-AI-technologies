# Notebook 2: Deploying a Cognite Function via the SDK

In this notebook, we will learn how to deploy the thermal resistance calculation performed in the previous section as a Cognite Function. We will also look at how we can enable this calculation to take place every 5 minutes through the use of Cognite Functions scheduling.

This notebook covers steps 2-4 of the typical workflow with Cognite Functions: restructuring the code to the handler.py format, deploying the function, and calling and scheduling it.

It’s important that you follow the naming convention we suggest in this course so you can easily find your data in Cognite Data Fusion. In the ds-cognitefunctions project you're working in, we're simulating a collaborative environment where you can see all the data created by your peers. If you prefer not to have your name displayed as part of the data set's name, please choose another unique identifier.
Please pay extra attention to only working with your own data sets. The code in the notebook makes sure that you're only working with your data. However, if you're playing around with the code and writing any CDF resource type, pay extra attention to the name of the data set.
In a production environment, data sets can be used to set read/write access for CDF resources so that users can control who has the right access to their data.

In the following lessons, you will:

Create a client secret that you'll use to schedule your function.
Find a demo of running the code in notebook 2.