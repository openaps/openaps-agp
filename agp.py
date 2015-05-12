import dateutil.parser
from scipy import stats
from scipy.stats import norm
from numpy import percentile
import math

values = []
hour_buckets = {}
for hour in range(0,24):
	hour_buckets[hour] = []
with open("glucose.txt") as f:
	lines = f.readlines()
	for line in lines:
		(time, glucose, trend) = line.strip().split()
		datetime = dateutil.parser.parse(time)
		glucose = int(glucose)
		if (glucose >= 39):
			values.append((datetime, glucose, trend))
			bucket = hour_buckets.get(datetime.hour, [])
			bucket.append((datetime, glucose))

def agp(bucket):
	subbuckets = [[] for x in range(0,60,5)]
	for (time, glucose) in bucket:
		subbuckets[int(math.floor(time.minute / 5))].append(glucose)
	agps = [percentile(subbucket, [10,25,50,75,90]) for subbucket in subbuckets]
	return agps

for hour in range(0,24):
	agps = agp(hour_buckets[hour])
	for minute in range(0,60,5):
		print hour, minute, agps[minute/5]
		
