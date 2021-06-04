#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Main execution script."""

# Internal Imports
from text_processor.utils import validate_input_args
from text_processor.text_processor import TextProcessor


def main():
    """Execute text processor."""
    #
    file_path, output_view_id = validate_input_args()

    text_processor = TextProcessor(file_path=file_path, output_view_id=output_view_id)
    output = text_processor.process()

    return output
