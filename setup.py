from setuptools import setup, find_packages

setup(
    name="skedgo-mkdocs-theme",
    version="1.0.0",
    description="SkedGo MKDocs theme for the developer page",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Duy Luong",
    author_email="luongducduy.cantho@gmail.com",
    url="https://github.com/duduct/skedgo-mkdocs-theme",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mkdocs>=1.1.0",
        "jinja2>=2.11.1"
    ],
    python_requires=">=3.6",
    entry_points={
        "mkdocs.themes": [
            "skedgo = skedgo_mkdocs_theme",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)