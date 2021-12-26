import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN"
USER_NAME = "jaiyesh"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.1.0",
    author=USER_NAME,
    author_email="jaiyesh0002@gmail.com",
    description="A ANN Implementation Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaiyesh/ANN_implementation",
    project_urls={
        "Bug Tracker": "https://github.com/jaiyesh/ANN_implementation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        'tensorflow',
        "pandas",
        "matplotlib",
        "seaborn"

    ]
)