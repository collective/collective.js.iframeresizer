# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.js.iframeresizer.testing import COLLECTIVE_JS_IFRAMERESIZER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.js.iframeresizer is properly installed."""

    layer = COLLECTIVE_JS_IFRAMERESIZER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.js.iframeresizer is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.js.iframeresizer'))

    def test_uninstall(self):
        """Test if collective.js.iframeresizer is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.js.iframeresizer'])
        self.assertFalse(self.installer.isProductInstalled('collective.js.iframeresizer'))

    def test_browserlayer(self):
        """Test that ICollectiveJsIframeresizerLayer is registered."""
        from collective.js.iframeresizer.interfaces import ICollectiveJsIframeresizerLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveJsIframeresizerLayer, utils.registered_layers())
