# tropofy_event_tracking_demo
A simple food stall tracking system for a school fete/fair type event (demo) using the Tropofy platform.

This project requires a Tropofy API key. Visit https://tropofy.com/index.html#pricing for more info. 

## Quick start

* `$ git clone git@github.com:henrycjc/tropofy_event_tracking_demo.git && cd tropofy_event_tracking_demo`
* `$ virutalenv env && source env/bin/activate`
* `$ cp settings.example.json settings.json`
* `$ vim settings.json` _(add your API keys in the appropriate places)_
* `$ python setup.py develop`
* `$ python run.py` _(this will serve the app on localhost:8080)_


## Dependencies

This project uses the Tropofy platform. It may take some time to install as there are a number of scientific
libs that will need to be compiled.

macOS: If you have trouble compiling `psycopg2`, you may need to update Xcode / install Xcode CLI tools (most recent version) as you need a certain version of libssl. 

