import re
ERRORS = []

from urllib.request import urlretrieve
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

print('Retrieving File')

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

print('File Succesfully Retrieved')

LOG_FILE = 'local_copy.log'

#for line in open(LOG_FILE):
	#print(line)
	
wait = input('PRESS ENTER TO CONTINUE.')

print('Pulling requests...')

wait = input('PRESS ENTER TO CONTINUE.')

fname = 'local_copy.log'
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print('Total number of requests is:', count)

wait = input('PRESS ENTER TO CONTINUE.')

#regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
#parts = regex.split('local_copy.log', line)
#print(parts)
#if not parts or len(parts) < 7:
 # print('Error parsing line! Log entry added to ERRORS[] list...')
 # ERRORS.append('local_copy.log')
  
#filecountdcn = {}
f#or line in open('local_copy.log'):
	 #pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)
	 #filenamelst = pieces[3]
	 #if filenamelst in filecountdcn:
		#filecountdcn[filenamelst] += 1
	# else:
		#filecountdcn[filenamelst] = 1
		
	
	
	