# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, unicode_literals

from functools import wraps

import pytest

from hypothesis import given


def fails(f):
    @wraps(f)
    def inverted_test(*arguments, **kwargs):
        with pytest.raises(AssertionError):
            f(*arguments, **kwargs)
    return inverted_test


@given(int)
def test_ints_are_ints(x):
    pass


@fails
@given(int)
def test_ints_are_floats(x):
    assert isinstance(x, float)
