from flask import render_template, request
from app import app, host, port, user, passwd, db
from helpers.database import con_db
import pymysql
import cPickle as pickle

import datetime
import socket
import urllib2
import sys
import scipy
import numpy
import re
import datetime
import urllib
import time
import pandas


import json

# To create a database connection, add the following
# within your view functions:
flickr_response_re = r'jsonFlickrApi\((.*)\)'

# ROUTING/VIEW FUNCTIONS

MyGBR_Yosemite_Percentage    = pickle.load( open( "./app/helpers/GradientBoostingRegressor_Yosemite_Percentages_pickle3.p", "rb" ) )
MyGBR_SmokyMtn_Percentage    = pickle.load( open( "./app/helpers/GradientBoostingRegressor_SmokyMtn_Percentages_pickle3.p", "rb" ) )
MyGBR_GrandCanyon_Percentage = pickle.load( open( "./app/helpers/GradientBoostingRegressor_GrandCanyon_Percentages_pickle3.p","rb") )
MyGBR_Yellowstone_Percentage    = pickle.load( open( "./app/helpers/GradientBoostingRegressor_Yellowstone_Percentages_pickle3.p","rb") )
MyGBR_RockyMountains_Percentage = pickle.load( open( "./app/helpers/GradientBoostingRegressor_RockyMtns_Percentages_pickle3.p","rb") )


@app.route('/')
@app.route('/instructions')
def index():

    return render_template('instructions.html')

@app.route('/user_submit')
def UserSubmit():
    return render_template('index.html')


@app.route('/api/date_range/<location>/<min_date>/<max_date>/<holweekendonly>')
def dateRange(location,min_date, max_date,holweekendonly):
    print 'In dateRange'
    try:
      print host, port, user, db
      conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    except pymsyql.Error, e:
      return ('Could not connect to database: %s' % e), 500

    print location, min_date, max_date,holweekendonly
    
    minyear = int(min_date[0:4])
    maxyear = int(max_date[0:4])
    
    minmonth = int(min_date[5:7])
    maxmonth = int(max_date[5:7])
    
    minday = int(min_date[8:])
    maxday = int(max_date[8:])
    
    print minyear, maxyear
    print minmonth, maxmonth
    print minday, maxday


    min_date_for_temp = min_date.replace("-","")
    max_date_for_temp = max_date.replace("-","")
    
    min_date_for_temp = '2012'+ min_date_for_temp[4:]
    max_date_for_temp = '2012'+ max_date_for_temp[4:]

    print 'min date and max date for temp: '
    print min_date_for_temp, max_date_for_temp

    cur = conn.cursor()
    
   
    chosen_months = []
    predicted_temps = []
    chosen_days = []
    chosen_years = []
    daysofyear = [] #NEWPICKLE
    daysofweek = []  #NEWPICKLE
    weekendflags = []
    res = []
    
    start_date = datetime.datetime.strptime(min_date,"%Y-%m-%d")
    end_date = datetime.datetime.strptime(max_date,"%Y-%m-%d")
    
    d = start_date
    delta = datetime.timedelta(days=1)
    while  d <=end_date:
        current_date= d.strftime("%Y%m%d")
        d_str = '2012'+current_date[4:]

        print 'SELECT * FROM all_temperature_averages WHERE park_id = "{0}" AND date = {1}'.format(location, d_str)
        # Location is provided directly by the user, so escape it.
        location_escaped = conn.escape(location)
        cur.execute(
            'SELECT * FROM all_temperature_averages WHERE park_id = {0} AND date = {1}'.
            format(location_escaped, d_str))
        print 'Query successfully executed'
        cur_res = cur.fetchone()
        res.append(cur_res)

        d +=delta
        
        #print res[idx][1]
        T = cur_res[4]
        M = cur_res[2]
        D = cur_res[3]
        Y = int(current_date[0:4])
      
        #print chosen_years,chosen_months, chosen_days

        dayofyear = int(datetime.datetime.strptime(str(Y)+str(M).zfill(2)+str(D).zfill(2),'%Y%m%d').strftime("%j")) #NEWPICKLE
        print dayofyear #NEWPICKLE

        dayofweek = datetime.date(Y,M,D).weekday()
        print dayofweek

        if dayofweek == 5 or dayofweek == 6:
          weekendflags.append(1)
        elif is_holiday(str(Y)+'-'+str(M)+'-'+str(D)):
          weekendflags.append(1)
        else:
          weekendflags.append(0)

        predicted_temps.append(T)
        chosen_months.append(M)
        chosen_days.append(D)
        chosen_years.append(Y)
        daysofyear.append(dayofyear) #NEWPICKLE
        daysofweek.append(dayofweek) #NEWPICKLE


    cur.close()
    conn.close()


    print chosen_months, daysofweek,predicted_temps, daysofyear, weekendflags
    #dates = zip(chosen_years, chosen_months, chosen_days)
    strdate=[]
    print len(chosen_years)
    for date in range(0,len(chosen_years)):
      strdate.append(str(chosen_years[date]) + '-' + str(chosen_months[date]).zfill(2)+'-'+ str(chosen_days[date]).zfill(2))

    #predictors = zip(chosen_months, daysofweek, daysofyear,predicted_temps,weekendflags) #NEWPICKLE
    predictors = zip(daysofweek, daysofyear,predicted_temps,weekendflags) #NEWPICKLE


    print predictors
    
    #below won't work if you roll over from one year to the next. can only fix with replacement for date range.
    if location == 'Yosemite_National_Park':
      predicted_crowds = MyGBR_Yosemite_Percentage.predict(predictors)
    elif location == 'Great_Smoky_Mountains':
      predicted_crowds = MyGBR_SmokyMtn_Percentage.predict(predictors) 
    elif location == 'Grand_Canyon':
      predicted_crowds = MyGBR_GrandCanyon_Percentage.predict(predictors) 
    elif location == 'Yellowstone':
      predicted_crowds = MyGBR_Yellowstone_Percentage.predict(predictors) 
    elif location == 'Rocky_Mountains':
      predicted_crowds = MyGBR_RockyMountains_Percentage.predict(predictors)
    
    candidates = []
    
    print 'test zip'
    date_predictors_crowds = zip(strdate,predictors,predicted_crowds)
    print date_predictors_crowds
    print date_predictors_crowds[0][0] # first and only output
    print date_predictors_crowds[0][0][1] # second input
    
    if holweekendonly == 'true':
      for idx in range(0, len(predictors)):  #now find recommended dates
#        if date_predictors_crowds[idx][1][2]==1:
        if date_predictors_crowds[idx][1][3]==1:

          candidates.append(date_predictors_crowds[idx])
    else:
      candidates = date_predictors_crowds
      
    print candidates
    
    sortedcandidates = sorted(candidates,key=lambda tup: tup[2])
    print ' sorted candidates RIGHT HERE FINAL'
    print sortedcandidates
    bestdate = sortedcandidates[0][0]
    print 'this is the best date'
    print bestdate
    
    bestdate_outputformat = datetime.datetime.strptime(bestdate,"%Y-%m-%d").strftime("%A, %B %d")
    print bestdate_outputformat
    
    photo_urls = get_photos(location,bestdate)
    
    plotdata=[['Date', 'Crowd size']];
    for index in range(0,len(chosen_years)):
      plotdata.append([strdate[index], predicted_crowds[index]])
    print plotdata
    
    returnObject = {
        'visData': plotdata,
        'bestDate': bestdate_outputformat,
        'photoURLs': photo_urls
    }

    return json.dumps(returnObject)

def FarmPhotoURL_(photo):
  return 'https://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg'.format(
      photo['farm'], photo['server'], photo['id'], photo['secret'])

def FlickrPhotoURL_(photo):
  return 'https://www.flickr.com/photos/{0}/{1}'.format(photo['owner'], photo['id'])


def get_photos(location,bestdate):
    key = '7f32d1881e9c8a7feee262c4e85686af'


    timeout = 10
    socket.setdefaulttimeout(timeout)
  
    start_time = '00:00:00'
    end_time = '23:59:59'
    init_photo_date = (datetime.datetime.strptime(bestdate,'%Y-%m-%d') -
        datetime.timedelta(days=380))
    end_photo_date = (datetime.datetime.strptime(bestdate,'%Y-%m-%d') -
        datetime.timedelta(days=350))
    init_photo_date = init_photo_date.strftime('%Y-%m-%d')
    end_photo_date = end_photo_date.strftime('%Y-%m-%d')

    current_startdatetime = str(init_photo_date)+' '+ start_time
    current_enddatetime = str(end_photo_date)+' '+ end_time

    if location == 'Yosemite_National_Park':
        latitude = 37.8399951
        longitude = -119.5409561
        radius = 31
    elif location == 'Great_Smoky_Mountains':
        latitude = 35.566538
        longitude = -83.6419481
        radius = 31
    elif location == 'Grand_Canyon':
        latitude = 36.106965
        longitude = -112.112997
        radius = 31
    elif location == 'Yellowstone':
        latitude = 37.8399951
        longitude = -119.5409561
        radius = 31
    elif location == 'Rocky_Mountains':
        latitude = 40.342793
        longitude = -105.683639
        radius = 31


    params = {
            'method': 'flickr.photos.search',
            'min_taken_date': current_startdatetime,
            'max_taken_date': current_enddatetime,
            'has_geo': 1,
            'lat': latitude,
            'lon': longitude,
            'radius': radius,
            'per_page': 3,
            'format': 'json',
            'extras': 'date_taken',
            'api_key': key,
            'license':'1,2,3,4,5,6,7,8'
          }
          

    print params
    flickr_data = urllib2.urlopen(
        'https://api.flickr.com/services/rest/?%s'%
        urllib.urlencode(params)).read()
    flickr_output = ParseOutput(flickr_data)
    import pprint; pprint.pprint(flickr_output)
    
    allurls = [{
        'static': FarmPhotoURL_(photo),
        'flickr': FlickrPhotoURL_(photo)
    } for photo in flickr_output['photos']['photo']]
    print allurls

    return allurls

    
    
def ParseOutput(flickr_response):
    return json.loads(re.match(flickr_response_re,flickr_response).group(1))
    

    
def is_holiday(current_date):
  holiday_list = ['2004-12-31',
                  '2005-1-17',
                  '2005-2-21',
                  '2005-5-30',
                  '2005-7-4',
                  '2005-9-5',
                  '2005-10-10',
                  '2005-11-11',
                  '2005-11-24',
                  '2005-12-26',
                  '2006-1-2',
                  '2006-1-16',
                  '2006-2-20',
                  '2006-5-29',
                  '2006-7-4',
                  '2006-9-4',
                  '2006-10-9',
                  '2006-11-10',
                  '2006-11-23',
                  '2006-12-25',
                  '2007-1-1',
                  '2007-1-15',
                  '2007-2-19',
                  '2007-5-28',
                  '2007-7-4',
                  '2007-9-3',
                  '2007-10-8',
                  '2007-11-12',
                  '2007-11-22',
                  '2007-12-25',
                  '2008-1-1',
                  '2008-1-21',
                  '2008-2-18',
                  '2008-5-26',
                  '2008-7-4',
                  '2008-9-1',
                  '2008-10-13',
                  '2008-11-11',
                  '2008-11-27',
                  '2008-12-25',
                  '2009-1-1',
                  '2009-1-19',
                  '2009-2-16',
                  '2009-5-25',
                  '2009-7-3',
                  '2009-9-7',
                  '2009-10-12',
                  '2009-11-11',
                  '2009-11-26',
                  '2009-12-25',
                  '2010-1-1',
                  '2010-1-18',
                  '2010-2-15',
                  '2010-5-31',
                  '2010-7-5',
                  '2010-9-6',
                  '2010-10-11',
                  '2010-11-11',
                  '2010-11-25',
                  '2010-12-24',
                  '2010-12-31',
                  '2011-1-17',
                  '2011-2-21',
                  '2011-5-30',
                  '2011-7-4',
                  '2011-9-5',
                  '2011-10-10',
                  '2011-11-11',
                  '2011-11-24',
                  '2011-12-26',
                  '2012-1-2',
                  '2012-1-16',
                  '2012-2-20',
                  '2012-5-28',
                  '2012-7-4',
                  '2012-9-3',
                  '2012-10-8',
                  '2012-11-12',
                  '2012-11-22',
                  '2012-12-25',
                  '2013-1-1',
                  '2013-1-21',
                  '2013-2-18',
                  '2013-5-27',
                  '2013-7-4',
                  '2013-9-2',
                  '2013-10-14',
                  '2013-11-11',
                  '2013-11-28',
                  '2013-12-25',
                  '2014-1-1',
                  '2014-1-20',
                  '2014-2-17',
                  '2014-5-26',
                  '2014-7-4',
                  '2014-9-1',
                  '2014-10-13',
                  '2014-11-11',
                  '2014-11-27',
                  '2014-12-25',
                  '2015-1-1',
                  '2015-1-19',
                  '2015-2-16',
                  '2015-5-25',
                  '2015-7-3',
                  '2015-9-7',
                  '2015-10-12',
                  '2015-11-11',
                  '2015-11-26',
                  '2015-12-25',
                  '2016-1-1',
                  '2016-1-18',
                  '2016-2-15',
                  '2016-5-30',
                  '2016-7-4',
                  '2016-9-5',
                  '2016-10-10',
                  '2016-11-11',
                  '2016-11-24',
                  '2016-12-26',
                  '2017-1-2',
                  '2017-1-16',
                  '2017-2-20',
                  '2017-5-29',
                  '2017-7-4',
                  '2017-9-4',
                  '2017-11-10',
                  '2017-11-23',
                  '2017-12-25',
                  '2018-1-1',
                  '2018-1-15',
                  '2018-2-19',
                  '2018-5-28',
                  '2018-7-4',
                  '2018-9-3',
                  '2018-10-8',
                  '2018-11-12',
                  '2018-11-22',
                  '2018-12-25',
                  '2019-1-1',
                  '2019-1-21',
                  '2019-2-18',
                  '2019-5-27',
                  '2019-7-4',
                  '2019-9-2',
                  '2019-10-14',
                  '2019-11-11',
                  '2019-11-28',
                  '2019-12-25',
                  '2020-1-1',
                  '2020-1-20',
                  '2020-2-17',
                  '2020-5-25',
                  '2020-7-3',
                  '2020-9-7',
                  '2020-10-12',
                  '2020-11-11',
                  '2020-11-26',
                  '2020-12-25']
  if current_date in holiday_list:
    return 1
  else:
    return 0


@app.route('/api/users/<year>/<month>/<day>')  #nick
def users(year,month,day):
    print year, month, day
    makedatestring = str(2013)+str(month).zfill(2)+str(day).zfill(2)
    print makedatestring


@app.route('/api/out') #nick
def users_test():
    return render_template('users_test.html')

@app.route('/home')
def home():
    # Renders home.html.
    return render_template('home.html')
    
@app.route('/indexbs')
def indexbs():
    # Renders indexbs.html.
    return render_template('indexbs.html')

@app.route('/slides')
def about():
    # Renders slides.html.
    return render_template('slides.html')

@app.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
