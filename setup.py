from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='cloudgenix',
      version='6.4.1b1',
      description='Python3 SDK for the CloudGenix AppFabric',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/CloudGenix/sdk-python',
      author='CloudGenix Developer Support',
      author_email='developers@cloudgenix.com',
      license='MIT',
      install_requires=[
            'requests',
            'websockets >= 8.1; python_version > "3.6"',
            'urllib3 >= 2.0.0'
      ],
      packages=['cloudgenix'],
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
      ]
      )
