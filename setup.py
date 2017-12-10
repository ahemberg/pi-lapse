from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pi_lapse',
      version='0.1',
      description='Scripts to gather and handle time lapses',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.2',
        'Topic :: Image Processing :: Imaging',
      ],
      keywords='rpi pi-camera timelapse',
      url='https://github.com/ahemberg/pi-lapse',
      author='Alexander Hemberg',
      author_email='alexander.hemberg@gmail.com',
      license='MIT',
      packages=['pi_lapse'],
      install_requires=[
          'picamera'
      ],
      scripts=['bin/take-long-exposure', 'bin/take_image'],
      include_package_data=True,
      zip_safe=False)