# gen-SparkPost-Lists-python
This is a Python version of the [original PHP tool](https://github.com/tuck1s/gen-SparkPost-Lists-php).

Creates example, randomised Suppression and Recipient Lists for import into SparkPost (in .CSV format).

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
    domain = recipient domain to generate records for (default demo.sink.sparkpostmail.com)
```

## Example output
```bash
$ ./gen-sparkpost-lists.py recip 10
email,name,return_path,metadata,substitution_data,tags
anon35901572@demo.sink.sparkpostmail.com,Angela Rubin,bounce@demo.sink.sparkpostmail.com,"{""custID"": 27438690}","{""memberType"": ""platinum"", ""state"": ""ME""}",[]
anon03524931@demo.sink.sparkpostmail.com,Keisha Forehand,bounce@demo.sink.sparkpostmail.com,"{""custID"": 88667120}","{""memberType"": ""gold"", ""state"": ""PA""}","[""gwen"", ""bacon"", ""lamb hass"", ""hass"", ""reed"", ""pinkerton"", ""fuerte""]"
anon94961144@demo.sink.sparkpostmail.com,Ron Jenkins,bounce@demo.sink.sparkpostmail.com,"{""custID"": 35676181}","{""memberType"": ""bronze"", ""state"": ""MA""}","[""fuerte"", ""gwen"", ""bacon""]"
anon96298949@demo.sink.sparkpostmail.com,Diane Lucia,bounce@demo.sink.sparkpostmail.com,"{""custID"": 24033998}","{""memberType"": ""gold"", ""state"": ""VT""}","[""pinkerton"", ""gwen"", ""hass"", ""fuerte"", ""bacon"", ""lamb hass""]"
anon72308190@demo.sink.sparkpostmail.com,Jorge Dias,bounce@demo.sink.sparkpostmail.com,"{""custID"": 76123717}","{""memberType"": ""platinum"", ""state"": ""NH""}",[]
anon65280789@demo.sink.sparkpostmail.com,Chris Young,bounce@demo.sink.sparkpostmail.com,"{""custID"": 63789416}","{""memberType"": ""platinum"", ""state"": ""GU""}","[""fuerte"", ""gwen"", ""hass"", ""pinkerton"", ""lamb hass"", ""reed"", ""bacon""]"
anon79839806@demo.sink.sparkpostmail.com,Kurt Vonsoosten,bounce@demo.sink.sparkpostmail.com,"{""custID"": 91461763}","{""memberType"": ""silver"", ""state"": ""MS""}","[""gwen"", ""fuerte"", ""bacon"", ""hass""]"
anon66603972@demo.sink.sparkpostmail.com,Neal Preston,bounce@demo.sink.sparkpostmail.com,"{""custID"": 76760251}","{""memberType"": ""gold"", ""state"": ""MT""}","[""bacon"", ""fuerte"", ""reed"", ""pinkerton"", ""hass"", ""lamb hass"", ""gwen""]"
anon44156895@demo.sink.sparkpostmail.com,Edna Devers,bounce@demo.sink.sparkpostmail.com,"{""custID"": 81455813}","{""memberType"": ""platinum"", ""state"": ""AK""}","[""bacon"", ""gwen"", ""fuerte""]"
anon32881142@demo.sink.sparkpostmail.com,Carlos Lucia,bounce@demo.sink.sparkpostmail.com,"{""custID"": 19844619}","{""memberType"": ""bronze"", ""state"": ""SC""}","[""gwen"", ""hass"", ""fuerte"", ""bacon""]"
```

The email addresses 'anonxxx' are ensured unique, so that there are no repeats.

The human-readable names are selected using the 'names' package, described below (it makes use of real US census data).

Metadata, substitution data, and tags are randomised examples only:
- metadata is a randomised customer ID
- substitution_data contains a random memberType and random US postal-code / state
- tags contain zero or more avocado varieties

## Suppression List - updated format
The suppression list output now reflects current (Aug 2017) recommended SparkPost .csv format, with columns
`recipient,type,description`

Subaccount is no longer a column in the file - instead it's selected at import-time via the SparkPost UI.

## External dependencies

Project now includes a `Pipfile` for easier installation:

```
pip install pipenv
pipenv install
pipenv shell
./gen-sparkpost-lists.py
 ```

## Importing your lists
See the following support articles:

[Using Suppression Lists](https://support.sparkpost.com/customer/portal/articles/1929891)

[Uploading and Storing a Recipient List as a CSV file](https://support.sparkpost.com/customer/portal/articles/2351320)

## How do I modify user data, e.g. name, return_path, metadata, substitution_data, tags?
This is not command-line parameterized, but the code is meant to be easy to change and extend.