#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Main execution script."""

import sys
from text_processor.text_processor import TextProcessor

def main():
    """Execute text processor."""
    #
    file_path = sys.argv[1]

    text_processor = TextProcessor(file_path=file_path)
    output = text_processor.process()

    return output
