import json

clubs_data = [
    {
        "name": "Shoko",
        "lat": 41.38556,
        "lng": 2.19691,
        "schedule": {
            "Monday": {
              "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "red", "0:30" : "red", "1:00" : "red","1:30" : "red", "2:00" : "red", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange","0:30" : "orange", "1:00" : "red","1:30" : "red", "2:00" : "red", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "green", "5:00" :"green"
            },
            "Wednesday": {
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "orange", "1:00" : "orange","1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "orange", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Thursday": {
              "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "orange", "1:00" : "red","1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Friday": {
              "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "yellow", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "orange", "0:30" : "orange", "1:00" : "red","1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Saturday":{
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "yellow", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "orange", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
               "12:00": "green", "13:00" : "green", "14:00" : "yellow", "15:00" : "yellow", "16:00" : "yellow", "17:00" : "yellow", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow","1:30" : "orange", "2:00" : "orange", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "green", "04:00": "green", "5:00" :"green"
            }
        }
    },
    {"name": "Opium",
        "lat": 41.38537,
        "lng": 2.19676,
        "schedule": {
            "Monday": {
                "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange", "0:30" : "orange", "1:00" : "orange", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "orange", "3:30" : "orange", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
                "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "green", "23:00" : "green", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "orange", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Wednesday": {
              "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "green", "23:00" : "green", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "yellow", "2:30" : "orange", "3:00" : "yellow", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Thursday": {
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "green", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "orange", "3:00" : "yellow", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Friday": {
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "yellow", "23:00" : "yellow", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Saturday":{
               "12:00": "green", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
               "12:00": "green", "13:00" : "green", "14:00" : "yellow", "15:00" : "yellow", "16:00" : "yellow", "17:00" : "yellow", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "red", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            }
        }
    },
    {"name": "Pacha",
        "lat": 41.385740931557,
        "lng": 2.1970712632294,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "orange", "3:30" : "orange", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "orange", "3:00" : "orange", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Wednesday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Thursday": {
              "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Friday": {
              "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "red", "5:00" :"green"
            },
            "Saturday":{
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "red", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30": "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "red", "5:00" :"green"
            },
            "Sunday": {
              "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "red", "0:00" : "red", "0:30" : "red", "1:00" : "red", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "orange", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            }
        }
    },
    {"name": "Twenties",
        "lat": 41.39346,
        "lng": 2.15801,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "orange", "3:00" : "yellow", "3:30" : "green", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "green", "04:00": "green", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "orange", "2:30" : "orange", "3:00" : "red", "3:30" : "red", "04:00": "yellow", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "yellow", "0:30": "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "orange", "2:30" : "orange", "3:00" : "yellow", "2:30": "yellow", "04:00": "yellow", "5:00" :"green"
            }
        }
    },
    {"name": "Sutton",
        "lat": 41.39596,
        "lng": 2.15174,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "yellow", "3:00" : "green", "3:30" :"green", "04:00": "green", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "yellow", "1:00" : "orange", "1:30" : "orange", "2:00" : "orange", "2:30" : "orange", "3:00" : "orange", "3:30" : "yellow", "04:00": "yellow", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            }
        }
    },
    {"name": "Downtown",
        "lat": 41.38142,
        "lng": 2.11457,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "green", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "orange", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "green", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "orange", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "yellow", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "yellow", "0:00" : "red", "0:30" : "orange", "1:00" : "orange", "1:30" : "red", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            }
        }
    },
    {"name": "Razzmatazz",
        "lat": 41.39778,
        "lng": 2.19118,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "orange", "1:30" : "orange", "2:00" : "red", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "red", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "red", "04:00": "red", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "orange", "2:00" : "orange", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black","0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            }
        }
    },
    {"name": "Jamboree",
        "lat": 41.37971,
        "lng": 2.17528,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "green", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "yellow", "04:00": "yellow", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "red", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "red", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green","0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "yellow", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            }
        }
    },
    {"name": "Sala Apolo",
        "lat": 41.37439,
        "lng": 2.16956,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "green", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "green", "04:00": "green", "5:00" :"green"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "green", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "yellow", "04:00": "yellow", "5:00" :"green"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "yellow", "2:30" : "yellow", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "yellow", "2:30" : "yellow", "3:00" : "orange", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "orange", "2:30" : "orange", "3:00" : "red", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green","0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "green", "2:30" : "yellow", "3:00" : "yellow", "3:30" : "yellow", "04:00": "green", "5:00" :"green"
            }
        }
    },
    {"name": "Bling Bling",
        "lat": 41.39475,
        "lng": 2.15192,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "orange", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "yellow", "5:00" :"green"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "yellow", "2:30" : "orange", "3:00" : "orange", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Friday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "yellow", "2:00" : "orange", "2:30" : "red", "3:00" : "orange", "3:30" : "orange", "04:00": "orange", "5:00" :"green"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "green", "0:30" : "green", "1:00" : "green", "1:30" : "green", "2:00" : "yellow", "2:30" : "orange", "3:00" : "red", "3:30" : "red", "04:00": "orange", "5:00" :"green"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "black", "14:00" : "black", "15:00" : "black", "16:00" : "black", "17:00" : "black", "18:00" : "black", "19:00" : "black", "20:00" : "black", "21:00" : "black", "22:00" : "black", "23:00" : "black", "0:00" : "black", "0:30" : "black", "1:00" : "black", "1:30" : "black", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black" 
            }
        }
    },
    {"name": "George Payne",
        "lat": 41.38700,
        "lng": 2.16983,
        "schedule": {
            "Monday": {
               "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange", "0:30" : "orange", "1:00" : "yellow", "1:30" : "green", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Tuesday": {
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange", "0:30" : "yellow", "1:00" : "yellow", "1:30" : "green", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Wednesday": {
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "green", "1:30" : "green", "2:00" : "black", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Thursday": {
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange", "0:30" : "orange", "1:00" : "yellow", "1:30" : "yellow", "2:00" : "green", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Friday": {
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "orange", "23:00" : "orange", "0:00" : "orange", "0:30" : "orange", "1:00" : "yellow", "1:30" : "green", "2:00" : "green", "2:30" : "green", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Saturday":{
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "yellow", "21:00" : "yellow", "22:00" : "yellow", "23:00" : "orange", "0:00" : "orange", "0:30" : "orange", "1:00" : "orange", "1:30" : "orange", "2:00" : "yellow", "2:30" : "yellow", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black"
            },
            "Sunday": {
                "12:00": "black", "13:00" : "green", "14:00" : "green", "15:00" : "green", "16:00" : "green", "17:00" : "green", "18:00" : "green", "19:00" : "green", "20:00" : "green", "21:00" : "green", "22:00" : "green", "23:00" : "yellow", "0:00" : "yellow", "0:30" : "yellow", "1:00" : "green", "1:30" : "green", "2:00" : "green", "2:30" : "black", "3:00" : "black", "3:30" : "black", "04:00": "black", "5:00" :"black" 
            }
        }
    },
]

# Save the file
with open("clubs_data.json", "w", encoding="utf-8") as f:
    json.dump(clubs_data, f, indent=2)

print("✅ clubs_data.json created successfully!")
