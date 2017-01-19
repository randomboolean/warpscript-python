# WarpScript-Python #

This provides an interactive python api for WarpScript.

### As python function ###

Make sure they are in your python path then:

* `from warpscript import post`
* `from permalink import generate`

### Inside a Notebook ###

* See `example.ipynb`

### As command line ###

* `python warpscript.py --help`
* `python permalink.py --help`

### Arguments ###

```
usage: warpscript.py [-h] [--url [URL]] [--token [TOKEN]] [--gzip]                                                                                
                     [--timeout [TIMEOUT]] [--dontVerifySSL]                                                                                      
                     code [code ...]                                                                                                              
                                                                                                                                                  
Post warpscript code to a Warp 10 platform                                                                                                        
                                                                                                                                                  
positional arguments:                                                                                                                             
  code                  Warpscript code or filename ending with ".mc2"                                                                            
                                                                                                                                                  
optional arguments:                                                                                                                               
  -h, --help            show this help message and exit                                                                                           
  --url [URL], -u [URL]                                                                                                                           
                        Url of Warp10 platform. Default to                                                                                        
                        https://warp.cityzendata.net/api/v0/exec                                                                                  
  --token [TOKEN], -t [TOKEN]                                                                                                                     
                        In the warpscript code, will overwrite start of lines                                                                     
                        ending with: 'TOKEN' STORE. Do nothing if this                                                                            
                        argument is not set                                                                                                       
  --gzip, -g            Use gzip encoding. Default to False                                                                                       
  --timeout [TIMEOUT], -s [TIMEOUT]                                                                                                               
                        Timeout value (in s). Default to None                                                                                     
  --dontVerifySSL, -n   Verify SSL or not. Verify SSL per default

```

```
usage: permalink.py [-h] [--url [URL]] [--url_quantum [URL_QUANTUM]] [--plot]
                    [--token [TOKEN]]
                    code [code ...]

Generate permalink to quantum UI

positional arguments:
  code                  Warpscript code or filename ending with ".mc2"

optional arguments:
  -h, --help            show this help message and exit
  --url [URL], -u [URL]
                        Url of Warp10 platform. Default to
                        https://warp.cityzendata.net/api/v0/exec
  --url_quantum [URL_QUANTUM], -q [URL_QUANTUM]
                        Url of quantum application. Default to
                        https://home.cityzendata.net/quantum/
  --plot, -p            Link directly to the plot. Default to False
  --token [TOKEN], -t [TOKEN]
                        In the warpscript code, will overwrite start of lines
                        ending with: 'TOKEN' STORE. Do nothing if this
                        argument is not set
```