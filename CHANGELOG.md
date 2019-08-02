### CHANGELOG

#### 2019-08-02 
Lots of cleanup in preparation for ReconVillage @ DEF CON.
Link generation tool rewritten.
Image Loader created to view pics in rapid succession.
Filetype analysis added.
This isn't 2017 anymore.

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
