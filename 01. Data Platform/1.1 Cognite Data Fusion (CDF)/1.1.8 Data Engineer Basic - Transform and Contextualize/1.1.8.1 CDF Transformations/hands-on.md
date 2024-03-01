# Introduction to the data
Cognite AS has locations in different parts of the world. For this hands-on exercise we will be using the locations in Norway, the US, and Japan. In Norway and the US, there are also two different office locations. Oslo & Stavanger for Norway, and Austin & Houston for the US.

For this hands-on course, you will work with 3 different CSV files. 

  * The “office” file will give you information about Cognite´s offices and how they are related. 

  * The “sensors” file has information about the temperature and the pressure from the offices´ sensors.

  * The third file “values” has information about the actual values of the temperature/pressure at three different times a day for a period of 30 days.

``` 
/* MAPPING_MODE_ENABLED: false */
/* {"version":1,"sourceType":"raw","mappings":[{"from":"","to":"externalId","asType":"STRING"},{"from":"","to":"parentExternalId","asType":"STRING"},{"from":"","to":"source","asType":"STRING"},{"from":"office_name","to":"name","asType":"STRING"},{"from":"description","to":"description","asType":"STRING"},{"from":"","to":"metadata","asType":"MAP<STRING, STRING>"},{"from":"","to":"dataSetId","asType":"BIGINT"},{"from":"","to":"labels","asType":"ARRAY<STRING>"}],"sourceLevel1":"AndreAlves1979","sourceLevel2":"office"} */

SELECT
SELECT
  IF(
  contains(description, 'Country of office') is true,
  concat('AndreAlves1979:',current_date(), ':','Cognite AS'),
    IF(
    contains(loc_id, '_') is false,
    '',
    concat('AndreAlves1979:',current_date(), ':',substring(loc_id, 0,2)) 
  )	
  ) as parentExternalId,  
  concat('AndreAlves1979:',current_date(), ':',office_name) as externalId,
  cast(`office_name` as STRING) as name,
  cast(`description` as STRING) as description,
  'from RAW' AS source
FROM `AndreAlves1979`.`office` order by description
```