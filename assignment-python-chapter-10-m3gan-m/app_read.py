#megan moore 

import sqlite3

#print("Getting data")
db_name = "chinook.db"
with sqlite3.connect(db_name) as conn:
    sql_command2 = "SELECT trackid FROM playlist_track WHERE playlistid=12"
    cursor = conn.execute(sql_command2)
    trackidlist = cursor.fetchall()
    #print(trackidlist)
    id=list(trackidlist)
    #fix tuple into list without extra "(...),""
    result=[i[0] for i in trackidlist]
    #print(result)
    #convert int list to string list
    result_str=list(map(str,result))
    #print(result_str)

    select_query = "SELECT name, composer, unitprice FROM tracks WHERE trackid="
    
    for x in range(75):
        var=select_query+result_str[x]
        #print(var)
        #print(f"track id: ",result[x])  #used to confirm trackinfo printing matching correct trackid
        var_list=list(cursor.execute(var))
        title=[i[0] for i in var_list]
        a=str(title)[2:-2]
        #print(title)
        #print(a)
        composer=[i[1] for i in var_list]
        b=str(composer)[2:-2]
        #print(composer)
        #print(b)
        unitprice=[i[2] for i in var_list]
        c=str(unitprice)[1:-1]
        #print(unitprice)
        #print(c)
        #print(unitprice_str)
        print(f"Title: ",a,"\b. Composer: ",b,"\b. Unit Price: ",c)
        #result_str2=list(map(str,result2))
        #print(result_str2)
        #print(list(map(str,var_list)))        
        x+=1

#I'm sure there's an easier way to do the above but this was the easiest way for me
#to continually test and confirm I was printing the right info line by line