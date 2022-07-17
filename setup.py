import setuptools

with open('README.md','r') as fh:
  long_description = fh.read()
  
setuptools.setup(
  name='simple_telebot',
  version='0.1.0',
  author='Mikko Sipola',
  author_email='mikko.sipola@uef.fi',
  description='Simple to use Telegram alarm bot',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/msipola/simple_telebot',
  packages=setuptools.find_packages(),
  install_requires=[
    'telepot',
    're'
  ],
)
