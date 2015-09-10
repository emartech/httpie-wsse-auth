from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-wsse-auth',
    description='WsseAuth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.1.1',
    author='Andras Barthazi',
    author_email='andras@barthazi.hu',
    license='MIT',
    url='https://github.com/emartech/httpie-wsse-auth',
    download_url='https://github.com/emartech/httpie-wsse-auth',
    py_modules=['httpie_wsse_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_wsse_auth = httpie_wsse_auth:WsseAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
