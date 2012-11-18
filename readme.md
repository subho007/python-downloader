Python mass downloader using BING Search API v2.0
=================================================

This small python script can be used to download files from the result obtained 
by the search key provided. This is a small utility written for dummy mass download,
for your fuzzing needs !

Requirements
============

- Python >= 2.6
- Python Request module ( https://github.com/kennethreitz/requests )
- Bing Search API ( http://www.bing.com/developers/ )
- BeautifulSoup Python module for google_downloader.py ( http://www.crummy.com/software/BeautifulSoup/ )

Usage
=====

For Bing Search Downloader
-------------------------
Please set your API key in the script replacing `<BING-API-ID>`

```
python bing_search_api.py -h
Usage: bing_search_api.py [options]

Options:
  -h, --help            show this help message and exit
  -s SEARCH, --search=SEARCH
                        keyword to SEARCH
  -f WEBFILE, --file=WEBFILE
                        Filetype to SEARCH
  -n NUM, --number=NUM  Number of results to SEARCH
```
For Google Search Downloader
----------------------------

```
./google-downloader.py --help
Usage: google-downloader.py [options]

Options:
  -h, --help            show this help message and exit
  -s SEARCH, --search=SEARCH
                        keyword to SEARCH
  -n NUM, --number=NUM  Number of results to SEARCH
  -d DOMAIN, --domain=DOMAIN
                        The url you want google.com or google.co.in, all you
                        have to do is enter 'com' or 'co.in' etc.
  -l LANGUAGE, --language=LANGUAGE
                        Select your language (Default en)
```

Author
======

Coded by Subho Halder
- Web: http://subhohalder.com/
- Blog: http://subho.me/

Feel free to contact me !