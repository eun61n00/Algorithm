# -*- coding: utf-8 -*-
# boj 10930 SHA-256

import hashlib

str = input()
print(hashlib.sha256(str.encode('utf-8')).hexdigest())