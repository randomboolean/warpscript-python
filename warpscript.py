# A little python function to post warpscript

url = 'https://warp.cityzendata.net/api/v0/exec'

import requests as req
import json

def post(warpscript, url=url, gzip=False, timeout=None, verifySSL=True):
    
    # check if warpscript is a filename
    if len(warpscript) > 4:
        if warpscript[-4:] == '.mc2':
            warpscript = open(warpscript).read()
    
    # posting
    headers = {'Accept-Encoding':'gzip'} if gzip else None
    answer = req.post(url, warpscript, timeout=timeout, verify=verifySSL, headers=headers)
    
    # return json
    if answer.status_code == 200:
        return json.dumps(answer.json() , indent = 2)
    else:
        return answer.text
    
if __name__ == '__main__':
    import sys
    import argparse as ap
    
    parser = ap.ArgumentParser(description='Post warpscript code to a warp10 platform')
    parser.add_argument('warpscript', metavar='code', nargs='+',
                     help='Warpscript code or file name')
    parser.add_argument('--url', '-u', nargs='?', default=url,
                     help='Url of Warp10 platform. Default to https://warp.cityzendata.net/api/v0/exec')
    parser.add_argument('--gzip', '-g', nargs='?', default=False, type=bool,
                     help='Use gzip encoding. Default to False')
    parser.add_argument('--timeout', '-t', nargs='?', default=None, type=int,
                     help='Timeout value (in s). Default to None')
    parser.add_argument('--verifySSL', '-s', nargs='?', default=True, type=bool,
                     help='Verify SSL or not. Default to True')
    
    args = parser.parse_args()
    
    print post((' ').join(args.warpscript), args.url, args.gzip, args.timeout, args.verifySSL)

    
    
    
 