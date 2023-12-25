# import module
import os
import re

import typer

from typing import Annotated  # noqa: TYP001 isort: skip


app = typer.Typer()


@app.command()
def poetry(
    requirement_file: Annotated[
        str, typer.Argument(help="Enter the requirements file name or path: ")
    ] = "requirements.txt"
):
    """
    Switch From Using Pip to Poetry package manager on your project, Easily
    This CLI app converts Pip requirements to Poetry projects.
    It parses a Pip requirements file and generates the corresponding
    `pyproject.toml` file for Poetry. The resulting Poetry project file
    includes the necessary dependencies and metadata.
    """
    try:
        if not os.path.exists(requirement_file):
            typer.echo(
                f"Error: The specified requirements file '{requirement_file}' does not exist or no '{requirement_file}' found in current path"  # noqa
            )
            raise typer.Abort()

        # Initialize Poetry if it doesn't yet have a pyproject.toml file
        if not os.path.exists("./pyproject.toml"):
            os.system("poetry init")

        with open(requirement_file, encoding="utf-8") as fh:
            requirements = fh.read()

        no_comments = re.sub(
            "^#.*$", "", requirements, 0, re.IGNORECASE | re.MULTILINE
        )  # noqa
        bare_requirements = re.sub(
            "\n+", "\n", no_comments, 0, re.IGNORECASE | re.MULTILINE
        ).strip()

        pip_poetry_map = {">": "^", "=": ""}

        req_list = list()
        for line in bare_requirements.splitlines():
            try:
                package, match, version = re.sub(
                    r"^(.*?)\s*([~>=<])=\s*v?([0-9\.\*]+)",
                    r"\1,\2,\3",
                    line,
                    0,
                    re.IGNORECASE | re.MULTILINE,
                ).split(",")
                try:
                    poetry_match = pip_poetry_map.get(match, match)
                except KeyError:
                    poetry_match = match
                poetry_line = f"{package}:{poetry_match}{version}"
                req_list.append(poetry_line)
            except ValueError:
                if len(line.split(" ")) == 1:
                    req_list.append(line)
                else:
                    typer.echo(
                        f"Skipping Dependency There seems to be a problem with the '{line}' dependency provided."  # noqa
                    )

        for req in req_list:
            typer.echo(req)
            os.system(f"poetry add {req}")

        typer.echo("Done! 🎉")
    except ValueError:
        typer.echo(
            f"❌ Error 😥: There seems to be a problem with the '{requirement_file}' provided."  # noqa
        )
        raise typer.Abort()  # noqa


if __name__ == "__main__":
    app()
