#create two table models and error logs with all column names in the database gsm

import psycopg2
import dbauth


# Database credentials for usage in pyscopg2.connect method
dbcreds = dbauth.getPsqlConnectString();

conn = psycopg2.connect(dbcreds)
cur = conn.cursor()


cur.execute("CREATE TABLE models (id SERIAL NOT NULL,model_name TEXT ,Company Text,Gsm_link TEXT ,Extra_comments TEXT ,Image_url TEXT,_2G_Network TEXT ,_3G_Network TEXT ,_4G_Network TEXT ,Sim TEXT ,Announced TEXT ,Status TEXT ,General_Extra TEXT ,Dimensions TEXT ,Weights TEXT ,Keyboard TEXT ,Body_Extra TEXT ,Type TEXT ,Size TEXT ,Multitouch TEXT ,Protection TEXT ,Display_Extra TEXT ,Alert_Types TEXT ,Loudspeaker TEXT ,_3_5mm_jack TEXT ,Sound_extra TEXT ,Card_Slot TEXT ,Internal TEXT ,Phonebook TEXT ,Call_Records TEXT ,Memory_Extra TEXT ,GPRS TEXT ,EDGE TEXT ,Speed TEXT ,WLAN TEXT ,Bluetooth TEXT ,Infrared_Port TEXT ,USB TEXT ,NFC TEXT ,DATA_Extra TEXT ,_Primary TEXT ,Features TEXT ,Video TEXT ,Secondary TEXT ,Camera_Extra TEXT ,OS TEXT ,Chipset TEXT ,CPU TEXT ,GPU TEXT ,Sensors TEXT ,Messaging TEXT ,Browser TEXT ,Radio TEXT ,GPS TEXT ,Java TEXT ,Colours TEXT ,Games TEXT ,Clock TEXT ,Alarm TEXT ,Languages TEXT ,Features_Extra TEXT ,Battery_Extra TEXT ,Stand_By TEXT ,Talk_Time TEXT ,Music_Play TEXT ,Price_Group TEXT ,SAR_US TEXT ,SAR_EU TEXT ,MISC_Extra TEXT);")

#cur.execute("CREATE TABLE models2 (id SERIAL NOT NULL,_model_no TEXT DEFAULT 12,_2G_Network TEXT DEFAULT 12);")

#cur.execute("INSERT INTO models2 (_model_no,_2G_Network) VALUES (%s,%s)",(678,"asad-sds_"))

cur.execute("CREATE TABLE errorlogs (id SERIAL NOT NULL,error_link TEXT);")

conn.commit()
cur.close()
conn.close()
