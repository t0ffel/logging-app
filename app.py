#!/usr/bin/env python
#
# Sample log generator
#
# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import sys
import time
import os
import string
import logging
import logging.handlers
import argparse


def write_logs(log, podname, namespace, interval):
    '''Emit a formatted payload of random bytes, using a Gaussian
    '''

    count = 0
    tmpl = 'NS:' + namespace + ', POD:' + podname + ', message number {}'
    while True:
        msg = tmpl.format(count)
        log.info(msg)
        count+=1
        time.sleep(interval)


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(module)s: %(message)s')
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    log.addHandler(consoleHandler)

    parser = argparse.ArgumentParser(description='Simplified log generator.')
    parser.add_argument('--pod-name', metavar='POD', dest='podname', default=os.environ.get('HOSTNAME', ''),
			help='Name of the pod to use')
    parser.add_argument('--namespace', default=os.environ.get('NAMESPACE', ''),
            help='Namespace to use in the messages')
    parser.add_argument('--interval', metavar='INTERVAL', type=int,
            default=10,
            help='seconds between messages, defaults to 10')
    args = parser.parse_args()


    try:
        write_logs(log, args.podname, args.namespace, args.interval)
    except KeyboardInterrupt:
        exit(0)
