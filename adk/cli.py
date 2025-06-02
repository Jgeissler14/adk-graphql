"""Command line interface for the ADK demo project."""

from __future__ import annotations

import argparse
import threading
import webbrowser


def web_command(port: int) -> None:
    """Run the web server and open a browser."""
    url = f"http://localhost:{port}/"

    def open_browser() -> None:
        webbrowser.open(url)

    threading.Timer(1.0, open_browser).start()

    from adk.webapp import app  # Import here to avoid heavy deps on CLI startup
    app.run(host="0.0.0.0", port=port)


def main() -> None:
    parser = argparse.ArgumentParser(description="ADK demonstration commands")
    sub = parser.add_subparsers(dest="command", required=True)

    web_parser = sub.add_parser("web", help="Launch the local web chat interface")
    web_parser.add_argument("--port", type=int, default=8000, help="Port to listen on")

    args = parser.parse_args()

    if args.command == "web":
        web_command(args.port)


if __name__ == "__main__":
    main()
