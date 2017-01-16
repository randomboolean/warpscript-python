# A little python function to generate a permalink

url = 'https://warp.cityzendata.net/api/v0/exec'
url_quantum = 'https://home.cityzendata.net/quantum/'

import base64 as b64

def generate(warpscript, plot=False, url=url, url_quantum=url_quantum, token=None):
    
    # check if warpscript is a filename
    if len(warpscript) > 4:
        if warpscript[-4:] == '.mc2':
            warpscript = open(warpscript).read()

    # handling token
    if not(token is None):
        warpscript = re.sub(".*'TOKEN' STORE", "'" + token + "' 'TOKEN' STORE", warpscript)
    
    return url_quantum + ('#/plot/' if plot else '#/warpscript/') + b64.b64encode(warpscript) + '/' + b64.b64encode(url)

if __name__ == '__main__':
    import argparse as ap
    
    parser = ap.ArgumentParser(description='Generate permalink to quantum UI')
    parser.add_argument('warpscript', metavar='code', nargs='+',
                     help='Warpscript code or filename ending with ".mc2"')
    parser.add_argument('--url', '-u', nargs='?', default=url,
                     help='Url of Warp10 platform. Default to ' + url)
    parser.add_argument('--url_quantum', '-q', nargs='?', default=url_quantum,
                     help='Url of quantum application. Default to ' + url_quantum)
    parser.add_argument('--plot', '-p', action='store_true',
                     help='Link directly to the plot. Default to False')
    parser.add_argument('--token', '-t', nargs='?', default=None,
                     help="In the warpscript code, will overwrite start of lines ending with: 'TOKEN' STORE. Do nothing if this argument is not set")
    
    args = parser.parse_args()
    warpscript = (' ').join(args.warpscript)
    print generate(warpscript, args.url, args.url_quantum, args.plot)
