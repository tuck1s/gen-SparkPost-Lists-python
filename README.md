# gen-SparkPost-Lists-python
This is a Python version of the [original PHP tool](https://github.com/tuck1s/gen-SparkPost-Lists-php).

Simple command-line tool to create example, randomised Suppression and Recipient Lists for import into SparkPost (in .CSV format).

This is useful for any testing that requires lists of specified size, as the email-address uniqueness is checked and enforced.
Redirect output to a file with >myfile.csv, then upload the file using the SparkPost web user interface.

## Usage
```
NAME
   ./gen-sparkpost-lists.py
   Generate a random, SparkPost-compatible Recipient- or Suppression-List for .CSV import.

SYNOPSIS
  ./gen-sparkpost-lists.py recip|supp|help [count [domain]]

OPTIONAL PARAMETERS
    count = number of records to generate (default 10)
    domain = recipient domain to generate records for (default sedemo.sink.sparkpostmail.com)
```

##Example output
```bash
$ ./gen-sparkpost-lists.py recip 10
email,name,return_path,metadata,substitution_data,tags
anon65068068@sedemo.sink.sparkpostmail.com,William Williams,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 90153123}","{""memberType"": ""bronze"", ""state"": ""DE""}",
anon00645960@sedemo.sink.sparkpostmail.com,Aracely Gibson,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 16448501}","{""memberType"": ""silver"", ""state"": ""OK""}",
anon89927931@sedemo.sink.sparkpostmail.com,Angela Monroe,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 12142912}","{""memberType"": ""gold"", ""state"": ""MD""}",
anon17910948@sedemo.sink.sparkpostmail.com,Richard Leber,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 77532118}","{""memberType"": ""bronze"", ""state"": ""TX""}",
anon49708069@sedemo.sink.sparkpostmail.com,Joyce Morrison,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 47869024}","{""memberType"": ""gold"", ""state"": ""GA""}",
anon49376624@sedemo.sink.sparkpostmail.com,Jaime Whitley,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 83300287}","{""memberType"": ""gold"", ""state"": ""NM""}",
anon48442130@sedemo.sink.sparkpostmail.com,Richard Jones,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 98224223}","{""memberType"": ""platinum"", ""state"": ""TN""}",
anon85110754@sedemo.sink.sparkpostmail.com,Diana Fulkerson,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 24351711}","{""memberType"": ""bronze"", ""state"": ""CA""}",
anon63355536@sedemo.sink.sparkpostmail.com,Christopher Nichols,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 59126359}","{""memberType"": ""gold"", ""state"": ""AZ""}",
anon65786481@sedemo.sink.sparkpostmail.com,Alicia Camacho,bounce@sedemo.sink.sparkpostmail.com,"{""custID"": 98630101}","{""memberType"": ""platinum"", ""state"": ""IL""}",
stevet-macbook-air:gen-sparkpost-lists stuck$ 
```

The email addresses 'anonxxx' are checked for uniqueness, to avoid repeats.
The human-readable names are selected using the 'names' package, described below (it makes use of real US census data).
Metadata and substitution data are randomised examples only.

## External dependencies
https://github.com/treyhunner/names

## Importing your lists
See the following support articles:

[Using Suppression Lists](https://support.sparkpost.com/customer/portal/articles/1929891)

[Uploading and Storing a Recipient List as a CSV file](https://support.sparkpost.com/customer/portal/articles/2351320)

## How do I modify user data, e.g. name, return_path, metadata, substitution_data, tags?
This is not command-line parameterized, but the code is meant to be easy to change and extend.