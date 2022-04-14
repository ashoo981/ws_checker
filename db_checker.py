import psycopg2


try:

    conn = None
    dbname = 'atakumgis20210922'
    sqlidx = ("""select    t.relname as table_name ,a.attname as column_name ,count(*) as say from pg_class t,pg_class i,  
      pg_index ix,    pg_attribute a     where    t.oid = ix.indrelid    and i.oid = ix.indexrelid    and a.attrelid = t.oid   
       and a.attnum = ANY(ix.indkey)        and t.relkind = 'r'	group by table_name,column_name	having count(*)>1;""")
    conn = psycopg2.connect ("dbname ='atakumgis20210922' user='postgres' password='q1w2e3r4t5y6' host='172.72.239.180' port='5432'")
    cursor = conn.cursor()
    cursor.execute ("""select f_table_name,f_geometry_column,srid from geometry_columns 
    where f_table_name in (select table_name from information_schema.tables  where table_schema='public');""")
    result = cursor.fetchall()
    # index mükerreler
    cursor.execute(sqlidx)
    resultidx = cursor.fetchall()
    cursor.close()

    
    
    for gidxt in resultidx:

        print(gidxt)
        fileToAppend = open("rpr/idx.txt","a")
        fileToAppend.write("\n")
        fileToAppend.write(  dbname + "_mükerrer index "+ str(gidxt))
        fileToAppend.close()     
    # gtype ve srid kontrol
       
    for gez in result:
        tablo =  gez[0]
        geom = gez[1]
        print(tablo)
        sqlgtype = ("select distinct geometrytype (\""+ f"{geom}" +"\") from  \"" + f"{tablo}" + "\"  ;"  )
        sqlsrid = ("select distinct srid (\""+ f"{geom}" +"\") from  \"" + f"{tablo}" + "\"  ;"  )
        #print(sql) 
        cursor = conn.cursor()
        cursor.execute (sqlgtype)
        resgtype = cursor.fetchall()
        cursor.execute (sqlsrid)
        ressrid = cursor.fetchall()
        cursor.close()
        # bir dizi içine tablolar biriktirilecek.
        # aynı tabloya iki kere index verme kontrolu  OK
        
        if len(resgtype)>1:
            print("2 gtype "+ tablo)
                

            fileToAppend = open("rpr/gtype.txt","a")
            fileToAppend.write("\n")
            fileToAppend.write(dbname +"_mixed gtype "+ str(tablo))
            fileToAppend.close()

        if len(ressrid)>1:
            print("2 srid "+ tablo)   
            fileToAppend = open("rpr/mixed_srid.txt","a")
            fileToAppend.write("\n")
            fileToAppend.write(dbname + "_mixed srid "+ str(tablo))
            fileToAppend.close()         

                




    print("Bitti")
except Exception as e:
    print ('Error:',e)