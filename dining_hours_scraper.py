"""
We parse from raw html which ones are open and which ones are not.
 """
import subprocess
import json
from bs4 import BeautifulSoup
url="http://menu.dining.ucla.edu/Hours/"



def parseAllRawHTMLPages():
    '''Returns a JSON dictionary with following key value pair:
        {'Hallname':{'mealtime':{'open':{'hour':hour,'min':min}}}}
        Only gets mealtimes when they are open. '''
    hallTimes={}
    fullstring=subprocess.check_output(["curl",url])
    soup = BeautifulSoup(fullstring, 'html.parser')
    restos=soup.find('table','hours-table')\
                              .find('tbody')\
                              .find_all('tr')
    for resto in restos:
        #a resto object is what is enlcosed in each tr tag in the table.
        restoName=str(str(resto.find('a').get('href')).split('/')[2])
        #print restoName
        #openingtimes=[]
        mealTimeDict={'Breakfast':'none',\
                          'Lunch':'none',\
                          'Dinner':'none',\
                          'Late Night':'none',\
                          }

        for mealTime in ["hours-open "+ time for time in ['Breakfast',\
                                                                                    'Lunch',\
                                                                                    'Brunch',\
                                                                                    'Dinner',\
                                                                                    'Late Night']]:
            result=resto.find('td',mealTime)
            if result is not None:
                a,b=parseRawDate(str(result.find('span','hours-range').contents[0]))
                mealTimeDict[mealTime[11:]]={'open':{'hour':a[0],'min':a[1]},'close':{'hour':b[0],'min':b[1]}}
                #openingtimes.append([mealTime[11:],a,b])
                #print 'open at '+mealTime
            #else:
                #print 'closed at '+mealTime


        #hallTimes[restoName]=openingtimes
        hallTimes[restoName]=mealTimeDict
    f = open("dininghallTimes.json","w")
    f.write(json.dumps(hallTimes))
    f.close()
    #return json.dumps(hallTimes)

def parseRawDate(rawDateString):
    '''
    <span class="hours-range">9:30 am - 3:00 pm</span>

    Returns two arrays:  opening time and closing time.
    They have a format:
    [0] = hour [0,36] (>24 if the closing time is past midnight.)
    [1]= min [0,59]
    12 am midnight, 12 pm noon
    '''
    openingTime=[]
    openingAMPM=rawDateString.split(':')[1][3:5]
    openingHour=int(rawDateString.split(':')[0])
    if openingAMPM=='am':
        if openingHour == 12:#12 midnight

            openingTime.append(0)
        else:
            openingTime.append(openingHour)
    else:
        #print 'opening is pm'
        if openingHour ==12:#12 afternoon.
            openingTime.append(12)
        else:

            openingTime.append(openingHour+12)
    #-----MINUTES---------
    openingTime.append(int(rawDateString.split(':')[1][0:2]))


    closingTime=[]
    closingAMPM=rawDateString.split(':')[2][3:5]
    closingHour=int(rawDateString.split(':')[1][-1]) if str(rawDateString.split(':')[1][-2])==' ' else int(rawDateString.split(':')[1][-2:])
    if closingAMPM=='am':
        #print 'closing is am'
        if closingHour==12:
            closingTime.append(0)
        else:
            closingTime.append(closingHour)
    else:
        if closingHour==12:
            closingTime.append(12)
        else:
            closingTime.append(closingHour+12)
    #-------MINUTES
    closingTime.append(int(rawDateString.split(':')[2][0:2]))
    
    # ADDITION. for easy comparison of numbers, below is added:
    if closingAMPM=='am' and openingAMPM =='pm':
        if closingTime[0]==0:
            closingTime[0]=24
        else:
            closingTime[0]+=12

    return openingTime,closingTime


parseAllRawHTMLPages()
