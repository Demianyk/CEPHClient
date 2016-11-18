import click
import lib.utils as utils


def remove_all_images(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    utils.remove_all_images()


@click.group()
def client():
    pass


@client.command(name="remove-image")
@click.option('--all', help="remove all images from the pool", is_flag=True,
              callback=remove_all_images, expose_value=False)
@click.argument('image-name', required=False)
def remove_image(image_name=False):
    utils.remove_image(image_name)


@client.command(name="list-images")
def list_images():
    utils.list_images()


def main():
    client()


if __name__ == '__main__':
    main()
