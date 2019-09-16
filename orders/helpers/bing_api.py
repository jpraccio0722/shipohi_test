import requests
from shipohi.settings import BING_KEY
import urllib.parse as parse
import logging
import json
from orders.models import Warehouse
import sys


def find_nearest_warehouse(**kwargs):
    logger = logging.getLogger()
    bing_endpoint = f'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?'
    warehouses = Warehouse.objects.all()
    address = kwargs['address']

    nearest_warehouse = None
    nearest_distance = float(sys.maxsize)

    for warehouse in warehouses:
        endpoint = bing_endpoint
        endpoint += f'origins={{{warehouse.address.lat, warehouse.address.lon}}}'
        endpoint += f'&destinations={{{address.lat, address.lon}}}'
        endpoint += f'&travelMode=driving&key={BING_KEY}'

        resp = requests.get(endpoint)

        if resp.status_code == 200:
            data = json.loads(resp.text)

            try:
                for sets in data['resourceSets']:
                    for resource in sets['resources']:
                        if resource['results'][0]['travelDistance'] < nearest_distance:
                            nearest_warehouse = warehouse
                            nearest_distance = resource['results'][0]['travelDistance']

            except KeyError as e:
                raise e
        else:
            logger.error('Bad response: {}'.format(resp.status_code))

    return nearest_warehouse


def get_lat_lon(**kwargs):
    logger = logging.getLogger()

    try:
        address=kwargs['address']
        logger.info(f'address: {address}')
    except KeyError:
        return None
        # do something

    bing_address_endpoint = \
        f'http://dev.virtualearth.net/REST/v1/Locations/US/' \
        f'{address.state_province}/{address.post_code}/{parse.quote(address.address1)}/?maxResults=1&key={BING_KEY}'

    resp = requests.get(bing_address_endpoint)

    if resp.status_code == 200:

        data = json.loads(resp.text)
        logger.info(f'{data}')

        try:
            # todo check lengths assuming one result
            for sets in data['resourceSets']:
                for resource in sets['resources']:
                    lat = resource['point']['coordinates'][0]
                    lon = resource['point']['coordinates'][1]

                    return lat, lon

        except KeyError as e:
            logger.exception(f'Key not found: {e}')
            raise e

    else:
        raise Exception(f'Bad response from bing api {resp.status_code} : {resp.text}')


