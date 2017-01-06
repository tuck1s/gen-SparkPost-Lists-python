#!/usr/bin/env python
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
# Author: Steve Tuck (January 2017)
#

from __future__ import print_function
import sys, os.path, csv, random, json

countDefault = 10;                                      # Default number of suppressions
domainDefault = "sedemo.sink.sparkpostmail.com";        # Safe default

def printHelp():
    progName = sys.argv[0];
    shortProgName = os.path.basename(progName);
    print("\nNAME")
    print("   " + progName)
    print("   Generate a random, SparkPost-compatible Recipient- or Suppression-List for .CSV import.\n")
    print("SYNOPSIS")
    print("  ./" + shortProgName + " recip|supp|help [count [domain]]\n")
    print("OPTIONAL PARAMETERS")
    print("    count = number of records to generate (default " + str(countDefault) + ")")
    print("    domain = recipient domain to generate records for (default " + domainDefault + ")")

# Need to treat ensureUnique only with mutating list methods, so the updated value is returned to the calling function
def randomRecip(domain, digits, ensureUnique):
    taken = True
    while taken:
        localpartnum = random.randrange(0, 10**digits)
        taken = localpartnum in ensureUnique            # If already had this number, then pick another one
    ensureUnique.add(localpartnum)
                                                        # Pad the number out to a fixed length of digits
    return "anon" + str(localpartnum).zfill(digits) + "@" + domain

def randomMeta():
    exampleMeta = {'foo': 'bar'}                        # Your metadata goes here
    return json.dumps(exampleMeta)

def randomSubData():
    # Your substitution data goes here
    exampleSubData = {'member': 'Platinum', 'region': 'US'}
    return json.dumps(exampleSubData)

def randomName():
    # Your readable name goes here
    return 'Fred Bloggs'

# -----------------------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------------------

count = countDefault
domain = domainDefault

# Check argument count
if len(sys.argv) >= 2:
    if sys.argv[1] == "supp":
        listType = "supp"
    elif sys.argv[1] == "recip":
        listType = "recip"
    else:
        printHelp()
        sys.exit(0)
else:
    printHelp()
    sys.exit(0)

# Check optional parameters
if len(sys.argv) >= 3:
        count = int(sys.argv[2])

if len(sys.argv) >= 4:
        domain = sys.argv[3]

# Mark numbers as we use them, to ensure uniqueness .. this does use a lot of memory.  set() more efficient than list
uniqFlags = set()
numDigits = 8                           # Number of random local-part digits to generate (max)

if count > 1000000:
    print("Too big for a single table")
    sys.exit(1)

if listType == "supp":
    headerRow = [
        "recipient",
        "transactional",
        "non_transactional",
        "description",
        "subaccount_id"
    ]
    fObj = csv.writer(sys.stdout)
    fObj.writerow(headerRow)

    # Generate the file on stdout
    for i in range(1, count):
        dataRow = []
        dataRow.append(randomRecip(domain, numDigits, uniqFlags))
        dataRow.append("true")                  # Transactional flag - Change this as needed
        dataRow.append("true")                  # Non-Transactional flag - Change this as needed
        dataRow.append("Example data import")
        dataRow.append("0")                     # 0 = Master account
        fObj.writerow(dataRow)

elif listType == "recip":
    headerRow = [
        "email",
        "name",
        "return_path",
        "metadata",
        "substitution_data",
        "tags"
    ]
    fObj = csv.writer(sys.stdout)
    fObj.writerow(headerRow)

    # Generate the file on stdout
    for i in range(1, count):
        dataRow = []
        dataRow.append(randomRecip(domain, numDigits, uniqFlags))
        dataRow.append(randomName())
        dataRow.append("bounce@" + domain)      # simple fixed value for testing
        dataRow.append(randomMeta())
        dataRow.append(randomSubData())
        dataRow.append("")                      # Tags not currently filled
        fObj.writerow(dataRow)
else:
    print("Invalid option - stopping.")