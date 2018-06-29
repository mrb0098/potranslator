#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `potranslator` package."""

import pytest

from click.testing import CliRunner

from potranslator import potranslator
from potranslator import cli


class TestPoTranslator:
    translator = potranslator.PoTranslator(pot_dir='./tests/test_data/pot_files', locale_dir='./tests/test_data/locale')

    def test_translate(self):
        test_file = './tests/test_data/empty_test.po'
        with pytest.raises(ValueError):
            failed_translation = self.translator.translate(test_file, 'sp')
        translation = self.translator.translate(test_file, 'es')
        assert all([entry.msgstr != '' for entry in translation])
        assert translation[0].msgstr == 'Créditos'
        pass


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'potranslator.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
