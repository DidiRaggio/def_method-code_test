#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Auxiliary function for input argument validation."""

# Standard Library Imports
import sys


def validate_input_args():
    """Validate number of arguments passed."""
    args_length = len(sys.argv)
    if args_length not in [2, 3]:
        raise Exception("You must pass atleast one argument to text_processor")

    file_path = sys.argv[1]
    output_view_id = int(sys.argv[2]) if args_length == 3 else 3

    return file_path, output_view_id
