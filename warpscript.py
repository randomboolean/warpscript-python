# A little python function to post warpscript

url = 'https://warp.cityzendata.net/api/v0/exec'

import requests as req
import json
import re

def post(warpscript, url=url, token=None, gzip=False, timeout=None, verifySSL=True):
    
    # check if warpscript is a filename
    if len(warpscript) > 4:
        if warpscript[-4:] == '.mc2':
            warpscript = open(warpscript).read()

    # handling token
    if not(token is None):
        warpscript = re.sub(".*'TOKEN' STORE", "'" + token + "' 'TOKEN' STORE", warpscript)
    
    # posting
    headers = {'Accept-Encoding':'gzip'} if gzip else None
    answer = req.post(url, warpscript, timeout=timeout, verify=verifySSL, headers=headers)
    
    # return json
    if answer.status_code == 200:
        return json.dumps(answer.json() , indent=2)
    else:
        return answer.text
    
if __name__ == '__main__':
    import argparse as ap
    
    parser = ap.ArgumentParser(description='Post warpscript code to a Warp 10 platform')
    parser.add_argument('warpscript', metavar='code', nargs='+',
                     help='Warpscript code or filename ending with ".mc2"')
    parser.add_argument('--url', '-u', nargs='?', default=url,
                     help='Url of Warp10 platform. Default to https://warp.cityzendata.net/api/v0/exec')
    parser.add_argument('--token', '-t', nargs='?', default=None,
                     help="In the warpscript code, will overwrite start of lines ending with: 'TOKEN' STORE. Do nothing if this argument is not set")
    parser.add_argument('--gzip', '-g', action='store_true',
                     help='Use gzip encoding. Default to False')
    parser.add_argument('--timeout', '-s', nargs='?', default=None, type=int,
                     help='Timeout value (in s). Default to None')
    parser.add_argument('--dontVerifySSL', '-n', action='store_false',
                     help='Verify SSL or not. Verify SSL per default')
    
    args = parser.parse_args()
    
    print post((' ').join(args.warpscript), args.url, args.gzip, args.timeout, args.verifySSL)

    
    
    
 