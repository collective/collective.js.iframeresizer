# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.testing import z2

import collective.js.iframeresizer


COLLECTIVE_JS_IFRAMERESIZER_FIXTURE = PloneWithPackageLayer(
    zcml_package=collective.js.iframeresizer,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.js.iframeresizer:testing',
    name='CollectiveJsIframeresizerLayer',
    additional_z2_products=()
)


COLLECTIVE_JS_IFRAMERESIZER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_JS_IFRAMERESIZER_FIXTURE,),
    name='CollectiveJsIframeresizerLayer:IntegrationTesting'
)


COLLECTIVE_JS_IFRAMERESIZER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_JS_IFRAMERESIZER_FIXTURE,),
    name='CollectiveJsIframeresizerLayer:FunctionalTesting'
)


COLLECTIVE_JS_IFRAMERESIZER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_JS_IFRAMERESIZER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveJsIframeresizerLayer:AcceptanceTesting'
)
