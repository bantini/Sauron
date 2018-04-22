from setuptools import setup

setup(name='Sauron',
      version='0.1',
      description='Monitoring tool for endpoints',
      url='https://github.com/bantini/Sauron',
      author='Nilayan B (bantini)',
      author_email='nilayan.nbinc@gmail.com',
      license='Apache Commons 2.0',
      packages=['sauron', 'sauron/machine_monitor', 'sauron/ping_monitor',
                'sauron/process_monitor'],
      install_requires=[
          'psutil',
          'requests'
          ],
      zip_safe=False)
