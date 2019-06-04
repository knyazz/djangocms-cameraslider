# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder
from cms.toolbar.utils import get_toolbar_from_request

from djangocms_cameraslider.cms_plugins import SliderPlugin


class SliderPluginTestCase(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SliderPlugin,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('instance', context)

    def _test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SliderPlugin,
            'en',
        )
        toolbar = get_toolbar_from_request({})
        renderer = toolbar.get_content_renderer()
        html = renderer.render_plugin(
            instance=model_instance,
            context={},
            editable=renderer._placeholders_are_editable,
        )
        self.assertTrue(html.find('class="cameraslider">') > -1)
