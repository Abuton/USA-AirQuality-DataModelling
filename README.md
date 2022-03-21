# AirQuality BigData Modelling

![image](https://user-images.githubusercontent.com/40719064/146573808-26ab36dd-6da9-4231-99a6-7c2031ac0574.png)

## Practice

- Learn to model, clense, normalize, shard, map, query and analyze substantial real-world big data (230mb+);
- Understand the data cleansing, normalization and sharding processes by writing PYTHON scripts to process and convert the data to first (cleansed) CSV and then (normalized) SQL;
- Design and implement a relational (MySQL) database and then write a PYTHON script to pipe (import) the SQL into the appropriate tables ensuring all referential integerity constraints are met.
- Construct and implement a set of SQL queries to extract data using various filters and constraints.
- Map (forward engineer) the data to a NoSQL database of your choice (MongoDB, BaseX, CouchBase, ArangoDB etc.)
- Write a short, reflective report on the learning outcomes you have achieved.
- Get exposure to and learn the use of a range of data oriented technologies (databases, python & sql.)
- Learn and use the MARKDOWN markup syntax.

### Context:Measuring Air Quality

Levels of various air borne pollutants such as Nitrogen Monoxide (NO), Nitrogen Dioxide (NO2) and particulate matter (also called particle pollution) are all major contributors to the measure of overall air quality.

For instance, NO2 is measured using micrograms in each cubic metre of air (µg m3). A microgram (µg) is one millionth of a gram. A concentration of 1 µg m3 means that one cubic metre of air contains one microgram of pollutant.

To protect our health, the UK Government sets two air quality objectives for NO2 in their Air Quality Strategy

    The hourly objective, which is the concentration of NO2 in the air, averaged over a period of one hour.

    The annual objective, which is the concentration of NO2 in the air, averaged over a period of a year.

There are 18 stations (monitors):

- 188 => 'AURN Bristol Centre',
- 203 => 'Brislington Depot',
- 206 => 'Rupert Street',
- 209 => 'IKEA M32',
- 213 => 'Old Market',
- 215 => 'Parson Street School',
- 228 => 'Temple Meads Station',
- 270 => 'Wells Road',
- 271 => 'Trailer Portway P&R',
- 375 => 'Newfoundland Road Police Station',
- 395 => "Shiner's Garage",
- 452 => 'AURN St Pauls',
- 447 => 'Bath Road',
- 459 => 'Cheltenham Road \ Station Road',
- 463 => 'Fishponds Road',
- 481 => 'CREATE Centre Roof',
- 500 => 'Temple Way',
- 501 => 'Colston Avenue'

Each line represents one reading from a specific detector. 

Detectors take one reading every hour. If you examine the file using a programming editor, Notepad++ can handle the job, you can see that the first row gives headers and there are another 1408379 (1.4 million+) rows (lines). 
There are 23 data items (columns) per line.

Have fun
