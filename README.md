# tropofy_event_tracking_demo
A simple attraction/ride popularity tracking system for a school fete/fair type event (demo) using the Tropofy platform.

This project requires a Tropofy API key. Visit https://tropofy.com/index.html#pricing for more info. 

## Quick start

`$ git clone git@github.com:henrycjc/tropofy_event_tracking_demo.git && cd tropofy_event_tracking_demo`  
`$ vim run.py` (add your API keys in the appropriate places)  
`$ python setup.py develop`  
`$ python run.py` (this will serve the app on localhost:8080)  


## Dependencies

This project uses the Tropofy platform. 

macOS: If you have trouble compiling `psycopg2`, you may need to update Xcode / install Xcode CLI tools (most recent version) as you need a certain version of libssl. 

