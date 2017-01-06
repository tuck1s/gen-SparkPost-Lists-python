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
```
./gen-sparkpost-lists.py recip 10
email,name,return_path,metadata,substitution_data,tags
anon93115417@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon77717755@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon19892920@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon65699942@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon87920342@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon28301908@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon60377150@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon98606741@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
anon58551008@sedemo.sink.sparkpostmail.com,Fred Bloggs,bounce@sedemo.sink.sparkpostmail.com,"{""foo"": ""bar""}","{""member"": ""Platinum"", ""region"": ""US""}",
```

##Importing your lists
See the following support articles:

[Using Suppression Lists](https://support.sparkpost.com/customer/portal/articles/1929891)

[Uploading and Storing a Recipient List as a CSV file](https://support.sparkpost.com/customer/portal/articles/2351320)

##How do I modify user data, e.g. name, return_path, metadata, substitution_data, tags?
This is not command-line parameterized, but the code is meant to be easy to change and extend.
