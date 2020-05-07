# Wikipedia Pageviews Count

**Wikipedia Pageviews Count** is an application that ingests wikipedia pagevisits raw data and determines the total count of visits
to wiki pages containing a certain keyword.
 
Both the ingestion and the pageview aggregator jobs are developed to run concurrently using the `concurrent.futures module` in python

## Installation

This section describes the steps that need to be followed for setting up the project and its dependencies

### Project setup

The pipeline setup can be achieved by running the following simple commands

- Cleanup pre-existing virtual environments
```
$ make clean
```
- Create a new virtual env and install dependencies
```
$ make setup
```

## Testing

This section describes how to run the tests.

### Invoke tests using Makefile
```
$ make test
```
***Alternately***

### Invoke unit tests normally
```
$ python -m unittest -v
```

## Run
This section describes how to run the jobs.

### Execute the ingestion job
In this job, the wikipedia raw data is downloaded from the base url containing several download links.

- Run ingestion using Makefile
```
$ make ingest
```
***Alternately***

### Run the normal way
```
$ python ingest_data.py
```

### Execute the pageview count aggregation job
In this job, the wikipedia raw data ingested in the previous step is processed and the total count of pageviews 
containing the keyword is derived.

* Please note, that the parameters for the wikipedia version (language) and the search keyword (bitcoin in this case),
are both configurable and can both be passed as input parameters to this aggregation job using the `-l` and `-k` flags 
respectively. The default values for these parameters are `en` and `bitcoin` respectively.

- Run aggregation using Makefile
```
$ make count
```
***Alternately***

### Run the normal way
```
$ python pageview_count.py
```
### Run with parameters
```
$ python pageview_count.py -l de -k java
```
