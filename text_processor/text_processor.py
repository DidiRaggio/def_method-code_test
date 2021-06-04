#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Text processing logic."""

# Standard Library Imports
import os
import datetime


class TextProcessor(object):
    """TextProcessor class."""

    def __init__(self, file_path, output_view_id=3):
        """Intialize class variables.

        Args:
            file_path (str): path to file to parse.
            output_view_id (int): defines the output sorting method.
        """
        super(TextProcessor, self).__init__()
        self.file_path = self.validate_file_path(file_path)
        self.output_view_id = output_view_id
        self.separator = None
        self.property_indexes = None
        self.parsed_file = None
        self.output = ""

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
            self.property_indexes = {
                "last_name": 0,
                "first_name": 1,
                "gender": 3,
                "birthdate": 5,
                "favorite_color": 4
            }

        elif "," in line:
            self.separator = ", "
            self.property_indexes = {
                "last_name": 0,
                "first_name": 1,
                "gender": 2,
                "birthdate": 4,
                "favorite_color": 3
            }

        else:
            self.separator = " "
            self.property_indexes = {
                "last_name": 0,
                "first_name": 1,
                "gender": 3,
                "birthdate": 4,
                "favorite_color": 5
            }

    def process(self):
        """Process the file."""
        self.parse()
        self.sort_output()

        return self.output

    def parse(self):
        """Parse the file."""
        parsed_file = []
        with open(self.file_path) as file:
            for i, line in enumerate(file):
                line = line.rstrip()
                if i == 0:
                    self.identify_separator(line)

                properties = line.split(self.separator)
                property_dict = {
                    "last_name": properties[
                        self.property_indexes['last_name']],
                    "first_name": properties[
                        self.property_indexes['first_name']],
                    "gender": self.parse_gender(properties[
                        self.property_indexes['gender']]),
                    "birthdate": self.format_date(properties[
                        self.property_indexes['birthdate']]),
                    "favorite_color": properties[
                        self.property_indexes['favorite_color']]
                }
                property_dict["string"] = f"{property_dict['last_name']} " \
                                          f"{property_dict['first_name']} " \
                                          f"{property_dict['gender']}" \
                                          f" {property_dict['birthdate']}" \
                                          f" {property_dict['favorite_color']}\n"

                parsed_file.append(property_dict)
        self.parsed_file = parsed_file

    def sort_output(self):
        """Sort the output in accordace to view id."""
        # Sort Female first, and then by last name ascending.
        if self.output_view_id == 1:
            sorted_list = sorted(
                self.parsed_file,
                key=lambda v: (
                    v["gender"].lower(), v["last_name"].lower()
                )
            )
        # Sort by birhtday accending and then by last name acending.
        elif self.output_view_id == 2:
            sorted_list = sorted(
                self.parsed_file,
                key=lambda v: (
                    datetime.datetime.strptime(v['birthdate'], '%m/%d/%Y'),
                    v["last_name"].lower()
                )
            )
        # Sort by last name decending.
        elif self.output_view_id == 3:
            sorted_list = sorted(
                self.parsed_file, key=lambda i: i['last_name'].lower(),
                reverse=True
            )
        for person in sorted_list:
            self.output += person["string"]
