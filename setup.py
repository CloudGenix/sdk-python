from setuptools import setup

setup(name='cloudgenix',
      version='4.5.7b1',
      description='Python2 and Python3 SDK for the CloudGenix AppFabric',
      url='https://github.com/CloudGenix/sdk-python',
      author='CloudGenix Developer Support',
      author_email='developers@cloudgenix.com',
      license='MIT',
      install_requires=[
            'requests[security] >= 2.18.4'
      ],
      packages=['cloudgenix'],
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
      ]
      )
