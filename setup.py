from setuptools import setup, find_packages

setup(
    name='student-management-system11',
    version='0.1.9',
    author='Anna Adamiak',
    author_email='anna.adamiak@edu.uekat.pl',
    description='A simple student management system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Anulka677/CI',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
