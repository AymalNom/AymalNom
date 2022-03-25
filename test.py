from aiohttp import ServerTimeoutError
import requests
from sanic import json

# API TO get Cities
# url='https://auth.feedni.net/settings?type=Cities&app=seekers'
# json_data=requests.get(url).json()
# length=len(json_data['data']['options'])
# ask_city= "In which city would like to avail the Services?"
# total=""
# for city in range(1,length):
#     cities_list= str(city) + ". "+json_data['data']['options'][city]['name']+ "\n"
#     total+=cities_list
# print(ask_city+"\n"+total)

#API TO Get Services
url="""https://api-bas.feedni.net/services?filters[]={"field":"app","value":"seekers","condition":"e"}&filters[]={"field":"isPublished","value":true,"condition":"e"}&filters[]={"field":"type","value":"cat","condition":"e"}&city=&for=firstpage&type=cat&projection[]={"field":"_id","value":1}&projection[]={"field":"label","value":1}&projection[]={"field":"friendlyName","value":1}"""
json_data=requests.get(url).json()
length=len(json_data['data'])
print(json_data)
for service in range(0,length):
    print(json_data['data'][service]['friendlyName'])

# url="""https://api-bas.feedni.net/services??hide_empty_category=false&filters[]=%7B%22field%22:%22app%22,%22value%22:%22seekers%22,%22condition%22:%22like%22%7D&filters[]=%7B%22field%22:%22isPublished%22,%22value%22:true,%22condition%22:%22e%22%7D&filters[]=%7B%22field%22:%22type%22,%22value%22:%22subcat%22,%22condition%22:%22e%22%7D&filters[]=%7B%22field%22:%22cat._id%22,%22value%22:%22612fc12cd317d10ac62027c7%22,%22condition%22:%22e%22%7D&sort[]=%7B%22field%22:%22label%22,%22order%22:%22asc%22%7D&city=Ras Al-Khaimah&for=firstpage&type=subcat&projection[]=%7B%22field%22:%22_id%22,%22value%22:1%7D&projection[]=%7B%22field%22:%22label%22,%22value%22:1%7D&projection[]=%7B%22field%22:%22friendlyName%22,%22value%22:1%7D"""
# json_data=requests.get(url).json()
# print(json_data)