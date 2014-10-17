import sys
import tarfile
import os
import urllib2
import time
import shutil
import subprocess

def download_geos(version):
    """Download the approprate version of the GEOS source from the official
    download mirror.

    version - the version of GEOS to download.  Must be a string in the form
        1.1.1

    Returns the absolute path to the downloaded tar.bz2 file."""

    # parse out the version info
    major, minor, release = version_info(version)

    geos_download_uri = 'http://download.osgeo.org/geos/'
    if minor >= 10:
        geos_download_uri += version + '/'

    local_gzip = 'geos-%s.tar.bz2' % version
    geos_download_uri += local_gzip
    print geos_download_uri

    print 'downloading ...'
    u = urllib2.urlopen(geos_download_uri)
    localFile = open(local_gzip, 'w')
    localFile.write(u.read())
    localFile.close()

    return os.path.abspath(local_gzip)


if __name__ == '__main__':
    start_time = time.time()
    version_info = lambda v: map(lambda x: int(x), v.split('.'))

    # if the user provided an argument and it's a file, use that.
    try:
        source_filepath = sys.argv[1]
    except IndexError:
        source_filepath = ''

    if os.path.exists(source_filepath):
        print 'Building from source archive %s' % source_filepath
        local_gzip = source_filepath
    else:
        geos_version = '3.4.2'
        local_gzip = download_geos(geos_version)

    geos_dir = local_gzip.replace('.tar.bz2', '')
    if os.path.exists(geos_dir):
        print 'removing %s' % geos_dir
        shutil.rmtree(geos_dir)

    print 'extracting', local_gzip
    tfile = tarfile.open(local_gzip, 'r:bz2')
    tfile.extractall('.')

    os.chdir(geos_dir)
    build_dir = os.path.join(os.getcwd(), '_built')
    subprocess.call('./configure --prefix=%s' % build_dir, shell=True)
    subprocess.call('make install', shell=True)

    end_time = time.time()
    print 'All operations took %ss' % ((end_time - start_time))
