from setuptools import setup, find_packages
from pathlib import Path

# Read requirements.txt
def read_requirements():
    requirements_path = Path(__file__).parent / "requirements.txt"
    with open(requirements_path) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="ml-project",
    version="0.1.0",
    description="End-to-end machine learning project",
    author="Udith S Nair",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements(),
)
