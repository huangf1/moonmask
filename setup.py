from distutils.core import setup

setup(
    name = 'moonmask',
    packages = ['moonmask'],
    version = '0.1',
    license='MIT',
    description = 'Gets moon visualizations courtesy of Ernie Wright and uses them for artistic collages',
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/moonmask',
    download_url = 'https://github.com/spacerest/moonmask/archive/v_01.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'PIL',
        'urllib'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers, Visual Artists, Anyone',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)