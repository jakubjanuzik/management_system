#!/usr/bin/env bash
set -x

COMMAND="$1";

shift;

case "$COMMAND" in
  "")
    # No arguments, simply run the app (development)
    python manage.py runserver 0.0.0.0:8000
    ;;

  "manage")
    python manage.py "${@}"
    ;;

  "shell")
    bash "$@"
    ;;

  "test")
    pytest "$@"
    ;;

  *)
    echo "Unknown command: $1."
    exit 1
    ;;
esac
