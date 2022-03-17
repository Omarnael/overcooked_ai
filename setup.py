#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='hacktrick_ai',
      version='1.1.0',
      description='Cooperative multi-agent environment based on Hacktrick',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages('src'),
      keywords=['Hacktrick', 'AI', 'Reinforcement Learning'],
      package_dir={"": "src"},
      package_data={
        'hacktrick_ai_py' : [
          'data/layouts/*.layout', 'data/planners/*.py', 'data/human_data/*.pickle',
          'data/graphics/*.png', 'data/graphics/*.json', 'data/fonts/*.ttf',
        ],
      },
      install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'gym',
        'ipython',
        'pygame',
        'ipywidgets'
      ]
    )
