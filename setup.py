from setuptools import find_packages, setup

setup(
    name='django-safe-filefield-new',
    version='0.4.1',
    url='https://github.com/beckedorf/django-safe-filefield-new',
    description='Secure file field, which allows you to '
                'restrict uploaded file extensions.',
    keywords=['django', 'filefield', 'model-field', 'form-field'],

    long_description=open('README.rst', 'r').read(),
    long_description_content_type='text/x-rst',

    author='Vladislav Bakin',
    author_email='mixkorshun@gmail.com',
    maintainer='Janis Beckedorf',
    maintainer_email='mail@janisbeckedorf.de',

    license='MIT',

    install_requires=[
        'django',
        'python-magic',
        'clamd',
    ],

    packages=find_packages(exclude=['*.tests.*', '*.tests']),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Topic :: Security',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
