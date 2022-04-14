import psycopg2
import sys
import time
import datetime as d

from xml.etree import ElementTree
path = r'workspace.xml'
root = ElementTree.parse(path).getroot()
connection_manager_tag = [i for i in root if i.tag == 'ConnectionManager']
tables = connection_manager_tag [0][0][0][9][0]
for table in tables:
    for field in table:

         if field.tag == 'TableName' :
            print(field.text)
            tbl = field.text
            print (tbl)
            conn = None
            dbname='ankarabbgis20211104'
            #conn = psycopg2.connect ("dbname ='bandirmagis' user='postgres' password='ntc123*' host='192.168.0.238' port='5432'")
            #conn = psycopg2.connect ("dbname ='bcmcgis20210702' user='postgres' password='q1w2e3r4t5y6' host='192.168.1.135' port='5437'")
            conn = psycopg2.connect ("dbname ='bcekmece20220223' user='postgres' password='q1w2e3r4t5y6' host='192.168.1.135' port='5435'")
            #conn = psycopg2.connect ("dbname ='nilufer20210528' user='postgres' password='q1w2e3r4t5y6' host='127.0.0.1' port='5434'")
            cursor = conn.cursor()
            start_time = int(time.time()*1000)
            print ("başlangıç:" + str( start_time))
            sql = ("select count (*) from  "+ f"{tbl}" +"; ")
            cursor.execute (sql)
            result = cursor.fetchall()
            print ()
            cursor.close()
            last_time=int(time.time()*1000)
            print ("bitiş:" + str( last_time))
            print (sql)
            print ( "fark:" + str( float( last_time-start_time)))

            fileToAppend = open("rpr/layer_count_time.txt","a")
            fileToAppend.write("\n")
            fileToAppend.write(dbname + ': ' +tbl +': '+ str(result[0][0])+ ' ' +  str( float( last_time-start_time)) + ' milisecons')
            fileToAppend.close()




            #start_time = time.time()
            #last_time=time.time()
            
