#!/usr/bin/env python3

import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logging.info('Event:\n{}'.format(json.dumps(event, indent=4)))
    logging.info('so and so')
