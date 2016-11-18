from subprocess import call
import subprocess


with open("/home/denis/credentials/ceph_creds_paths") as f:
    CLIENT, POOL, KEYRING, CONFIG = (string.strip() for string in f)


RDB = "rbd -n {} " \
      "--keyring={} " \
      "-c {}".format(CLIENT, KEYRING, CONFIG).split()


def _get_image_list():
    cmd = "ls {}".format(POOL).split()
    output = subprocess.check_output(RDB + cmd)
    return output.split()


def list_images():
    images = _get_image_list()
    for image in images:
        print image


def remove_image(image_name):
    cmd = "rm {}".format(_full_image_name(image_name)).split()
    call(RDB + cmd)


def remove_all_images():
    images = _get_image_list()
    for image in images:
        remove_image(image)


def _full_image_name(name):
    return "{}/{}".format(POOL, name)