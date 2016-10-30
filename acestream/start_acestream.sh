#!/bin/sh
PATH=/sbin:/usr/sbin:/bin:/usr/bin
ACEADDON="/acestream"
ACECHROOT="androidfs"
/system/bin/sh -c "cd /system/data/data/org.acestream.engine/files ; /system/bin/acestream.sh" > $ACEADDON/acestream.log 2>&1 - << EOF
import os
import argparse
from acestreamengine import Core
 
params = "$@".split(' ')
if params == ['']:
    params = []
 
Core.run(params)
EOF
