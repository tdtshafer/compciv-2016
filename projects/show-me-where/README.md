# Show Me Where project

## Travis Shafer


# About the dataset

This database contains fire incidents in San Francisco from 2003 to present.


## Basic facts about the dataset

- The source of the data: [City of San Francisco, Open Data Portal, Pulic Safety](https://data.sfgov.org/data?category=Public%20Safety&dept=&search=&type=datasets)
- The data's landing page: [Fire Incidents](https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric)
- Direct link to the data: [https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD](https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD)
- The data format: CSV
- Number of rows: 391,632 O_o

## Description of data fields

#### Incident Number 

An administrative filing number

#### Exposure Number

Use not clear, but values are 0 and a rare 1

#### Address

Street Address, like “3000 Polk Street”

#### Incident Datea

contains date in MM/DD/YY format

#### Call Number

Another filing number

#### Alarm DtTm

Alarm date and time in MM/DD/YY HH:MM

#### Arrival DtTm

Arrival date and time in MM/DD/YY HH:MM

#### Close DtTm

Close date and time in MM/DD/YY HH:MM

#### City

String of City Name

#### Zipcode

5-digit integer zipcode

#### Battalion

Battalion number like ‘B01’

#### Station Area

One or two digit code for station area

#### Around 50 additional mostly blank columns that will not affect this project

The most interesting would be the fatalities, injuries and property use columns

#### Neighborhood

String of SF neighborhood location

#### Location

(Latitude, Longitude)

#### Anticipated Edits
- I will have to delete an enormous amount of pointless rows
- I’ll have to either geocode by the addresses (which are inconsistent in form) or parse out the lat and long (which I can do fairly quickly.)
- The records go back all the way back to 2003, so I’ll probably parse it down to the year of 2015 or something similar