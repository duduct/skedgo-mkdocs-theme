from setuptools import setup, find_packages

setup(
    name="skedgo_mkdocs_theme",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mkdocs>=1.0"
    ],
    entry_points={
        'mkdocs.themes': [
            'skedgo = skedgo_mkdocs_theme',
        ]
    },
)