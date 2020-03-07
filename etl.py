import pandas as pd
import sqlite3
from queries import *

def label_vehicle_id(row, classes, class_labels):

    for label in class_labels:
        if row[0] == label:
            ret_str = class_labels[label]+str(classes[row[0]]).zfill(3)
            classes[row[0]] += 1
            return ret_str    
        
        
def process_vehicle_data(cur, conn):

    data = pd.read_csv('GTA_vehicle.csv')
    df = pd.DataFrame(data)


    df.head()
    #lets get rid of the header row
    df.columns = df.iloc[0]
    df = df[1:]

    df.tail()
    #get rid of the last two rows
    df = df[:491]

    #theres also unecessary rows for each new vehicle class
    #lets get rid of those too
    df = df[df['Vehicle_Name'].notna()]

    #drop the columns we don't need    
    df = df.drop(df.columns[[3,4,10,11,12,13,14,15,16]], axis=1)

    #get rid of the dollar signs and commas
    df['Buy_Price'] = df['Buy_Price'].apply(lambda x: str(x).replace(',','')[1:])

    #convert types
    df[['Speed','Accel', 'Brake','Handl']] = df[['Speed','Accel', 'Brake','Handl']].astype(float)    
    df['Capacity'] = df['Capacity'].astype(int)    

    #change all the invalid values to None in order to change them to floats
    df.loc[df['Buy_Price']=='an','Buy_Price'] = None   
    df.loc[df['Buy_Price']=='','Buy_Price'] = None

    df['Buy_Price'] = df['Buy_Price'].astype(float)
    #now that they are floats, we can change all the NaN to the median values of their respective glass
    df['Buy_Price'] = df.groupby('Vehicle_Class')['Buy_Price'].apply(lambda x: x.fillna(x.median()))

    #add a new column for unique ids for each vehicle
    df.Vehicle_Class.unique()
    classes = { i:0 for i in df.Vehicle_Class.unique() }
    class_labels = {
        'SUPER':'SUP', 'SPORTS':'SPO', 'SPORTS CLASSIC':'SPC', 'MUSCLE':'MUS', 
        'SEDANS':'SED', 'COUPES':'COU', 'COMPACT':'CMP', 'SUVs':'SUV', 'OFF-ROAD':'OFR',
        'MOTORCYCLES':'MOT', 'GANG':'GAN', 'VANS':'VAN', 'EMERGENCY':'EME', 
        'SERVICE':'SER', 'MILITARY':'MIL', 'COMMERCIAL':'COM', 'INDUSTRIAL':'IND',
        'HELICOPTERS':'HEL', 'PLANES':'PLA', 'BOATS':'BOA', 'CYCLES':'CYC'}
                
    df['Vehicle_id'] = df.apply(lambda row: label_vehicle_id(row, classes, class_labels), axis=1)   
    


    for name, label in class_labels.items():
        cur.execute(vehicle_class_insert, (label, name))
        conn.commit()
        
    for row in df.values:
        vclass, vname, price, capacity, speed, accel, brake, handl, vid = row
        
        vehicle_data = (vid, buffer(vname), price, capacity, speed, accel, brake, handl, class_labels[vclass])
        cur.execute(vehicle_insert, vehicle_data)
        conn.commit()
    
def main():
    """
    Driver main function.
    """

    conn = sqlite3.connect('GTA_Vehicles.db')
    cur = conn.cursor()
    
    process_vehicle_data(cur, conn)
    print('data processing success')
    
    conn.close()

if __name__ == "__main__":
    main()
      
    
    
    
    
    
    
    
    
    
    
    
