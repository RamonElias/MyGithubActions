#!/usr/bin/env python

import os
from base64 import b64encode
from nacl import encoding, public


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


if __name__ == "__main__":
    # Get values from environment variables
    public_key = os.environ.get("PUBLIC_KEY")
    secret_value = os.environ.get("SECRET_VALUE")
    # print(public_key)
    # print(secret_value)

    if not public_key or not secret_value:
        print("Error: PUBLIC_KEY and SECRET_VALUE environment variables must be set.")
        exit(1)

    encrypted_value = encrypt(public_key, secret_value)
    print(encrypted_value)
