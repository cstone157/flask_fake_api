# flask-app.py
from flask import Flask, request
import json
import random
from datetime import datetime

## Some constants
_NEXT_STEPS, _PROBABILITY, _MIN_TIME, _DURATION =\
  "NEXT_STEPS", "PROBABILITY", "MIN_TIME", "DURATION"

class track:
  _DEFAULT, _FIND, _FIX, _TRACK, _TARGET, _APPROVED, _COMPLETE, _DROP = \ 
    "DEFAULT", "FIND", "FIX", "TRACK", "TARGET", "APPROVED", "COMPLETE", "DROP"
  
  _STEPS = {
    track._DEFAULT: {
      _NEXT_STEPS: [ track._FIND ],
      _PROBABILITY: [ 1.0 ],
      _MIN_TIME: [ 60 ],
      _DURATION: [ 3600 ],
    },
    track._FIND: {
      _NEXT_STEPS: [ track._FIX, track._TRACK, track._TARGET, track._APPROVED, track._DROP,  ],
      _PROBABILITY: [ 0.10, 0.11, 0.12, 0.13, 1.0,  ],
      _MIN_TIME: [ 60, 360, 360, 360, 0,  ],
      _DURATION: [ 300, 600, 1200, 1800, 1,  ],
    },
    
  }
  
  __init__(self, prev_status=track._DEFAULT, created_at=datetime.now()):
    self.prev_status = prev_status
    self.created_at = created_at

## Status CONSTANTS


## What are the tracks that we are currently tracking and 
##     what are the messages that we have built up.
_tracks = []
_messages = []

def _create_new_message(prev_status, created_at, prev_at)


# create a Flask instance
app = Flask(__name__)
  
## Return all of the messsages that we have collected
@app.route('/messages', methods=['GET'])
def square():
  global messages
  
  tmp = _messages
  _messages = []
  return json.dumps(tmp)
