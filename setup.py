import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock_picker",
    version="0.0.1",
    author="Chirag Chadha",
    author_email="chiragchadhairl@gmail.com",
    description="Stock picker table",
    packages=setuptools.find_packages(),
    install_requires=["pandas",
                      "requests",
                      "pyyaml"]
)
