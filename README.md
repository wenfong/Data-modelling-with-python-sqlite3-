# Data-modelling-with-python-sqlite3-

## **Overview**
In this project, I apply Data Modeling with Sqlite3 and build an ETL pipeline using Python. This project provides another project with some initial data. 


## **Vehicles Dataset**
The dataset is a csv file with most of the vehicles players can buy in the game Grand Theft Auto V.

Sample Record :
```
Vehicle_Class	Vehicle_Name	Buy_Price	Sell_Price	Stealable	Capacity	Speed	Accel	Brake	Handl	Avg w/o Brake	Avg w/o Accel	Avg w/o Speed	Overall	Picture	Notes	Based on

SUPER	Coil Rocket Voltic	$2,880,000	-	No	2	7.8	4.5	3.3	7.7	6.65	6.26	5.17	5.82	http://i.imgur.com/nfOGkZI.jpg	Import/Export update	Tesla Roadster, Lotus Elise, Coil Voltic, Falcon 9 (lol)

```


## Tables

**vehicle**  - Vehicles and all its info
```
vehicle_id, vehicle_name, price, capacity, speed, accel, brake, handl, vehicle_class
```
**vehicle_class**  - what kind of vehicle it is
```
vehicle_class, class_name
```


## Project Files

```queries.py``` -> contains sql queries for dropping and creating tables. Also, contains insertion query template.

```create_tables.py``` -> contains code for setting up database. 

```etl.py``` -> read and process the csv file

## Environment 
Python 2.7

python sqlite3

## How to run

Run the drive program ```main.py``` as below.
```
python main.py
``` 

The ```create_tables.py``` and ```etl.py``` file can also be run independently as below:
```
python create_tables.py 
python etl.py 
```
