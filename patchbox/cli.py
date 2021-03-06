import click
from patchbox.utils import PatchboxHomeGroup, PatchboxChoice, do_group_menu

click.Choice = PatchboxChoice


@click.command(cls=PatchboxHomeGroup, context_settings=dict(help_option_names=['--help']))
@click.option('--verbose', is_flag=True, help='Enables verbose mode.')
@click.option('--interactive', is_flag=True, help='Enables interactive mode.')
@click.version_option("1.01")
@click.pass_context
def cli(ctx, verbose, interactive):
    """Patchbox Configuration Utility"""
    if ctx.invoked_subcommand is None or interactive:
        ctx.meta['interactive'] = True
    do_group_menu(ctx, cancel='Exit')

if __name__ == '__main__':
	cli()
