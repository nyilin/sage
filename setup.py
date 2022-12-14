import setuptools

setuptools.setup(
    name="sage-importance",
    version="0.0.4m",
    author="Ian Covert, Yilin Ning",
    author_email="ningyilinnyl@gmail.com",
    description="For calculating global feature importance using Shapley values.",
    long_description="""
        A slightly modified version of SAGE. See https://github.com/nyilin/sage.
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/iancovert/sage/",
    packages=['sage'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'tqdm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.6',
)
