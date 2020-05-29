import os

from distutils.core import setup


def find_packages(path, base=None):

    packages = []

    for root, _, files in os.walk(path):
        if "__init__.py" in files:
            if base is not None:
                root = root.replace(path, base)
            pkg = root.replace(os.sep, ".")
            packages.append(pkg)

    return packages

#################################
# Packages section
#################################


package_info = {}
exec(open("src/__pkginfo__.py").read(), {}, package_info)

package = find_packages(path="src", base="md_dihedrals")

#################################
# The setup section
#################################

setup(name="md_dihedrals",
      version=package_info["__version__"],
      description=package_info["__description__"],
      long_description=package_info["__long_description__"],
      author=package_info["__author__"],
      author_email=package_info["__author_email__"],
      maintainer=package_info["__maintainer__"],
      maintainer_email=package_info["__maintainer_email__"],
      license=package_info["__license__"],
      packages=package,
      package_dir={"md_dihedrals": "src"},
      platforms=['Unix', 'Windows'])
