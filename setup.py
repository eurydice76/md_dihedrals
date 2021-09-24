import fnmatch
import glob
import os

from setuptools import find_packages, setup

#################################
# Packages section
#################################

package_info = {}
exec(open("src/md_dihedrals/__pkginfo__.py").read(), {}, package_info)

#################################
# Scripts section
#################################

scripts = glob.glob(os.path.join('scripts','*'))

#################################
# The setup section
#################################

with open('requirements.txt','r') as fin:
	deps = fin.readlines()

setup(name="md_dihedrals",
      version=package_info["__version__"],
      description=package_info["__description__"],
      long_description=package_info["__long_description__"],
      author=package_info["__author__"],
      author_email=package_info["__author_email__"],
      maintainer=package_info["__maintainer__"],
      maintainer_email=package_info["__maintainer_email__"],
      license=package_info["__license__"],
      install_requires=deps,
      packages=find_packages('src'),
      include_package_data=True,
      package_dir={'': 'src'},
      platforms=['Unix', 'Windows'],
      scripts=scripts)
