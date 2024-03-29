import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-cov',
    'pytest-django'
]

setuptools.setup(
    name='djangocms-cameraslider',
    version='1.0.1',
    license='MIT License',
    description='A Django CMS image slider plugin that uses Camera Slider/Slideshow.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/knyazz/djangocms-cameraslider',
    author='Evgenii Smirnov',
    author_email='knyazz@gmail.com',
    keywords='djangocms-cameraslider, cameraslider, django, image-slider',
    packages=[
        'djangocms_cameraslider',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django-cms>=3.9.0',
        'django-mptt==0.13.4',
        'django-filer',
        'easy-thumbnails',
        'djangocms-text-ckeditor',
    ],
    setup_requires=['pytest-runner'],
    tests_require=TEST_REQUIREMENTS
)
