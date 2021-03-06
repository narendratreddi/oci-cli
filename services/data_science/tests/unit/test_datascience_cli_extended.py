# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import re
import unittest
from tests import util


class TestDatascienceCLI(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_work_request_logs(self):
        result = util.invoke_command(['data-science', 'work-request'])
        assert 'list-work-request-logs' in result.output
        result = util.invoke_command(['data-science', 'work-request', 'list-work-request-logs'])
        assert 'Error: Missing option(s)' in result.output

    def test_create_notebook_session(self):
        result = util.invoke_command(['data-science', 'notebook-session', 'create'])
        assert '--configuration-details' in result.output

    def test_get_model_artifact_content(self):
        result = util.invoke_command(['data-science', 'model'])
        assert 'get-model-artifact-content' not in result.output

    def test_get_artifact_content(self):
        result = util.invoke_command(['data-science', 'model'])
        assert 'get-artifact-content' in result.output
        result = util.invoke_command(['data-science', 'model', 'get-artifact-content'])
        assert 'Error: Missing option(s)' in result.output
        assert '--file' in result.output
        assert '--model-id' in result.output

    def test_create_model_artifact_model_artifact(self):
        result = util.invoke_command(['data-science', 'model', 'create-model-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--model-artifact' not in tokens

    def test_create_model_artifact_model_artifact_file(self):
        result = util.invoke_command(['data-science', 'model', 'create-model-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--model-artifact-file' in tokens
