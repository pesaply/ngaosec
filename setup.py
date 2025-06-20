from setuptools import setup, find_packages

setup(
    name="ngaosec",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tkinter',  # Usually included with Python
    ],
    entry_points={
        'console_scripts': [
            'ngaosec=ngaosec.app:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A local browser-based security application with GUI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ngaosec",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
