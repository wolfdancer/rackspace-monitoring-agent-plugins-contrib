#! /usr/bin/python

# http_check.py
# Rackspace Cloud Monitoring Plugin to ping an HTTP/HTTPS URL to get
# response time. This is useful for the case where the server is not 
# available for remote check. 
#
# Copyright (c) 2013, Shane Duan <shane.duan@rackspace.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#
# This plugin expects to make a connection to the URL passed in,
# verify 200 response code, and report the response time
#
# Example criteria :
# if (metric['response_time'] > 2000) {
#   return new AlarmStatus(CRITICAL, 'Server response itme is beyond 2 seconds');
# }
# return new AlarmStatus(OK, 'Server response is within 2 seconds');
#

import sys
import urllib
import datetime


def main(url):
    try:
        start = datetime.datetime.now()
        url_connection = urllib.urlopen(url)
        status_code = url_connection.getcode()
        end = datetime.datetime.now()
        if status_code == 200:
            print "status ok url_check"
            print "metric response_time int32 ", int(round((end-start).microseconds/1000))
        else:
            print "status error", status_code, " ", url_connection.info()
    except Exception, ex:
        print "status error", ex
        raise ex
if __name__ == "__main__":
    main(sys.argv[1])
