import dateutil.parser
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
			bucket.append(glucose)
def agp(bucket):
	vals_sorted = sorted(bucket)
	#print vals_sorted
	percentile_10 = vals_sorted[int(len(vals_sorted)*.1)]
	median = vals_sorted[int(len(vals_sorted)/2)]
	percentile_25 = vals_sorted[int(len(vals_sorted)*.25)]
	percentile_75 = vals_sorted[int(len(vals_sorted)*.75)]
	percentile_90 = vals_sorted[int(len(vals_sorted)*.9)]
	return (percentile_10, percentile_25, median, percentile_75, percentile_90)

for hour in range(0,24):
	print hour, agp(hour_buckets[hour])
