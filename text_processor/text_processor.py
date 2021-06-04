#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Text processing logic."""

import os


class TextProcessor(object):
    """TextProcessor class."""

    def __init__(self, file_path: str):
        """Intialize class variables.

        Args:
            file_path (str): path to file to parse.
        """
        super(TextProcessor, self).__init__()
        self.file_path = self.validate_file_path(file_path)

    def validate_file_path(self, file_path):
        """Validate file path."""
        file_path = self.file_path_exists(
            self.validate_file_path_datatype(file_path)
        )
        return file_path

    def validate_file_path_datatype(self, file_path):
        """Validate file path is string."""
        if type(file_path) == str:
            return file_path
        else:
            raise TypeError("The argument is not is not a string")

    def file_path_exists(self, file_path):
        """Check path exists."""
        if os.path.exists(file_path):
            return file_path
        else:
            raise FileNotFoundError

    def parse_gender(self, gender):
        """Convert single character into gender."""
        if gender == 'F':
            return 'Female'
        elif gender == 'M':
            return "Male"
        else:
            return gender

    def format_date(self, date):
        """Replace dashes with slashes."""
        return date.replace("-", "/")

    def identify_separator(self, line):
        """Identify line separator."""
        if "|" in line:
            self.separator = " | "
            self.property_dict = {
                "last_name": 0,
                "first_name": 1,
                "gender": 3,
                "date": 5,
                "color": 4
            }

        elif "," in line:
            self.separator = ", "
            self.property_dict = {
                "last_name": 0,
                "first_name": 1,
                "gender": 2,
                "date": 4,
                "color": 3
            }

        else:
            self.separator = " "
            self.property_dict = {
                "last_name": 0,
                "first_name": 1,
                "gender": 3,
                "date": 4,
                "color": 5
            }

    def process(self):
        """Process the line"""
        output = ""
        with open(self.file_path) as file:
            for i, line in enumerate(file):
                line = line.rstrip()
                if i == 0:
                    self.identify_separator(line)

                properties = line.split(self.separator)
                output += f"{properties[self.property_dict['last_name']]} " \
                          f"{properties[self.property_dict['first_name']]} " \
                          f"{self.parse_gender(properties[self.property_dict['gender']])}" \
                          f" {self.format_date(properties[self.property_dict['date']])}" \
                          f" {properties[self.property_dict['color']]}\n"
        return output
