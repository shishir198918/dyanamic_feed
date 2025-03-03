import psycopg2 as pg



#resource=[{"url":"https://remoteok.com/rss","head_tag":"","update_tag":""},{"url":"https://weworkremotely.com/remote-jobs.rss","head_tag":"","update_tag":""},{"url":"https://hasjob.co/feed","head_tag":"entry","update_tag":"published"}]



def connection(fun)->None|list:
    def Db_connect(argument):
        try:
            conn=pg.connect(dbname="jobs",
                        port="5432",
                        host="localhost",
                        password="5101",
                        user="postgres"
                        )
            try:
                table=conn.cursor()
                query,values=fun(argument)                
                table.execute(query,values)
                result= table.fetchall()
                table.execute(query,values)
                conn.commit()
                table.close()
                return result
    
            except pg.Error as e1:
                print(f"SQL Error:{e1}")
            finally:
                conn.close()
        except pg.Error as e:
            print(f"Connection Error:{e}")
    return Db_connect            


@connection
def insert(argument):

    query="""insert into posted_jobs(title,link,updated,published,location,content)
          values(%s,%s,%s,%s,%s,%s)"""
    values=(argument[0],argument[1],argument[3],argument[4],argument[5],argument[6])

    return query,values



def acess_latest_time_from_query(fun)->str:
    return lambda : fun(argument=None)[0][0]


@acess_latest_time_from_query
@connection
def latest_time(argument=None)->list:
    query=f"""select published from posted_jobs order by published
            desc limit 1"""
    
    return query,()
#print(latest_time())





 
#l=main.to_json(main.connection(url))

#for entry in l:
    #insert(entry)
#print(latest_time(None)[0])    




        


        