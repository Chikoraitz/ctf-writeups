# Solution

From the source code provided, we can observe that the flag is the crack key. The key is composed of three parts:

-  `key_part_static1_trial` : `"picoCTF{1n_7h3_|<3y_of_"`

- `key_part_dynamic1_trial` : string of length 8
- `key_part_static2_trial` : `"}"`

```python
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial		# b"SCHOFIELD"
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```

If we manage to reverse the key verification process, we can retrieve the key.

```python
def check_key(key, username_trial):

    global key_full_template_trial # "picoCTF{1n_7h3_|<3y_of_" + "xxxxxxxx" + "}"

    if len(key) != len(key_full_template_trial): # 32
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False
        
        return True
```

The dynamic part of the valid key is based on the first 8 characters of the trial username `SHA256` hash in a different order. Since we know that the trial username is `SCHOFIELD`, the key verification can be trivially reversed.

```python
#!/usr/bin/python3

import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
key_part_dynamic1_trial = ""

user_hash = hashlib.sha256(b"SCHOFIELD").hexdigest()

for sha256_digest_i in [4,5,3,6,2,7,1,8]:
  key_part_dynamic1_trial += user_hash[sha256_digest_i]

print(key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial)
```

