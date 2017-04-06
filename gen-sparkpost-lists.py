#!/usr/bin/env python3
#Generate random suppressions CSV file
#Copyright  2017 SparkPost

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#
# Author: Steve Tuck (Updated: April 2017)
#

# External dependencies: https://github.com/treyhunner/names

from __future__ import print_function
import sys, os.path, csv, random, json, names

countDefault = 10;                                      # Default length of list
domainDefault = 'sedemo.sink.sparkpostmail.com';        # Safe default

def printHelp():
    progName = sys.argv[0];
    shortProgName = os.path.basename(progName);
    print('\nNAME')
    print('   ' + progName)
    print('   Generate a random, SparkPost-compatible Recipient- or Suppression-List for .CSV import.\n')
    print('SYNOPSIS')
    print('  ./' + shortProgName + ' recip|supp|help [count [domain]]\n')
    print('OPTIONAL PARAMETERS')
    print('    count = number of records to generate (default ' + str(countDefault) + ')')
    print('    domain = recipient domain to generate records for (default ' + domainDefault + ')')

# Need to treat ensureUnique only with mutating list methods such as 'add', so the updated value is returned to the calling function
def randomRecip(domain, digits, ensureUnique):
    taken = True
    while taken:
        localpartnum = random.randrange(0, 10**digits)
        taken = localpartnum in ensureUnique                    # If already had this number, then pick another one
    ensureUnique.add(localpartnum)
    return 'anon'+str(localpartnum).zfill(digits)+'@'+domain    # Pad the number out to a fixed length of digits

def randomMeta(Tmax):
    exampleMeta = {'custID': random.randrange(Tmax)}    # Generate a pseudorandom customer ID, for example
    return json.dumps(exampleMeta)

def randomSubData():
    # US Postal code list
    states = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA',
              'KS', 'KY', 'LA', 'ME', 'MD', 'MH', 'MA', 'MI', 'FM', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
              'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA',
              'VI', 'WA', 'WV', 'WI', 'WY']
    tiers = ['bronze', 'silver', 'gold', 'platinum']
    exampleSubData = {
        'memberType': random.choice(tiers),
        'state': random.choice(states)}
    return json.dumps(exampleSubData)

def randomName(l):
    # Compose a real readable name from the two-part list given.  Randomise first and last names separately, giving more variety
    return random.choice(l)['first']+' '+random.choice(l)['last']

# -----------------------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------------------
count = countDefault
domain = domainDefault
# Mark numbers as we use them, to ensure uniqueness .. this does use a lot of memory.  set() more efficient than list
uniqFlags = set()
numDigits = 8                           # Number of random local-part digits to generate (max)
Tmax = 10**numDigits

# Check list-type and argument count
if len(sys.argv) < 2 or not(sys.argv[1] == 'supp' or sys.argv[1] == 'recip'):
    printHelp()
    exit(0)

# Check optional parameters
if len(sys.argv) >= 3:
        count = int(sys.argv[2])

if len(sys.argv) >= 4:
        domain = sys.argv[3]

if count > Tmax:
    print('Too big for a single table')
    exit(1)

if sys.argv[1] == 'supp':
    headerRow = ['recipient', 'transactional', 'non_transactional', 'description', 'subaccount_id']
    fObj = csv.writer(sys.stdout)
    fObj.writerow(headerRow)

    # Generate the file on stdout, as the user can always redirect it into a file when needed
    for i in range(1, count):
        dataRow = []
        dataRow.append(randomRecip(domain, numDigits, uniqFlags))
        dataRow.append('true')                  # Transactional flag - Change this as needed
        dataRow.append('true')                  # Non-Transactional flag - Change this as needed
        dataRow.append('Example data import')
        dataRow.append('0')                     # 0 = Master account
        fObj.writerow(dataRow)

elif sys.argv[1] == 'recip':
    headerRow = ['email', 'name', 'return_path', 'metadata', 'substitution_data', 'tags']
    fObj = csv.writer(sys.stdout)
    fObj.writerow(headerRow)

    # Prepare a cache of actual, random names - this enables long lists to be built faster
    nameList = []
    for i in range(100):
        nameList.append( { 'first': names.get_first_name(), 'last': names.get_last_name() } )

    # Generate the file on stdout
    for i in range(0, count):
        dataRow = []
        dataRow.append(randomRecip(domain, numDigits, uniqFlags))
        dataRow.append(randomName(nameList))
        dataRow.append('bounce@' + domain)      # simple fixed value for testing
        dataRow.append(randomMeta(Tmax))
        dataRow.append(randomSubData())
        dataRow.append('')                      # Tags not currently filled
        fObj.writerow(dataRow)
else:
    print("Invalid option - stopping.")