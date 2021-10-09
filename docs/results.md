# Results

The aim of this part is to extract data regarding sport results, football for now.
The process is divided as follows:

## Gather a list of all the supervised teams 
So far, the decided format is `league | name | url | date`
- This is achieved running the following command `python league.py <country> <league>`
  - [ ] the 2 parameters have to be specified into a config for automation purpose
  - [ ] the dataframe generated has to be stored in a persistent way

## Scrape the results according to this list
This will be used to extract relevant information.

## Generate a report based on those data
The focus here will be the rendering of the previously extracted data.
