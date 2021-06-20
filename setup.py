import setuptools

setuptools.setup(
    name="easyMail",
    version="0.1",
    author="harshit allumolu",
    author_email="allumoluharshit@gmail.com",
    description="EasyMail",
    long_description="An easy to use python package for sending personalized emails with user-specific data facilitated with generation of email body.",
    url="https://github.com/harshit-allumolu/EasyMail.git",
    packages=setuptools.find_packages(),
    install_requires=["et-xmlfile","numpy","openpyxl","pandas","python-dateutil","pytz","six","xlrd"],
    classifiers=[
        "Programming Language :: Python :: 3.9.5",
        "Operating System :: OS Independent",
    ],
)