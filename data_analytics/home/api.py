from rest_framework.views import APIView
from rest_framework.response import Response
import redis
import json
import ast 
import datetime
from operator import itemgetter



redis_db = redis.StrictRedis(host='localhost',port=6379, db=0,charset="utf-8", decode_responses=True)

class last100transaction(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        list_last100 = redis_db.lrange('last100',0,-1)
        last100transaction = []
        for i in list_last100:
            data = ast.literal_eval(i)
            last100transaction.append(data)
        return Response({"status":"success", "data": last100transaction})

class Transactions_count_per_minute(APIView):
    def get(self, request, min_value=None, format=None):
        print('data us ', min_value)
        if min_value > 60:
            return Response({"status":"failure", "data": "only last 60minutes data possible "})
        allkeys=redis_db.keys('*')
        allkeys_time_based =sorted(allkeys, reverse = True)
        allkeys_time_based.remove('last100')
        current_time = int(datetime.datetime.now().timestamp())
        previous_1time = datetime.datetime.now() - datetime.timedelta(hours=1)
        previous_1timestamp = int(previous_1time.timestamp())
        hourscount=[]
        time_redu1 = current_time - 60
        minute_value = 1
        count = 0

        for i in allkeys_time_based:
            data_time =i.split('-')[0]
            if str(time_redu1) <= data_time:
                count = count+1
            if str(time_redu1) > data_time:
                data = { 'minutes' :  minute_value, 'count' : count}
                hourscount.append(data)
                time_redu1 = time_redu1 - 60
                minute_value = minute_value +1
                count = 0
            if str(previous_1timestamp) > data_time:
                break
        response_data = hourscount[:min_value]
        return Response({"status":"success", "data": response_data})




class High_value_addr(APIView):
    def get(self, request, min_value=None, format=None):
        allkeys=redis_db.keys('*')
        allkeys.remove('last100')
        data = []
        try:
            for i in allkeys:
                trans_data=json.loads(redis_db.get(i))
                for j in trans_data['x']['out']:
                    if j['value'] != 0:
                        address = j['addr']
                        value = j['value']
                        data.append({'address': address, 'value': value}) 
                        break  
            print('length of data',len(data))            
        except Exception as e:
            print ('error',str(e))
        finally:
            data_response =  sorted([{'address': x.get('address'), 
                                'value': x.get('value')} for x in data], 
                                key = itemgetter('value'), 
                                reverse=True) 
        return Response({"status":"success", "data": data_response})
        

        