"""
AGP - calculate agp values given some glucose text
"""

import dateutil.parser
from scipy import stats
from scipy.stats import norm
from numpy import percentile
import math

class AGP (object):
  """
  The actual calculator.
  """

  def __init__ (self, json=False):
    # init empty values
    self.json = json
    self.values = []
    # and empty buckets
    self.hour_buckets = {}
    # initialize all buckets with empty list
    for hour in range(0,24):
      self.hour_buckets[hour] = []

  def check (self, record):
    if self.json:
      return (record.get('display_time'), record.get('glucose'), record.get('trend_arrow'))
    return record.strip().split()
  def add_record (self, record):
    """ Add record to global list and assign to bucket
    """
    # clean/prep the record
    (time, glucose, trend) = self.check(record)
    # get a proper datetime object
    datetime = dateutil.parser.parse(time)
    glucose = int(glucose)
    # ignore special values < 40
    if (glucose >= 39):
      # print datetime.hour, glucose, trend
      # append to internal list
      self.values.append((datetime, glucose, trend))
      # assign to bucket
      bucket = self.hour_buckets.get(datetime.hour, [])
      bucket.append((datetime, glucose))

  # process data and return new agp stats
  def __call__ (self, data):
    out = [ ]
    # add all records
    for record in data:
      self.add_record(record)

    # calculate for out each hour of day

    for hour in range(0,24):
      agps = calc_agp(self.hour_buckets[hour])
      for minute in range(0,60,5):
        out.append((hour, minute, agps[minute/5]))
    return out

def calc_agp (bucket):
  subbuckets = [[] for x in range(0,60,5)]
  for (time, glucose) in bucket:
    subbuckets[int(math.floor(time.minute / 5))].append(glucose)
  agps = [percentile(subbucket, [10,25,50,75,90]) for subbucket in subbuckets]
  return agps



# The remainder is for debugging and testing purposes.
# This allows running the module from commandline without openaps.
# this uses no openaps logic, and is useful for debugging/testing
# this only runs when run as:
# $ python agp.py
if __name__ == '__main__':
  parser = AGP( )
  with open("glucose.txt") as f:
    for hour, minute, vals in parser(f.readlines()):
      print hour, minute, vals

