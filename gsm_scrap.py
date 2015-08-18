import requests
from bs4 import BeautifulSoup
import psycopg2
import dbauth
y ={}

# Database credentials for psycopg2.connect
dbcreds = dbauth.getPsqlConnectString()

def dict_y_update():
	y.update({'_gsm_link' : 'na','company' : 'na','img_url': 'na','Extra_comments': 'na','_model_name': 'na','_2G_Network': 'na','_3G_Network': 'na','_4G_Network': 'na','_SIM': 'na','_Announced': 'na','_Status': 'na','_General_Extra': 'na','_Dimensions': 'na','_Weight': 'na','_Keyboard': 'na','_Body_Extra': 'na','_Type': 'na','_Size': 'na','_Multitouch': 'na','_Protection': 'na','_Display_Extra': 'na','_Alert_types': 'na','_Loudspeaker_': 'na','_3_5mm_jack_': 'na','_Sound_Extra': 'na','_Card_slot': 'na','_Internal': 'na','_Phonebook': 'na','_Call_records': 'na','_Memory_Extra': 'na','_GPRS': 'na','_EDGE': 'na','_Speed': 'na','_WLAN': 'na','_Bluetooth': 'na','_Infrared_port': 'na','_USB': 'na','_NFC': 'na','_DATA_Extra': 'na','_Primary': 'na','_Features': 'na','_Video': 'na','_Secondary': 'na','_Camera_Extra': 'na','_OS': 'na','_Chipset': 'na','_CPU': 'na','_GPU': 'na','_Sensors': 'na','_Messaging': 'na','_Browser': 'na','_Radio': 'na','_GPS': 'na','_Java': 'na','_Colors': 'na','_Games': 'na','_Clock': 'na','_Alarm': 'na','_Languages': 'na','_Features_Extra': 'na','_Battery_Extra': 'na','_Stand_by': 'na','_Talk_time': 'na','_Music_play': 'na','_Price_Group': 'na','_SAR_US': 'na','_SAR_EU': 'na','_MISC_Extra':'na'})


def connect_to_db():
	global cur, conn
	conn = psycopg2.connect(dbcreds)
	cur = conn.cursor()

def disconnect_to_db():
	conn.commit()
	cur.close()
	conn.close()

def function3(link4):
	'''scrap all the phone attribute from the page ie http://www.gsmarena.com/apple_ipad_air-5797.php
	 and add it to the database '''
	try:
		dict_y_update()
		data3 = requests.get(link4)
		soup5 = BeautifulSoup(data3.text)
		soup6 = BeautifulSoup(str(soup5.div(id="specs-list")))

		def empty_tbl_dt1():
				p = "_" + tbl_dt1.get_text().replace(u'\xa0','h').replace(u'\xc2','h').replace(u' ','_').replace(u'.','_').replace(u'-','_')
				if p == ("_h"):
					return "_" + table.th.get_text() + "_Extra"
				else: 
					if p == ('_hh'):
						return "_" + table.th.get_text() + "_Extra"
					else:
						return p
		Comments = ''
		for para in soup6.find_all('p'):
			Comments = Comments + para.get_text() + ". "
		Extra_comments = str(Comments.encode('utf-8').replace('[. ',''))
		model_name = soup5.h1.get_text()
		img_url = BeautifulSoup(str(soup5.div(id="specs-cp-pic"))).img["src"]
		print model_name, img_url , Extra_comments
		company = model_name.split()[0]
		try:
			connect_to_db()
			cur.execute("SELECT * from models where model_name = (%s)",[model_name])
			cur.fetchone()[1]
			print "--------------Alredy Present In Database-------------------"
		except:
			for table in soup6.find_all("table"):
				soup7 = BeautifulSoup(str(table))

				for tbl_dt1,tbl_dt2 in zip(soup7.find_all("td",class_="ttl"),soup7.find_all("td",class_="nfo")):
						#print empty_tbl_dt1(), "---------" , tbl_dt2.get_text().encode("utf-8")
						y.update({"_model_name":model_name,"_gsm_link":link4,"img_url":img_url,"Extra_comments":Extra_comments,"company":company})
						y.update({empty_tbl_dt1():tbl_dt2.get_text().encode("utf-8")})

			print "--------------------------------------------------------"

			for key,value in dict.items(y):
					print key ,"--" ,value
			print "--------------------------------------------------------"
			print "--------------------------------------------------------"
			connect_to_db()
			cur.execute("INSERT INTO models (model_name, Company, Gsm_link, Extra_comments, Image_url, _2G_Network, _3G_Network, _4G_Network, Sim, Announced, Status, General_Extra, Dimensions, Weights, Keyboard, Body_Extra, Type, Size, Multitouch, Protection, Display_Extra, Alert_Types, Loudspeaker, _3_5mm_jack, Sound_extra, Card_Slot, Internal, Phonebook, Call_Records, Memory_Extra, GPRS, EDGE, Speed, WLAN, Bluetooth, Infrared_Port, USB, NFC, DATA_Extra, _Primary, Features, Video, Secondary, Camera_Extra, OS, Chipset, CPU, GPU, Sensors, Messaging, Browser, Radio, GPS, Java, Colours, Games, Clock, Alarm, Languages, Features_Extra, Battery_Extra, Stand_By, Talk_Time, Music_Play, Price_Group, SAR_US, SAR_EU, MISC_Extra ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[y['_model_name'],y['company'],y['_gsm_link'],y['Extra_comments'],y['img_url'],y['_2G_Network'],y['_3G_Network'],y['_4G_Network'],y['_SIM'],y['_Announced'],y['_Status'],y['_General_Extra'],y['_Dimensions'],y['_Weight'],y['_Keyboard'],y['_Body_Extra'],y['_Type'],y['_Size'],y['_Multitouch'],y['_Protection'],y['_Display_Extra'],y['_Alert_types'],y['_Loudspeaker_'],y['_3_5mm_jack_'],y['_Sound_Extra'],y['_Card_slot'],y['_Internal'],y['_Phonebook'],y['_Call_records'],y['_Memory_Extra'],y['_GPRS'],y['_EDGE'],y['_Speed'],y['_WLAN'],y['_Bluetooth'],y['_Infrared_port'],y['_USB'],y['_NFC'],y['_DATA_Extra'],y['_Primary'],y['_Features'],y['_Video'],y['_Secondary'],y['_Camera_Extra'],y['_OS'],y['_Chipset'],y['_CPU'],y['_GPU'],y['_Sensors'],y['_Messaging'],y['_Browser'],y['_Radio'],y['_GPS'],y['_Java'],y['_Colors'],y['_Games'],y['_Clock'],y['_Alarm'],y['_Languages'],y['_Features_Extra'],y['_Battery_Extra'],y['_Stand_by'],y['_Talk_time'],y['_Music_play'],y['_Price_Group'],y['_SAR_US'],y['_SAR_EU'],y['_MISC_Extra']])
			disconnect_to_db()
			y.clear()
			dict_y_update()
	except:
		connect_to_db()
		cur.execute("INSERT INTO errorlogs (error_link) VALUES (%s)",[link4])
		disconnect_to_db()
		y.clear()
		dict_y_update()


def function1(link3):
	'''returns all the page to be scrap of a particular company http://www.gsmarena.com/samsung-phones-9.php
	It will extract all the navigation link present on the bottom of the page'''
	data2 = requests.get(link3)
	soup3 = BeautifulSoup(data2.text)
	soup4= BeautifulSoup(str(soup3.div(class_="nav-pages")))
	if soup4.get_text() == '[]': #some pages have no navigation pages thats why if is used
		print link3
		function2(link3)
		print "----------------------------------------------"
	else:
		print link3
		function2(link3)
		link1=  "http://www.gsmarena.com/"+ soup4.a['href']
		print link1
		function2(link1)
		for links in soup4.find_all('a'):
			link2 = "http://www.gsmarena.com/" + links['href']
			if link2 == link1:
				pass
			else:
				link5 = "http://www.gsmarena.com/" + links['href']
				print link5
				function2(link5)
		print "-----------------------------------------------------------------"


def function2(phn_links):
	'''return all the phone links of the page ie http://www.gsmarena.com/amazon-phones-76.php'''
	#phn_links = "http://www.gsmarena.com/amazon-phones-76.php"
	phn_links_page = requests.get(phn_links)
	phn_soup = BeautifulSoup(phn_links_page.text)
	phn_soup2 = BeautifulSoup(str(phn_soup.div(class_="makers")))
	for link in phn_soup2.find_all('a'):
		link = "http://www.gsmarena.com/" + link['href']
		function3(link)

link = "http://www.gsmarena.com/makers.php3" #start link to scrap gsm contains all the phone maker company
data = requests.get(link)
soup = BeautifulSoup(data.text)
soup2= BeautifulSoup(str(soup.div(id="main")))
lis = soup2.find_all('a')
for i in range(0,len(lis),2):
	link2 = "http://www.gsmarena.com/"+ lis[i]['href']
	function1(link2)
