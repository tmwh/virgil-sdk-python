# Copyright (C) 2016 Virgil Security Inc.
#
# Lead Maintainer: Virgil Security Inc. <support@virgilsecurity.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#     (3) Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import urllib2
import json


class VirgilClient:
    # url - string, API location, for example https://keys.virgilsecurity.com/v3
    # token - string, Access token encoded as base64. Required for any API call
    def __init__(self, url, token=None):
        self.url = url
        self.token = token

    # Send request to specific endpoint
    # endpoint - string, API endpoint, for example /public-key/{public-key-id}
    # headers - dictionary, represents request header
    # values - dictionary, represents request body
    def _api_request(self, method, endpoint, headers=None, values=None):
        url = self.url+endpoint
        data = None
        if values:
            data = json.dumps(values).encode()
        if headers:
            req = urllib2.Request(url, data=data, headers=headers)
        else:
            req = urllib2.Request(url, data=data)
        req.get_method = lambda: method
        try:
            response = urllib2.urlopen(req)
            return response.read()
        except urllib2.HTTPError as e:
            return e.read()
