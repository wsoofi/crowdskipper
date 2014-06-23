
#def is_holiday(current_date):
#  holiday_list = ['2011-1-17','2011-2-21','2011-5-30','2011-7-4','2011-9-5','2011-10-10','2011-11-11','2011-11-24','2011-12-26','2012-1-2','2012-1-16','2012-2-20','2012-5-28', '2012-7-4','2012-9-3','2012-10-8','2012-11-12','2012-11-22','2012-12-25']
#  if current_date in holiday_list:
#    return 1
#  else:
#    return 0
    
    
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
                  '2020-12-25',
                  '2004-12-31', #ADD ZEROS
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
