from setuptools import setup, find_packages

setup(
    name="null-detector",
    version="1.0.0",
    description="A Python package for detecting and reporting null values in pandas DataFrames",
    author="Data Engineer",
    author_email="data@example.com",
    url="https://github.com/yourusername/null-detector",
    py_modules=["detect_null_values"],
    install_requires=[
        "pandas>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
