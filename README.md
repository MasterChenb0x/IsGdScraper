# IsGdScraper

### DESCRIPTION
This project scrapes is.gd links for a project on security analysis. It is not the author's intention to use information gained with this project in a malicous manner. Insights into findings will be released upon the final presentation.

### USAGE
In order, run:
1. link-generate.py. This will generate a text file of approximately 2.3 million parameters. You can split this file to divide the workload among multiple computers. Your choice.
2. isgd.py. this will initiate the proxy scrape and start resolving links. The input file is hardset, so you would need to change it depending on how you split the generated links.

### CHANGELOG

#### 2017-02-13
Removing proxy_scraper.php since URLs are resolved with HTTPS. Using proxy_scraper.php was cuasing false negatives in the URL resolution.
Code refactored by Kelso

#### 2017-02-01.2
Commented major tasks in each script.
Old scripts are left in for document's sake.

#### 2017-02-01
Revamped the way the datamining works.
Added isgd.py and isgd.sh.
Added proxy_scraper.php, but I did not write this file. It was written by a friend for a separate project, but the functionality applies here.
The scrape is now done through a proxy setup for potentially faster scraping without a constant hammer from one IP.
That should have been implemented from the beginning, but this is a learning process.
Initiate by ./isgd.py

##### 2017-01-17
Successfully feeding generated links through url-resolve.sh

##### 2017-01-15
Initialization.
Link generation success!
Need to take generated links through a web scraper.
