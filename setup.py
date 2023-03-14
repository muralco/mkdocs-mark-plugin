from setuptools import setup, find_packages

setup(
    name='mkdocs-mark-plugin',
    version='0.1.0',
    description='An MkDocs plugin',
    long_description='An MkDocs plugin that fixes links meant for https://github.com/kovetskiy/mark',
    keywords='mkdocs',
    url='https://github.com/muralco/mkdocs-mark-plugin',
    author='Roberto Alsina',
    author_email='ralsina@mural.co',
    license='MIT',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=1.2.3',
        'parse>=1.19.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'marklinks = mkdocs_mark_plugin.plugin:MarkLinksPlugin',
        ]
    }
)
