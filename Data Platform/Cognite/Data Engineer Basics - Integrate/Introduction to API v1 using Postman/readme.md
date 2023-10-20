# Postman and Cognite

In this doc, you will use Postman to:

- Set environment variables.
- Make a test API request.
- Find information about time series, assets, and events.
- Download data.

## Set up postman using OpenID connect

### Step 1: Import Postman collection
Import the latest API V1 Postman collection: 
https://storage.googleapis.com/cognite-postman-collections/v1.json

### Step 2: Set up environment variables

Variable:tenant-id		   	

    Type: default
    Initial value:
    Current value:  48d5043c-cf70-4c49-881c-c638f5796997

Variable: Token

    type: default	 	          
    Initial value:
    Current value:  

Variable: baseURL

    type: default	 	
    Initial value:
    Current value:  https://api.cognitedata.com

Variable: project

    type: default
    Initial value:
    Current value: publicdata


### Step 3: Update authorization
Next is to update the authorization in the collection overview of Cognite API v1, fill out the following values mention in the demo:

Type: OAuth2.0
Add auth data to: Request headers
Token name: token_implicit
Grant type: implicit
Callback URL: https://postman.cogniteapp.com/loggedin
Auth URL: https://login.microsoftonline.com/{{tenant-id}}/oauth2/v2.0/authorize
Client id: https://postman.cogniteapp.com
Scope: {{baseURL}}/.default

Cognite Data Fusion (CDF) authenticates your API requests to a project using OpenID Connect (OIDC).

To update the authorization, navigate to the Authorization tab in the collection overview.
Select OAuth 2.0 as Type and Request Headers as Add auth data to.
Select Configure New Token and specify the following configuration options:
Enter a Token Name. For example, token_implicit
Select the Grant Type as Implicit.
Input the Callback URL as https://postman.cogniteapp.com/loggedin 
Enter the Auth URL as https://login.microsoftonline.com/{{tenant-id}}/oauth2/v2.0/authorize 
Input the Client ID as https://postman.cogniteapp.com
And the Scope as {{baseURL}}/.default
Select Client Authentication as Send as Basic Auth header.

