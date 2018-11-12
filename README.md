# yelp Business Scraper for Python

The script provided here scrapes business names, addresses and contact info for specified business type and cities.

The script makes use of HTML patterns and BeautifulSoup4 to scrape information.
Further processing might be required for street, zip and xity fields since HTML pattern is not always the same across all businesses.

You can stabilize your results by adding details to the location parameter (i.e. "Dublin,+CA"), otherwise you may get irrelevant search results such as businesses in Dublin, Ireland.

**Important Note**: Limit your city list to a reasonable number or you may get your IP temporarily/permanently banned by yelp.com.  
Use at your own risk.

A sample list of locations is provided in `cities.csv` file.

### Features to be added:
Following features will soon be added to the script:
- Scraping business category, so you will get less irrelevant results or have more filtering options,
- Improvement in address scraping,
- Star rating
