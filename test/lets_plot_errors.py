#!/usr/bin/env python

import warnings

from selenium.webdriver.common.by import By

def check_lets_plot_message_errors(parser, parser_type, source, warn_only=True):
    message = "Plot displaying error in {0}".format(source)
    errors_count = 0
    if parser_type == 'driver':
        errors_count = len(parser.find_elements(By.CSS_SELECTOR, ".lets-plot-message-error"))
    elif parser_type == 'soup':
        errors_count = len([s for s in parser.select('script[data-lets-plot-script="plot"]') if "__error_message" in str(s)])
    else:
        raise ValueError("Bad parser type: {0}".format(parser_type))
    if warn_only:
        if errors_count > 0:
            warnings.warn(UserWarning(message))
    else:
        assert errors_count == 0, message

def check_warnings(parser, parser_type, source):
    warning_messages = []
    if parser_type == 'driver':
        warning_messages = [element.text.strip()
                    for element in parser.find_elements(By.XPATH, "//pre[contains(text(), 'Warning')]")
                    if 'jp-OutputArea-output' in element.find_element(By.XPATH, "..").get_attribute('class')]
    elif parser_type == 'soup':
        warning_messages = [element.text.strip()
                    for element in parser.select("div:-soup-contains('Warning')")
                    if 'jp-OutputArea-output' in element['class']]
    else:
        raise ValueError("Bad parser type: {0}".format(parser_type))
    for message in warning_messages:
        warnings.warn(UserWarning('Warning in {0} in output cell: "{1}"'.format(source, message)))