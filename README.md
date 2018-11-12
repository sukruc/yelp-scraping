# yelp Business Scraper for Python

## Description:
Scrape your favorite business!

The script provided here scrapes business names, addresses and contact info for specified business type and cities.

The script makes use of HTML patterns and BeautifulSoup4 to scrape information.
Further processing might be required for street, zip and city fields since HTML pattern is not always the same across all businesses.

You can stabilize your results by adding details to the location parameter (i.e. "Dublin,+CA"), otherwise you may get irrelevant search results such as businesses in Dublin, Ireland.

## Usage:

Just pass your list of locations to `location_list` variable and hit "run".
Kick back and watch your script scraping business info for you.

A sample list of locations is provided in `cities.csv` file.

**Important Note**: Limit the length of your location list to a reasonable number or you may get your IP temporarily/permanently banned by yelp.com.
Use at your own risk.


## Features to be added:
Following features will soon be added to the script:
- Scraping business category, so you will get less irrelevant results or have more filtering options,
- Improvement in address scraping,
- Star rating,
- and **Reviews**.
