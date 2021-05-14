import logging
import iptools


def main(event, context):
    logging.info('Python HTTP trigger function processed a request.')

    cidr = event['cidrSignature']

    lis = iptools.IpRangeList(cidr)
    first = str(lis).split(',')[0].split("'")[-2]
    last = str(lis).split(',')[1].split("'")[-2]


    data = {'cidrSignature': cidr, 'firstAddress': first
        , 'lastAddress': last, 'addressCount': len(lis)}
    return data

