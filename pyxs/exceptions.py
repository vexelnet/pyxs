# -*- coding: utf-8 -*-
"""
    pyxs.exceptions
    ~~~~~~~~~~~~~~~

    This module implements a number of Python exceptions used by
    :mod:`pyxs` classes.
"""

__all__ = frozenset(["InvalidOperation", "InvalidPayload"])


class InvalidOperation(ValueError):
    """Exception raised when :class:`~pyxs.Packet` is passed an
    operation, which isn't listed in :data:`~pyxs.Op`.

    :param int operation: invalid operation value.
    """


class InvalidPayload(ValueError):
    """Exception raised when :class:`~pyxs.Packet` is initialized
    with payload, which exceeds 4096 bytes restriction or contains
    characters outsied the ``[0x20;0x7f]`` range

    :param bytes operation: invalid payload value.
    """
