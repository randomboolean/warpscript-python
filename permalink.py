url = 'https://warp.cityzendata.net/api/v0/exec'
url_quantum = 'https://home.cityzendata.net/quantum/#/warpscript/'

import base64 as b64

def generate(warpscript, url=url):
    
    # check if warpscript is a filename
    if len(warpscript) > 4:
        if warpscript[-4:] == '.mc2':
            warpscript = open(warpscript).read()
            
    return url_quantum + b64.b64encode(warpscript) + '/' + b64.b64encode(url)

if __name__ == '__main__':
    import argparse as ap
    
    parser = ap.ArgumentParser(description='Generate permalink to quantum UI')
    parser.add_argument('warpscript', metavar='code', nargs='+',
                     help='Warpscript code or file name')
    parser.add_argument('--url', '-u', nargs='?', default=url,
                     help='Url of Warp10 platform. Default to https://warp.cityzendata.net/api/v0/exec')
    
    args = parser.parse_args()
    warpsript = (' ').join(args.warpscript)
    print generate(warpscript, args.url)
