
import requests

api_key = 'AIzaSyDJMhAnLZvc7tvBVafjrcVt95sL6eG803Q'
destination_dict = dict()
path = "dests.txt"
file = open(path, 'r', encoding='utf-8')
file_read = file.read()
destination = file_read.split('\n')
origin_for_loop = "תל%אביב"
distances = list()

######## first loop to collect data into the dictionary 
for city in destination:
    
    if len(destination) != 5:
        print("Error : this program print values for exactly 5 cities",
        "you have entered",len(destination)," cities")
        break
    
    distance_url = "https://maps.googleapis.com/maps/api/distancematrix/json?/unit=imperial&origins=%s&destinations=%s&key=%s" % (
    origin_for_loop, city, api_key)
    distance_response = requests.get(distance_url).json()
    countries = distance_response["destination_addresses"]

    for country in countries:
        time = distance_response['rows'][0].get('elements')[0].get('duration').get('text')
        distance = distance_response["rows"][0].get('elements')[0]['distance']['text']
        distances.append(distance)
        city = country.split(",")[0]
        geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (
                city, api_key)
        geocode_response = requests.get(geocode_url).json()
        lat = geocode_response.get('results')[0].get('geometry')['location']['lat']
        lng = geocode_response.get('results')[0].get('geometry')['location']['lng']
        destination_dict[country] = distance, time, lng, 
#########


######### a loop in order to print the dictionary in a proper way
for key in destination_dict:
    print("Destination:",key)
    print("Distance:",destination_dict[key][0])
    print("Longitude:",destination_dict[key][1])
    print("Latitude:",destination_dict[key][2],"\n")
#########


######### a loop to find largest distances from origin      
first_biggest = 0
second_biggest = 0
third_biggest = 0
     
for distance in distances:
    
    thousands = int(distance[0])*1000
    hundreds = int(distance[2])*100
    tens = int(distance[3])*10
    ones = int(distance[4])
    number = thousands + hundreds + tens + ones
    if number > third_biggest:
        third_biggest = number 
        if third_biggest > second_biggest:
            third_biggest = second_biggest
            second_biggest = number
            if second_biggest > first_biggest:
                second_biggest = first_biggest
                first_biggest = number 
                
#########


######### a loop in order to print origin without %                
origin_fix = origin_for_loop.split("%")
origin=""
for word in origin_fix:
     origin = origin + " " + word    

if len(destination) == 5 :    
    print("the largest distance from",origin, " is:",first_biggest)
    print("the largest distance from",origin, " is:",second_biggest)
    print("the largest distance from",origin, " is:",third_biggest)
#########


file.close()
