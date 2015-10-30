#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)
import logging

logger = logging.getLogger(__name__)


def handle_smsmo(message):
    logger.info("Received an SMS-MO in handler: {}".format(message))


def handle_smsmt(message):
    logger.info("Sent an SMS-MT in handler: {}".format(message))


def handle_smsdr(message):
    logger.info("Received an SMS-DR in handler: {}".format(message))
