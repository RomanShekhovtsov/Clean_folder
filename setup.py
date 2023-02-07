from setuptools import  setup, find_namespace_packages

setup (
    name = "Cleaning"
    version = "0.0.1"
    description = "Cleaning folders"
    author = "Shekhovtsov Roman"
    author_email = roman13sheh@gmail.com
    url = "https://github.com/RomanShekhovtsov"
    license = "MIT"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10 Home"]
    packages = find_namespace_packages(),
    data_files= [("Cleaning"),["Cleaning/clean.py"])],
    include_package_data = True,
    entry_point = {"console_scripts": ["clean=Cleaning.clean:run"]}
)