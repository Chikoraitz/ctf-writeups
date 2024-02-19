#!/usr/bin/python3

import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
key_part_dynamic1_trial = ""

user_hash = hashlib.sha256(b"SCHOFIELD").hexdigest()

for sha256_digest_i in [4,5,3,6,2,7,1,8]:
  key_part_dynamic1_trial += user_hash[sha256_digest_i]

print(key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial)
