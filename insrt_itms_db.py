import psycopg2
import dbauth

# Database credentials for usage in psycopg2.connect
dbcreds = dbauth.getPsqlConnectString();

y = {'_gsm_link' : 'na','company' : 'na','img_url': 'na','Extra_comments': 'na','_model_name': 'na','_2G_Network': 'na','_3G_Network': 'na','_4G_Network': 'na','_SIM': 'na','_Announced': 'na','_Status': 'na','_General_Extra': 'na','_Dimensions': 'na','_Weight': 'na','_Keyboard': 'na','_Body_Extra': 'na','_Type': 'na','_Size': 'na','_Multitouch': 'na','_Protection': 'na','_Display_Extra': 'na','_Alert_types': 'na','_Loudspeaker_': 'na','_3_5mm_jack_': 'na','_Sound_Extra': 'na','_Card_slot': 'na','_Internal': 'na','_Phonebook': 'na','_Call_records': 'na','_Memory_Extra': 'na','_GPRS': 'na','_EDGE': 'na','_Speed': 'na','_WLAN': 'na','_Bluetooth': 'na','_Infrared_port': 'na','_USB': 'na','_NFC': 'na','_DATA_Extra': 'na','_Primary': 'na','_Features': 'na','_Video': 'na','_Secondary': 'na','_Camera_Extra': 'na','_OS': 'na','_Chipset': 'na','_CPU': 'na','_GPU': 'na','_Sensors': 'na','_Messaging': 'na','_Browser': 'na','_Radio': 'na','_GPS': 'na','_Java': 'na','_Colors': 'na','_Games': 'na','_Clock': 'na','_Alarm': 'na','_Languages': 'na','_Features_Extra': 'na','_Battery_Extra': 'na','_Stand_by': 'na','_Talk_time': 'na','_Music_play': 'na','_Price_Group': 'na','_SAR_US': 'na','_SAR_EU': 'na','_MISC_Extra':'na'}

def insert_to_db():
	conn = psycopg2.connect(dbcreds)
	cur = conn.cursor()
	print y
	cur.execute("INSERT INTO models (model_name, Company, Gsm_link, Extra_comments, Image_url, _2G_Network, _3G_Network, _4G_Network, Sim, Announced, Status, General_Extra, Dimensions, Weights, Keyboard, Body_Extra, Type, Size, Multitouch, Protection, Display_Extra, Alert_Types, Loudspeaker, _3_5mm_jack, Sound_extra, Card_Slot, Internal, Phonebook, Call_Records, Memory_Extra, GPRS, EDGE, Speed, WLAN, Bluetooth, Infrared_Port, USB, NFC, DATA_Extra, _Primary, Features, Video, Secondary, Camera_Extra, OS, Chipset, CPU, GPU, Sensors, Messaging, Browser, Radio, GPS, Java, Colours, Games, Clock, Alarm, Languages, Features_Extra, Battery_Extra, Stand_By, Talk_Time, Music_Play, Price_Group, SAR_US, SAR_EU, MISC_Extra ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[y['_model_name'],y['company'],y['_gsm_link'],y['Extra_comments'],y['img_url'],y['_2G_Network'],y['_3G_Network'],y['_4G_Network'],y['_SIM'],y['_Announced'],y['_Status'],y['_General_Extra'],y['_Dimensions'],y['_Weight'],y['_Keyboard'],y['_Body_Extra'],y['_Type'],y['_Size'],y['_Multitouch'],y['_Protection'],y['_Display_Extra'],y['_Alert_types'],y['_Loudspeaker_'],y['_3_5mm_jack_'],y['_Sound_Extra'],y['_Card_slot'],y['_Internal'],y['_Phonebook'],y['_Call_records'],y['_Memory_Extra'],y['_GPRS'],y['_EDGE'],y['_Speed'],y['_WLAN'],y['_Bluetooth'],y['_Infrared_port'],y['_USB'],y['_NFC'],y['_DATA_Extra'],y['_Primary'],y['_Features'],y['_Video'],y['_Secondary'],y['_Camera_Extra'],y['_OS'],y['_Chipset'],y['_CPU'],y['_GPU'],y['_Sensors'],y['_Messaging'],y['_Browser'],y['_Radio'],y['_GPS'],y['_Java'],y['_Colors'],y['_Games'],y['_Clock'],y['_Alarm'],y['_Languages'],y['_Features_Extra'],y['_Battery_Extra'],y['_Stand_by'],y['_Talk_time'],y['_Music_play'],y['_Price_Group'],y['_SAR_US'],y['_SAR_EU'],y['_MISC_Extra']])

	conn.commit()
	cur.close()
	conn.close()

def check_item():
	conn = psycopg2.connect(dbcreds)
	cur = conn.cursor()
	cur.execute("SELECT (%s) from models")
