# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class ModelBreak(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, start_at=None, end_at=None, break_type_id=None, name=None, expected_duration=None, is_paid=None):
        """
        ModelBreak - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'start_at': 'str',
            'end_at': 'str',
            'break_type_id': 'str',
            'name': 'str',
            'expected_duration': 'str',
            'is_paid': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'start_at': 'start_at',
            'end_at': 'end_at',
            'break_type_id': 'break_type_id',
            'name': 'name',
            'expected_duration': 'expected_duration',
            'is_paid': 'is_paid'
        }

        self._id = id
        self._start_at = start_at
        self._end_at = end_at
        self._break_type_id = break_type_id
        self._name = name
        self._expected_duration = expected_duration
        self._is_paid = is_paid

    @property
    def id(self):
        """
        Gets the id of this ModelBreak.
        UUID for this object

        :return: The id of this ModelBreak.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelBreak.
        UUID for this object

        :param id: The id of this ModelBreak.
        :type: str
        """

        self._id = id

    @property
    def start_at(self):
        """
        Gets the start_at of this ModelBreak.
        RFC 3339; follows same timezone info as `Shift`. Precision up to the minute is respected; seconds are truncated.

        :return: The start_at of this ModelBreak.
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """
        Sets the start_at of this ModelBreak.
        RFC 3339; follows same timezone info as `Shift`. Precision up to the minute is respected; seconds are truncated.

        :param start_at: The start_at of this ModelBreak.
        :type: str
        """

        if start_at is None:
            raise ValueError("Invalid value for `start_at`, must not be `None`")
        if len(start_at) < 1:
            raise ValueError("Invalid value for `start_at`, length must be greater than or equal to `1`")

        self._start_at = start_at

    @property
    def end_at(self):
        """
        Gets the end_at of this ModelBreak.
        RFC 3339; follows same timezone info as `Shift`. Precision up to the minute is respected; seconds are truncated. The `end_at` minute is not counted when the break length is calculated. For example, a break from `00:00` to `00:11`  is considered a 10 minute break (midnight to 10 minutes after midnight).

        :return: The end_at of this ModelBreak.
        :rtype: str
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """
        Sets the end_at of this ModelBreak.
        RFC 3339; follows same timezone info as `Shift`. Precision up to the minute is respected; seconds are truncated. The `end_at` minute is not counted when the break length is calculated. For example, a break from `00:00` to `00:11`  is considered a 10 minute break (midnight to 10 minutes after midnight).

        :param end_at: The end_at of this ModelBreak.
        :type: str
        """

        self._end_at = end_at

    @property
    def break_type_id(self):
        """
        Gets the break_type_id of this ModelBreak.
        The `BreakType` this `Break` was templated on.

        :return: The break_type_id of this ModelBreak.
        :rtype: str
        """
        return self._break_type_id

    @break_type_id.setter
    def break_type_id(self, break_type_id):
        """
        Sets the break_type_id of this ModelBreak.
        The `BreakType` this `Break` was templated on.

        :param break_type_id: The break_type_id of this ModelBreak.
        :type: str
        """

        if break_type_id is None:
            raise ValueError("Invalid value for `break_type_id`, must not be `None`")
        if len(break_type_id) < 1:
            raise ValueError("Invalid value for `break_type_id`, length must be greater than or equal to `1`")

        self._break_type_id = break_type_id

    @property
    def name(self):
        """
        Gets the name of this ModelBreak.
        A human-readable name.

        :return: The name of this ModelBreak.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelBreak.
        A human-readable name.

        :param name: The name of this ModelBreak.
        :type: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def expected_duration(self):
        """
        Gets the expected_duration of this ModelBreak.
        Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of the break.

        :return: The expected_duration of this ModelBreak.
        :rtype: str
        """
        return self._expected_duration

    @expected_duration.setter
    def expected_duration(self, expected_duration):
        """
        Sets the expected_duration of this ModelBreak.
        Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of the break.

        :param expected_duration: The expected_duration of this ModelBreak.
        :type: str
        """

        if expected_duration is None:
            raise ValueError("Invalid value for `expected_duration`, must not be `None`")
        if len(expected_duration) < 1:
            raise ValueError("Invalid value for `expected_duration`, length must be greater than or equal to `1`")

        self._expected_duration = expected_duration

    @property
    def is_paid(self):
        """
        Gets the is_paid of this ModelBreak.
        Whether this break counts towards time worked for compensation purposes.

        :return: The is_paid of this ModelBreak.
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """
        Sets the is_paid of this ModelBreak.
        Whether this break counts towards time worked for compensation purposes.

        :param is_paid: The is_paid of this ModelBreak.
        :type: bool
        """

        self._is_paid = is_paid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
