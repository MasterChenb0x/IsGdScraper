# IsGdScraper
## by [MasterChen](https://twitter.com/chenb0x)

### DESCRIPTION
This project scrapes is.gd shortened links for security analysis purposes.
Public release for ReconVillage @ DEF CON 27: 2019-08-09, Friday @ 1100. 

### DISCLAIMER
This is for educational purposes only! It is not the author's intention to use information gained with this project in a malicous manner. Insights into findings will be released upon the final presentation.

### USAGE
In order, run:
1. `link_generator.py` Will generate the character set you want to analyze, i.e [A-Za-z0-9], saved in a file, linkslugs.txt
2. `url-resolve.sh linkslugs.txt` Takes linkslugs.txt as input and starts resolving links from the list, generating the urls-resolved.txt file
3. `image-loader.py` Loads image URLs found into your browser to view. Loads new image every second. **May lead to NSFW material**


If you like this project, [Please Donate](https://www.paypal.com/paypalme2/chenb0x)      
If you hate the developer, [Submit Formal Complaint](https://www.youtube.com/watch?v=zHU2RlSCdxU)

