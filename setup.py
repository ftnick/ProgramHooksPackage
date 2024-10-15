from setuptools import setup, find_packages

setup(
    name='ProgramHooks',
    version='v1.0',
    description='A modular Python framework for managing lifecycle hooks in applications. Easily register and execute pre-defined hooks (pre-init, post-init, pre-runtime, post-runtime) from external plugins, enabling flexible and extensible application design. Supports dynamic plugin loading and argument passing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='@ftnick',
    author_email='nicksynthex@gmail.com',
    url='https://github.com/ftnick/ProgramHooksPackage',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
