def get_file_lines(filename):
	f = open(filename)
	result = f.readlines()[:]
	f.close()
	return result
cpuinfo = get_file_lines('/proc/cpuinfo')
meminfo = get_file_lines('/proc/meminfo')

cpunumber = -1
cpus = []

for line in cpuinfo:
	if line.startswith('processor'):
		cpus.append({})
		cpunumber+=1
	elif line.startswith('vendor_id'):
		 cpus[cpunumber]['vendor'] = line.split(':')[1].strip()
	elif line.startswith('cpu MHz'):
		cpus[cpunumber]['clock'] = line.split(':')[1].strip()
	elif line.startswith('cache size'):
		cpus[cpunumber]['cache'] = line.split(':')[1].strip()	
	elif line.startswith('model name'):
		cpus[cpunumber]['model'] = line.split(':')[1].strip()	
			
totalmemory = ''
memfree = ''
for line in meminfo:
	if line.startswith('MemTotal'):
		totalmemory = line.split(':')[1].strip()
	if line.startswith('MemFree'):
		memfree = line.split(':')[1].strip()

print("Number of processors:", len(cpus))
for i,cpu in enumerate(cpus):
	print("Processor",i)
	print("Model",cpu['model'])
	print("Vendor:", cpu["vendor"])
	print("CPU clock speed:", cpu["clock"])
	print("CPU cache size", cpu["cache"])
	print("-"*60)

print("="*60)
print("Total installed memory:", totalmemory)
print("Free memory:", memfree)
