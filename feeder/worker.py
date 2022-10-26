import psycopg2
import time
import schedule


def worker():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="")
        cursor = connection.cursor()
        print("Connected...")

        postgres_insert_query = """ 
        update  public.feeder_feederdata
        set total_amount_of_feed=total_amount_of_feed-(number_of_chicken * feed_per_hen)
        where total_amount_of_feed>=(number_of_chicken * feed_per_hen)
        """
        query2 = """update  public.feeder_feederdata
        set feeder_opened=true
        where feeder_opened=false """
        cursor.execute(postgres_insert_query)
        cursor.execute(query2)
        query3 = """"
        select * where total_amount_of_feed <=300000
        """
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
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="")
        cursor = connection.cursor()
        print("Connected...")

        postgres_insert_query = """ 
        update  public.feeder_feederdata
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


def mail():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="")
        cursor = connection.cursor()
        print("Connected...")
        query3 = """"
            select * from public.feeder_feederdata 
            where total_amount_of_feed <=300000
            """
    finally:
        if query3:
            import smtplib, ssl
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "email"  # Enter your address
            receiver_email = ""  # Enter receiver address
            password = "password "
            message = """\
                Subject: Feeds Depleted
                
                Hello, the feeds are running low...kindly refill"""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            print("mail sent")


schedule.every().day.at("09:00").do(worker)
schedule.every().day.at("09:30").do(terminate)
schedule.every().day.at("08:00").do(mail)
schedule.every().day.at("17:00").do(worker)
schedule.every().day.at("17:30").do(terminate)

while True:
    schedule.run_pending()
    time.sleep(1)
    print("Worker/cron running")
