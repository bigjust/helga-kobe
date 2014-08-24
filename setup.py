from setuptools import setup, find_packages

version = '1.0.0'

setup(name="helga-kobe",
      version=version,
      description=('Kobe!'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot kobe',
      author='justin caratzas',
      author_email='bigjust@lambdaphil.es',
      url='https://github.com/bigjust/helga-kobe',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-kobe'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'kobe= helga_kobe:kobe',
          ],
      ),
)
