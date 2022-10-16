import psycopg2
import time
import schedule


def worker():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1000",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="feeder")
        cursor = connection.cursor()
        print("Connected...")

        postgres_insert_query = """ 
        update  public.api_feederdata
        set total_amount_of_feed=total_amount_of_feed-(number_of_chicken * feed_per_hen)
        where total_amount_of_feed>=(number_of_chicken * feed_per_hen)
        """
        query2 = """update  public.api_feederdata
        set feeder_opened=true
        where feeder_opened=false """
        cursor.execute(postgres_insert_query)
        cursor.execute(query2)

        connection.commit()
        count = cursor.rowcount
        print(count, "Feeder opened  successfully...Feeds being released released")

    except (Exception, psycopg2.Error) as error:
        print("Failed to open feeder", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def terminate():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1000",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="feeder")
        cursor = connection.cursor()
        print("Connected...")

        postgres_insert_query = """ 
        update  public.api_feederdata
        set feeder_opened=FALSE
        """
        # query2 = """update  public.api_feederdata
        # set feeder_opened=FALSE
        # where feeder_opened=false """
        cursor.execute(postgres_insert_query)
        # cursor.execute(query2)


        connection.commit()
        count = cursor.rowcount
        print(count, "Feeder closed ...")


    except (Exception, psycopg2.Error) as error:
        print("Failed to open feeder", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


schedule.every().day.at("12:01").do(worker)
schedule.every().day.at("09:30").do(terminate)

schedule.every().day.at("17:00").do(worker)
schedule.every().day.at("17:30").do(terminate)

while True:
    schedule.run_pending()
    time.sleep(1)
    print("Worker/cron running")
