# Building Steam Offline Client

This guide explains how to build and install the Steam Offline Client application.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Build Methods

### Method 1: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/irishbyblood/Steam-Offline-Client.git
cd Steam-Offline-Client
```

2. Install the package:
```bash
pip install .
```

3. Run the application:
```bash
steam-offline-client --help
```

### Method 2: Development Mode

For development, install in editable mode:

```bash
pip install -e .
```

This allows you to make changes to the source code without reinstalling.

### Method 3: Direct Execution

You can also run the script directly without installation:

```bash
python3 steam_offline_client.py --help
```

Make sure the script is executable:
```bash
chmod +x steam_offline_client.py
./steam_offline_client.py --help
```

## Building a Distribution Package

To create distribution packages (wheel and source distribution):

```bash
pip install build
python -m build
```

This will create packages in the `dist/` directory:
- `steam_offline_client-1.0.0-py3-none-any.whl` (wheel package)
- `steam-offline-client-1.0.0.tar.gz` (source distribution)

## Installation from Distribution Package

After building, install the wheel package:

```bash
pip install dist/steam_offline_client-1.0.0-py3-none-any.whl
```

## Verifying Installation

After installation, verify it works:

```bash
steam-offline-client --version
steam-offline-client --status
```

## Uninstallation

To remove the package:

```bash
pip uninstall steam-offline-client
```

## Troubleshooting

### Permission Errors

If you encounter permission errors during installation, use:

```bash
pip install --user .
```

Or use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install .
```

### Python Version

Ensure you're using Python 3.6+:

```bash
python3 --version
```
