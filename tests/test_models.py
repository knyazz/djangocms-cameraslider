# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File

from cms.test_utils.testcases import CMSTestCase
from filer.models import Image as FilerImage

from djangocms_cameraslider.models import Slider, Slide


class SliderModelTestCase(CMSTestCase):
    def test_creating_new_slider(self):
        s = Slider.objects.create(name='test')

        all_sliders = Slider.objects.all()

        self.assertEqual(all_sliders.count(), 1)
        self.assertEqual(all_sliders[0], s)
        self.assertEqual(s.__str__(), s.name)


class SlideModelTestCase(CMSTestCase):
    def setUp(self):
        self.f = FilerImage.objects.create(
            original_filename='test',
            file=File(open('tests/media/avatar.png')))
        self.slide = Slide.objects.create(image=self.f)

    def test_creating_new_slide(self):
        s = self.slide

        all_slides = Slide.objects.all()

        self.assertEqual(all_slides.count(), 1)
        self.assertEqual(all_slides[0], s)
        self.assertEqual(s.__str__(), s.image.url)

        s.caption = 'test caption'
        self.assertEqual(s.__str__(), s.caption)
