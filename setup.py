from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import numpy
from distutils import sysconfig
#import numpy.distutils.intelccompiler
import numpy.distutils.ccompiler
import platform as plt

if(plt.system() == 'Darwin'):
    root_dir = '/opt/local/'
    CC = 'clang'
    CXX= 'clang++'
    link_opts = ["-stdlib=libc++","-bundle","-undefined","dynamic_lookup"]
else:
    root_dir = '/usr/'
    CC = 'gcc'
    CXX= 'g++'
    link_opts = ["-shared"]

os.environ["CC"] = CC
os.environ["CXX"] = CXX

from distutils import sysconfig
sysconfig.get_config_vars()['CFLAGS'] = ''
sysconfig.get_config_vars()['OPT'] = ''
sysconfig.get_config_vars()['PY_CFLAGS'] = ''
sysconfig.get_config_vars()['PY_CORE_CFLAGS'] = ''
sysconfig.get_config_vars()['CC'] =  CC
sysconfig.get_config_vars()['CXX'] = CXX
sysconfig.get_config_vars()['BASECFLAGS'] = ''
sysconfig.get_config_vars()['CCSHARED'] = ''
sysconfig.get_config_vars()['LDSHARED'] = CC
sysconfig.get_config_vars()['CPP'] = CXX
sysconfig.get_config_vars()['CPPFLAGS'] = ''
sysconfig.get_config_vars()['BLDSHARED'] = ''
sysconfig.get_config_vars()['CONFIGURE_LDFLAGS'] = ''
sysconfig.get_config_vars()['LDFLAGS'] = ''
sysconfig.get_config_vars()['PY_LDFLAGS'] = ''



comp_flags=['-O3','-std=c++11','-march=native','-fPIC']#,
extension = Extension("spatWFA",
                      sources=["WFA.pyx"], 
                      include_dirs=["./", root_dir+"/include/",numpy.get_include()],
                      language="c++",
                      extra_compile_args=comp_flags,
                      extra_link_args=link_opts,
                      library_dirs=[root_dir+'/lib/','./'],
                      libraries=[])

extension.cython_directives = {'language_level': "3"}

setup(
    name = 'WFA Spat',
    version = '1.0',
    author = 'Jaime de la Cruz Rodriguez & Roberta Morosin (ISP-SU 2020)',
    ext_modules=[extension],
    cmdclass = {'build_ext': build_ext}
)

