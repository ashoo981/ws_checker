import psycopg2
from xml.etree import ElementTree
path = r'workspace.xml'
root = ElementTree.parse(path).getroot()
connection_manager_tag = [i for i in root if i.tag == 'ConnectionManager']
tables = connection_manager_tag[0][0][0][9][0]
for table in tables:
    for field in table:
        if field.tag == 'TableName':
            print(field.text)
            tbl =field.text
            print (tbl)
            conn = None
            dbname = 'postgres'
            conn = psycopg2.connect ("dbname ='ankarabbgis20211104' user='postgres' password='q1w2e3r4t5y6' host='192.168.1.135' port='5435'")
            cursor = conn.cursor()
            sql = ("select f_table_name,f_geometry_column,srid from geometry_columns  where f_table_name=   "+ f"'{tbl}'" +";")
            print(sql)
            fileToAppend = open("rpr/ncws_tables.txt","a")
            fileToAppend.write("\n")
            fileToAppend.write(dbname + "tables "+ str(tbl))
            fileToAppend.close()        
            cursor = conn.cursor()
            cursor.execute (sql)
            result = cursor.fetchall()
            cursor.close()
            print  (result[0][0])
            print  (result[0][1])
           
           
            tablo =  result[0][0]
            geom =   result [0][1]
            sqlgtype = ("select distinct geometrytype (\""+ f"{geom}" +"\") from  \"" + f"{tablo}" + "\"  ;"  )
            sqlsrid = ("select distinct srid (\""+ f"{geom}" +"\") from  \"" + f"{tablo}" + "\"  ;"  )
            sqlextend = ("select st_extent (\""+ f"{geom}" +"\") from  \"" + f"{tablo}" + "\"  ;"  )
            print(sql) 
            cursor = conn.cursor()
            cursor.execute (sqlgtype)
            resgtype = cursor.fetchall()
            cursor.execute (sqlsrid)
            ressrid = cursor.fetchall()
            cursor.execute (sqlextend)
            resextend = cursor.fetchall()
            cursor.close()
            if len(resgtype)>1:
                print("2 gtype "+ tablo)
                

                fileToAppend = open("rpr/ncws_gtype.txt","a")
                fileToAppend.write("\n")
                fileToAppend.write(dbname +"_mixed gtype "+ str(tablo))
                fileToAppend.close()

            if len(ressrid)>1:
                print("2 srid "+ tablo)   
                fileToAppend = open("rpr/ncws_mixed_srid.txt","a")
                fileToAppend.write("\n")
                fileToAppend.write(dbname + "_mixed srid "+ str(tablo))
                fileToAppend.close()   


            if len(resextend)==1:
                print("2 gtype "+ tablo)    
                fileToAppend = open("rpr/ncws_resextend.txt","a")
                fileToAppend.write("\n")
                fileToAppend.write(dbname + "_extent "+  str(resextend[0])  + str(tablo))
                fileToAppend.close()   
     