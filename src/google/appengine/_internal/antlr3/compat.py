#!/usr/bin/env python
#
# Copyright 2007 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Compatibility stuff"""































try:
  set = set
  frozenset = frozenset
except NameError:
  from sets import Set as set, ImmutableSet as frozenset


try:
  reversed = reversed
except NameError:

  def reversed(l):
    l = l[:]
    l.reverse()
    return l