# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from netseen.common import ns_except
from netseen.objects import fields as netseen_fields


class NetseenObject(object):
    """the base netseen object
    """
    fields = {}

    def __init__(self, **kwargs):
        for name, field in self.fields.items():
            if not isinstance(field, netseen_fields.Field):
                raise ns_except.ObjectFieldInvalid(
                    field=name, objname=self.obj_name())
            self.__dict__[name] = field.constraint(
                obj=self.obj_name(),
                attr=name,
                value=kwargs.get(name))

    @classmethod
    def obj_name(cls):
        """Return the object's name

        Return a canonical name for this object which will be used over
        the wire for remote hydration.
        """
        return cls.__name__
