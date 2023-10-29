# TvOverlay Python Client for Android/Google TV

[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](.github/LICENSE.md)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]
[![Quality Gate Status][sonarcloud-shield]][sonarcloud]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Sponsor Hareesh via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Hareesh on Patreon][patreon-shield]][patreon]

Asynchronous Python client for TvOverlay to send notifications to Android/Google TV.

## About

This package allows you to control an TvOverlay notifications. It is mainly created to allow third-party programs to automate
the TvOverlay notifications.

## Installation

```bash
pip install tvoverlay
```

## Usage

```python
import asyncio

from tvoverlay import ConnectError, Notifications

HOST = "10.10.10.150"

async def main() -> None:
    """Run the example script."""
    notifier = Notifications(HOST)

    # validate connection
    try:
        response = await notifier.async_connect()
        print(response)
    except ConnectError:
        print("Connect Error")

    # send notification
    print(await notifier.async_send("This is a notification message"))


if __name__ == "__main__":
    asyncio.run(main())
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality.

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The easiest way to start, is by opening a CodeSpace here on GitHub, or by using
the [Dev Container][devcontainer] feature of Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project is fully managed using the [Poetry][poetry] dependency
manager. But also relies on the use of NodeJS for certain checks during
development.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]
- NodeJS 18+ (including NPM)

To install all packages, including all development requirements:

```bash
npm install
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## Authors & contributors

The original setup of this repository is by [Hareesh M U][hareeshmu].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2023 Hareesh M U

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[build-shield]: https://github.com/hareeshmu/pytvoverlay/actions/workflows/tests.yaml/badge.svg
[build]: https://github.com/hareeshmu/pytvoverlay/actions/workflows/tests.yaml
[codecov-shield]: https://codecov.io/gh/hareeshmu/pytvoverlay/branch/main/graph/badge.svg
[codecov]: https://codecov.io/gh/hareeshmu/pytvoverlay
[contributors]: https://github.com/hareeshmu/pytvoverlay/graphs/contributors
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/hareeshmu/pytvoverlay
[hareeshmu]: https://github.com/hareeshmu
[github-sponsors-shield]: https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23db61a2.svg?&logo=github&logoColor=white&labelColor=181717&style=flat-square
[github-sponsors]: https://github.com/sponsors/hareeshmu
[license-shield]: https://img.shields.io/github/license/hareeshmu/pytvoverlay.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[patreon-shield]: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Dhareeshmu%26type%3Dpatrons&style=flat
[patreon]: https://www.patreon.com/hareeshmu
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[pypi]: https://pypi.org/project/tvoverlay/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/tvoverlay
[releases-shield]: https://img.shields.io/github/release/hareeshmu/pytvoverlay.svg
[releases]: https://github.com/hareeshmu/pytvoverlay/releases
[semver]: http://semver.org/spec/v2.0.0.html
[sonarcloud-shield]: https://sonarcloud.io/api/project_badges/measure?project=hareeshmu_pytvoverlay&metric=alert_status
[sonarcloud]: https://sonarcloud.io/summary/new_code?id=hareeshmu_tvoverlay
