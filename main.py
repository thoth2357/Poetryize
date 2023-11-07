# import module

import os
import re

import typer


def poetry_convert(
    source_file: str = typer.Argument(
        "./requirements.txt", help="Enter the source file name or path: "
    )
):
    if not os.path.exists(source_file):
        typer.echo(
            f"Error: The specified requirements file '{source_file}' "
            "does not exist."  # type: ignore
        )
        raise typer.Abort()

    # We don't need to keep track of this file
    with open(".gitignore", "a", encoding="utf-8") as fh:
        fh.write("\npoetry-convert.py\n")

    # Initialize Poetry if it doesn't yet have a pyproject.toml file
    if not os.path.exists("./pyproject.toml"):
        os.system("poetry init")

    with open(source_file, encoding="utf-8") as fh:
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

    typer.echo("Found Poetry-compatible dependencies:")
    for req in req_list:
        typer.echo(req)
        os.system(f"poetry add {req}")


if __name__ == "__main__":
    typer.run(poetry_convert)
