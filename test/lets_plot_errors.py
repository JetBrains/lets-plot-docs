#!/usr/bin/env python

import warnings

def check_lets_plot_message_errors(parser, parser_type, source, warn_only=True):
    message = "Plot displaying error in {0}".format(source)
    errors_count = 0
    if parser_type == 'driver':
        errors_count = len(parser.find_elements_by_css_selector('.lets-plot-message-error'))
    elif parser_type == 'soup':
        errors_count = len([s for s in parser.select('script[data-lets-plot-script="plot"]') if "__error_message" in str(s)])
    else:
        raise ValueError("Bad parser type: {0}".format(parser_type))
    if warn_only:
        if errors_count > 0:
            warnings.warn(UserWarning(message))
    else:
        assert errors_count == 0, message