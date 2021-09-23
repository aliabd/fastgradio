try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='fastgradio',
    version='0.1',
    license='MIT',
    include_package_data=True,
    description='Python library for easily creating Gradio demos from Fastai learners.',
    author="Ali Abdalla",
    author_email='ali.si3luwa@gmail.com',
    packages=['fastgradio'],
    url='https://github.com/aliabd/fastgradio',
    keywords=['machine learning', 'fastai', 'gradio', 'demo', 'interface', 'visualization', 'reproducibility'],
    install_requires=[
          'gradio',
          'fastai'
      ],

)