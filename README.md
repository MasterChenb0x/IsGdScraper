# IsGdScraper

### DESCRIPTION
This project scrapes is.gd links for a project on security analysis. It is not the author's intention to use information gained with this project in a malicous manner. Insights into findings will be released upon the final presentation.

### USAGE
For now, run link-generate.py first, and then shortscraper.py. My plan is to merge all interactive functionality into one main program with background functionality modularized into their own library.

### CHANGELOG

#### 2019-03-26
Still a work in progress, but here are the changes!

1. Verified links are being requested through proxy.
2. Randomized the links so that scraping is not sequential.

##### To Do
1. If a proxy doesn't work, grab next proxy without skipping link.
2. Write valid links to a file.
3. Exception handling for ProxyError.

#### 2019-03-19
Very much a work in progress at the moment. Most of the code written in the past week has been for testing purposes only and will be removed for a public release. We can now make proxied requests for hopefully faster scraping and avoiding rate limits. Actual production scraping still needs to be coded.

#### 2019-03-11
Revisiting code base. Link generation was redone to give choice to the way links are generated ( all caps, all lower case, numbers only, etc).New link generation is still a work in progress. Uploading current code to repository for saved work.

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
