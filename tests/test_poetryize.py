import os

from typer.testing import CliRunner

from poetryize.poetryize import app

runner = CliRunner()


def test_poetryize_with_valid_file():
    """
    tests if the CLI command works with a valid requirements file
    """
    with runner.isolated_filesystem():
        # Create a sample requirements.txt file
        requirements_file_content = "requests==2.25.1\nflask==1.1.2"
        with open("requirements.txt", "w") as requirements_file:
            requirements_file.write(requirements_file_content)

        # Run the CLI command
        result = runner.invoke(app, ["requirements.txt"])

        # Check if the command was successful
        assert result.exit_code == 0

        # Check if the stdout contains the expected lines
        assert "Found Poetry-compatible dependencies:" in result.stdout
        assert "requests:2.25.1" in result.stdout
        assert "flask:1.1.2" in result.stdout

        # Check if the pyproject.toml file was created
        assert os.path.exists("pyproject.toml")


def test_poetryize_with_nonexistent_file():
    """
    tests if the CLI command exits with an error when a non-existent file is specified
    """  # noqa
    with runner.isolated_filesystem():
        # Run the CLI command with a non-existent file
        result = runner.invoke(app, ["nonexistent_file.txt"])

        # Check if the command exits with an error
        assert result.exit_code != 0

        # Check if the error message is displayed
        assert (
            "Error: The specified requirements file 'nonexistent_file.txt' does not exist or no 'nonexistent_file.txt' found in current path"  # noqa
            in result.stdout
        )


def test_poetryize_without_requirements_file():
    """
    tests if the CLI command works with requirement file in path without specifying a requirements file # noqa
    """
    with runner.isolated_filesystem():
        requirements_file_content = "requests==2.25.1\nflask==1.1.2"
        with open("requirements.txt", "w") as requirements_file:
            requirements_file.write(requirements_file_content)

        # Run the CLI command without specifying a requirements file
        result = runner.invoke(app, [])

        # Check if the command was successful
        assert result.exit_code == 0

        # Check if the stdout contains the expected lines
        assert "Found Poetry-compatible dependencies:" in result.stdout
        assert "requests:2.25.1" in result.stdout
        assert "flask:1.1.2" in result.stdout

        # Check if the pyproject.toml file was created
        assert os.path.exists("pyproject.toml")


def test_poetryize_with_invalid_file():
    """
    tests if the CLI command exits with an error when an invalid requirements file is specified
    """  # noqa
    with runner.isolated_filesystem():
        # Create a sample requirements.txt file
        requirements_file_content = (
            "requests==2.25.1\nflask==1.1.2\nthoth is welcome"  # noqa
        )
        with open("requirements.txt", "w") as requirements_file:
            requirements_file.write(requirements_file_content)

        # Run the CLI command
        result = runner.invoke(app, ["requirements.txt"])

        # Check if the command was successful
        assert result.exit_code != 0

        # Check if the stdout contains the expected lines
        assert (
            "❌ Error 😥: There seems to be a problem with the 'requirements.txt' provided"  # noqa
            in result.stdout
        )
