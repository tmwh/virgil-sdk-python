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

import base64
import json
import random


class Helper:
    @staticmethod
    def trim_public_key(key):
        key = key.replace("-----BEGIN PUBLIC KEY-----\n", "")
        key = key.replace("\n-----END PUBLIC KEY-----\n", "")
        key = key.replace("\n", "")
        return key

    @staticmethod
    def trim_private_key(key):
        key = key.replace("-----BEGIN ENCRYPTED PRIVATE KEY-----\n", "")
        key = key.replace("\n-----END ENCRYPTED PRIVATE KEY-----\n", "")
        key = key.replace("\n", "")
        return key

    @staticmethod
    def remove_slashes(input):
        return input.replace("\\", "")

    @staticmethod
    def json_dumps(values):
        return json.dumps(values).encode()

    @staticmethod
    def json_loads(values):
        return json.loads(values)

    @staticmethod
    def generate_id():
        while True:
            bits = [format(random.getrandbits(16*i), 'x') for i in (2, 1, 1, 1, 3)]
            new_id = '-'.join(bits)
            if len(new_id) == 36:
                return new_id