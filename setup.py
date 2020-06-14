import os
import setuptools

this_dir = os.path.dirname(__file__)
with open(os.path.join(this_dir, 'README.md'), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="algerian-mobile-phone-number",
    version="0.0.1",
    author="Mohammed Amine BOURAS",
    author_email="mohamine19@gmail.com",
    description="Algerian mobile phone number package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamine18/algerian-mobile-phone-number",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)