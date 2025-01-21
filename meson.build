project('vial_serialization', 'c')
libsafe32 = subproject('safe32')
libsafe32_dep = libsafe32.get_variable('project_dep')

py = import('python').find_installation('python3.11', pure: true)
py_install_dir = py.get_install_dir()

# fix homebrew python fuckery
# https://github.com/mesonbuild/meson/pull/12375
# https://github.com/mesonbuild/meson/issues/12113
# https://github.com/mesonbuild/meson/issues/10459
# https://github.com/orgs/Homebrew/discussions/4858
# https://github.com/Homebrew/homebrew-core/blob/965f025f9f2858e0716f7569219460c19fc146bf/Formula/p/python%403.11.rb#L67
if py_install_dir.startswith('/opt/homebrew/opt/homebrew')
  message('fixing broken homebrew python site-packages install path')
  py_install_dir = py_install_dir.replace('/opt/homebrew/opt/homebrew', '/opt/homebrew')
elif py_install_dir.startswith('/usr/local/usr/local')
  message('fixing broken homebrew python site-packages install path')
  py_install_dir = py_install_dir.replace('/usr/local/usr/local', '/usr/local')
endif

safe32_module = py.extension_module(
    'safe32',
    'src/safe32_module/safe32.c',
    dependencies: libsafe32_dep,
    install: true,
    install_dir: py_install_dir
)
