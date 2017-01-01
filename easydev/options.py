import argparse


__all__ = ["SmartFormatter"]


class SmartFormatter(argparse.HelpFormatter):
    """Formatter to be used with argparse ArgumentParser"""
    def _split_lines(self, text, width):
        if text.startswith('FORMAT|'):
            return text[7:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)
