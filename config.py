#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    """ Get BOT_ID """
    with open(".localConfigs", "r") as f:
        for line in f:
            if line.startswith("BOT_ID="):
                BOT_ID = line.split("=")[1].strip()
                break
        else:
            BOT_ID = None
    """ Get BOT_PASSWORD """
    with open(".localConfigs", "r") as f:
        for line in f:
            if line.startswith("BOT_PASSWORD="):
                BOT_PASSWORD = line.split("=")[1].strip()
                break
        else:
            BOT_PASSWORD = None

    PORT = 3978
    APP_ID = BOT_ID
    APP_PASSWORD = BOT_PASSWORD
    # APP_ID = os.environ.get("MicrosoftAppId", BOT_ID)
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", BOT_PASSWORD)
