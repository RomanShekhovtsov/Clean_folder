from setuptools import setup

setup(
    name="Cleaning",
    version="0.0.1",
    description="Cleaning folders",
    author="Shekhovtsov Roman",
    author_email="roman13sheh@gmail.com",
    url="https://github.com/RomanShekhovtsov",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows 10 Home"
    ],
    packages=["Cleaning"],  # Добавьте здесь название пакета
    entry_points={
        "console_scripts": [
            "clean=Cleaning.clean:run"
        ]
    }
)
