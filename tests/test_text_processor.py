#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
"""Command line text processor."""

# Standard Library Imports
import os
import pytest

# Internal Imports
from text_processor.main import main
from text_processor.text_processor import TextProcessor


@pytest.fixture
def text_processor():
    """Generate TextProcessor instance."""
    return TextProcessor("./testing/space.txt")


def test_text_processor_TextProcessor_class():
    """Test instanciation of TextProcessor class."""
    tp = TextProcessor("./testing/space.txt")
    assert tp.__class__.__name__ == "TextProcessor" 
    assert tp.file_path == "./testing/space.txt"


    with pytest.raises(FileNotFoundError):
        assert TextProcessor("do-not-exist.txt")


def test_text_processor_file_path_datatype_failure(mocker):
    """Test whether argument from the command line is valid datatype."""
    mocker.patch(
        "sys.argv",
        [
            os.getcwd(),
            2,
        ],
    )

    with pytest.raises(TypeError):
        assert main()

    mocker.patch(
        "sys.argv",
        [
            os.getcwd(),
            None,
        ],
    )

    with pytest.raises(TypeError):
        assert main()


def test_text_processor_nonexistant_filepath(mocker):
    """Test whether argument from the command line ."""
    mocker.patch(
        "sys.argv",
        [
            os.getcwd(),
            "non-existant.txt",
        ],
    )

    with pytest.raises(FileNotFoundError):
        assert main()


def test_text_processor_format_date(text_processor):
    """Test TextProcessor's formatting of dates."""
    assert text_processor.format_date("20-10-1988") == "20/10/1988"
    assert text_processor.format_date("20/10/1988") == "20/10/1988"


def test_text_processor_identify_separator(text_processor):
    """Test whether separator is a comma."""
    # Identify a comma separated line.
    line = "foo, bar"
    text_processor.identify_separator(line)
    assert text_processor.separator == ", "

    # Identify a pipe separated line.
    line = "foo | bar"
    text_processor.identify_separator(line)
    assert text_processor.separator == " | "

    # Identify a space separated line.
    line = "foo bar"
    text_processor.identify_separator(line)
    assert text_processor.separator == " "


def test_text_processor_end_to_end(mocker):
    """End to end test for each of the cases."""
    filenames = [
        "pipe.txt",
        "comma.txt",
        "space.txt"
    ]
    expected_outputs = [
        "Smith Steve Male 3/3/1985 Red\nBonk Radek Male 6/3/1975 Green\nBouillon Francis Male 6/3/1975 Blue\n",
        "Abercrombie Neil Male 2/13/1943 Tan\nBishop Timothy Male 4/23/1967 Yellow\nKelly Sue Female 7/12/1959 Pink\n",
        "Kournikova Anna Female 6/3/1975 Red\nHingis Martina Female 4/2/1979 Green\nSeles Monica Female 12/2/1973 Black\n",
    ]
    for i, expected_output in enumerate(expected_outputs):
        mocker.patch(
            "sys.argv",
            [
                os.getcwd(),
                f"./testing/{filenames[i]}",

            ]
        )
        output = main()
        assert output == expected_output


if __name__ == '__main__':
    pytest.main()