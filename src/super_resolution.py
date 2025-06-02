import click

from src.super_resolution.base import super_resolution


@click.command(
    help="Run EDSR super-resolution on a single image. SRC_FILEPATH: Path to input image. "
         "DST_FILEPATH: Path where the output image will be saved."
)
@click.argument('src_filepath', type=click.Path(exists=True))
@click.argument('dst_filepath', type=click.Path())
@click.option('--scale', default=4, type=click.Choice(['2', '3', '4']), help='Upscale factor (2, 3, or 4)')
def super_resolution_cli(src_filepath: str, dst_filepath: str, scale: str = 4) -> None:

    super_resolution(src_filepath, dst_filepath, scale=int(scale))


if __name__ == '__main__':
    super_resolution_cli()