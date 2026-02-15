import time
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


# class to create and store rsa keys
class MyKey:
    def __init__(self, is_expired=False):

        # create random id for key
        self.id = str(uuid.uuid4())

        # generate private key
        self.private = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

        # get public key from private key
        self.public = self.private.public_key()

        # get current time
        now = int(time.time())

        # set expiration in past if expired
        if is_expired:
            self.exp = now - 3600

        # otherwise set expiration in future
        else:
            self.exp = now + 3600


# make one valid key
good_key = MyKey(is_expired=False)

# make one expired key
old_key = MyKey(is_expired=True)


# return valid key
def get_good_key():
    return good_key


# return expired key
def get_old_key():
    return old_key


# return only keys that are still valid
def get_good_public_keys():
    now = int(time.time())

    # list to hold valid keys
    key_list = []

    # check if key is expired
    if good_key.exp > now:
        key_list.append(good_key)

    return key_list
