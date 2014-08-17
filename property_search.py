from __future__ import division

import requests
import pandas as pd

# NOTE: Rightmove also seem to provide a data api, maybe there is a good way to combine the data of both!
# http://www.rightmove.co.uk/adf.html

if __name__ == '__main__':

    with open('key.txt', 'r') as fp:
        DEVELOPER_KEY = fp.read().rstrip()

    # Prices are listed in per-week format
    params = {
        'api_key': DEVELOPER_KEY,
        'session_id': None,
        'listing_status': 'rent',
        'maximum_price': 500,
        'minimum_beds': 3,
        'maximum_beds': 3,
        'furnished': 'furnished',
        'area': 'London Zone 2',
        'page_size': 100,
    }

    columns = [
        'displayable_address',
        'outcode',
        'price',
        'num_bedrooms',
        'property_type',
        'description',
        'latitude',
        'longitude',
    ]

    # http://developer.zoopla.com/docs/Property_listings
    req = requests.get('http://api.zoopla.co.uk/api/v1/property_listings.json', params=params)

    # Convert the incoming data to a dictionary
    json_data = req.json()

    # Place in a DataFrame
    table = pd.DataFrame(json_data['listing'])
    print table[columns]
    print table.shape

    from pandas import ExcelWriter
    writer = ExcelWriter('/home/michaela/zoopla.xls')
    table[columns].to_excel(writer)
    writer.close()
