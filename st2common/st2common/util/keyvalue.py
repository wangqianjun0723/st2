# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from st2common.constants.keyvalue import ALL_SCOPE, DATASTORE_PARENT_SCOPE
from st2common.constants.keyvalue import DATASTORE_SCOPE_SEPARATOR

__all__ = [
    'get_datastore_full_scope'
]


def get_datastore_full_scope(scope):
    if scope == ALL_SCOPE:
        return scope

    if DATASTORE_PARENT_SCOPE in scope:
        return scope

    return '%s%s%s' % (DATASTORE_PARENT_SCOPE, DATASTORE_SCOPE_SEPARATOR, scope)
