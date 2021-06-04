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


# def test_text_processor_end_to_end(mocker):
#     """End to end test for each of the cases."""
#     filenames = [
#         "pipe.txt",
#         "comma.txt",
#         "space.txt"
#     ]
#     expected_outputs = [
#         "Smith Steve Male 3/3/1985 Red\nBonk Radek Male 6/3/1975 Green\nBouillon Francis Male 6/3/1975 Blue\n",
#         "Abercrombie Neil Male 2/13/1943 Tan\nBishop Timothy Male 4/23/1967 Yellow\nKelly Sue Female 7/12/1959 Pink\n",
#         "Kournikova Anna Female 6/3/1975 Red\nHingis Martina Female 4/2/1979 Green\nSeles Monica Female 12/2/1973 Black\n",
#     ]
#     for i, expected_output in enumerate(expected_outputs):
#         mocker.patch(
#             "sys.argv",
#             [
#                 os.getcwd(),
#                 f"./testing/{filenames[i]}",

#             ]
#         )
#         output = main()
#         assert output == expected_output

def test_text_processor_end_to_end_pipe_separator(mocker):
    """End to end test for each of the cases with a pipe separator."""
    expected_outputs = [
        # Sort Female first, and then by last name ascending.
        "Bonk Radek Male 6/3/1975 Green\nBouillon Francis Male 6/3/1975 Blue\nSmith Steve Male 3/3/1985 Red\n",
        # Sort by birhtday accending and then by last name acending.
        "Bonk Radek Male 6/3/1975 Green\nBouillon Francis Male 6/3/1975 Blue\nSmith Steve Male 3/3/1985 Red\n",
        # Sort by last name decending.
        "Smith Steve Male 3/3/1985 Red\nBouillon Francis Male 6/3/1975 Blue\nBonk Radek Male 6/3/1975 Green\n"

    ]
    for i, expected_output in enumerate(expected_outputs):
        mocker.patch(
            "sys.argv",
            [
                os.getcwd(),
                "./testing/pipe.txt",
                i + 1

            ]
        )
        output = main()
        assert output == expected_output

def test_text_processor_end_to_end_comma_separator(mocker):
    """End to end test for each of the cases with a comma separator."""
    expected_outputs = [
        # Sort Female first, and then by last name ascending.
        "Kelly Sue Female 7/12/1959 Pink\nAbercrombie Neil Male 2/13/1943 Tan\nBishop Timothy Male 4/23/1967 Yellow\n",
        # Sort by birhtday accending and then by last name acending.
        "Abercrombie Neil Male 2/13/1943 Tan\nKelly Sue Female 7/12/1959 Pink\nBishop Timothy Male 4/23/1967 Yellow\n",
        # Sort by last name decending.
        "Kelly Sue Female 7/12/1959 Pink\nBishop Timothy Male 4/23/1967 Yellow\nAbercrombie Neil Male 2/13/1943 Tan\n"

    ]
    for i, expected_output in enumerate(expected_outputs):
        mocker.patch(
            "sys.argv",
            [
                os.getcwd(),
                "./testing/comma.txt",
                i + 1

            ]
        )
        output = main()
        assert output == expected_output

def test_text_processor_end_to_end_space_separator(mocker):
    """End to end test for each of the cases with a space separator."""
    expected_outputs = [
        # Sort Female first, and then by last name ascending.
        "Hingis Martina Female 4/2/1979 Green\nKournikova Anna Female 6/3/1975 Red\nSeles Monica Female 12/2/1973 Black\n",
        # Sort by birhtday accending and then by last name acending.
        "Seles Monica Female 12/2/1973 Black\nKournikova Anna Female 6/3/1975 Red\nHingis Martina Female 4/2/1979 Green\n",
        # Sort by last name decending.
        "Seles Monica Female 12/2/1973 Black\nKournikova Anna Female 6/3/1975 Red\nHingis Martina Female 4/2/1979 Green\n"

    ]
    for i, expected_output in enumerate(expected_outputs):
        mocker.patch(
            "sys.argv",
            [
                os.getcwd(),
                "./testing/space.txt",
                i + 1

            ]
        )
        output = main()
        assert output == expected_output

if __name__ == '__main__':
    pytest.main()