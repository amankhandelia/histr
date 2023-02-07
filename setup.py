from setuptools import Extension, find_packages, setup


with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="histr",
        version="0.1.0",
        description="One stop solution for text preprocessing on devanagari text",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Aman Khandelia",
        author_email="opensourceaman@gmail.com",
        url="https://github.com/amankhandelia/histr",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        python_requires=">3.5",
    )
