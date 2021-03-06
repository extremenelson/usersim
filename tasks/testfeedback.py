# Copyright 2017 Carnegie Mellon University. See LICENSE.md file for terms.

import tasks.test


class TestFeedback(tasks.test.Test):
    """ Task for testing an exception raised from the __call__ method.
    """
    def __call__(self):
        super().__call__()
        raise Exception('Test exception raised.')
