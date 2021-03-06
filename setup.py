import sys

from setuptools import setup, find_packages

version = '3.2.3dev'

install_requires = [
    'zope.tal >= 3.5.2',
    'zope.interface >= 3.3',
    'zope.i18nmessageid >= 3.3',
    'plone.i18n',
    'ordereddict',
    ]

if sys.version_info < (2, 5):
    install_requires.append('elementtree')

setup(name='i18ndude',
      version=version,
      description="i18ndude performs various tasks related to ZPT's, Python Scripts and i18n.",
      long_description=(open("README.txt").read() + "\n" +
                        open("CHANGES.rst").read()),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Plone',
          'Framework :: Zope2',
          'Framework :: Zope3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities',
          ],
      keywords='Plone i18n zpt',
      author='Daniel Nouri',
      author_email='plone-i18n@lists.sourceforge.net',
      maintainer='Vincent Fretin',
      maintainer_email='vincent.fretin@gmail.com',
      url='https://github.com/collective/i18ndude',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      [console_scripts]
      i18ndude=i18ndude.script:main
      """,
      )
