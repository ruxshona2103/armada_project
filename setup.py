from setuptools import setup, find_packages

setup(
    name='armada_project',
    version='0.0.1',
    description='ERPNext app for Armada company',
    author='Ruxshona',
    author_email='your_email@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
