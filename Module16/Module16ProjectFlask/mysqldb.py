import mysql.connector

def insertMBTARecord(mbtaList):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3300,
            password="MyNewPass",
            database="MBTAdb"
            )

        mycursor = mydb.cursor()
        #complete the following line to add all the fields from the table
        sql = '''insert into mbta_buses ( 
            bus_id,
            latitude,
            longitude,
            route_num,
            bearing,
            current_status,
            current_stop_sequence,
            direction_id,
            occupancy_status,
            updated_at,
            stop_id,
            trip_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        for mbtaDict in mbtaList:
            #complete the following line to add all the fields from the table
            val = (mbtaDict['bus_id'], 
                mbtaDict['latitude'], 
                mbtaDict['longitude'], 
                mbtaDict['route_num'], 
                mbtaDict['bearing'], 
                mbtaDict['current_status'], 
                mbtaDict['current_stop_sequence'], 
                mbtaDict['direction_id'], 
                mbtaDict['occupancy_status'], 
                mbtaDict['updated_at'], 
                mbtaDict['stop_id'], 
                mbtaDict['trip_id']
                )
            mycursor.execute(sql, val)

        mydb.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()