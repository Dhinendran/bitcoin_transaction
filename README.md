Python version 3.6
1.Install Requirements.txt 
    commands: pip3 install -r requirements.txt
2.Install Kafka refer link : https://kafka.apache.org/quickstart
3.Install Redis
4.Run kafkapro.py 
    commands : python3.6 kafkapro.py
5.Run kafkacons.py
    commands : python3.6 kafkacons.py
6.Run Django Framework 
    commands : 1.cd data_analytics
               2.python3.6 manage.py runserver


open the link after server starts http://127.0.0.1:8000/

7.open http://127.0.0.1:8000/show_transactions/ 
    Display latest 100 transactions
8.http://127.0.0.1:8000/transactions_count_per_minute/{min_value}
    Display number of transactions per minute for the last hour
    1.min_value should be number
    2.if min_value = 10, it display number of transactions per minute for the 10minutes
    3.if min_value > 60, it display the error
9.http://127.0.0.1:8000/high_value_addr
    Display the bitcoin addresses which has the most aggregate value in transactions in the last 3 hours.
    It display the last 3 hours transaction and descending order of out addr value



