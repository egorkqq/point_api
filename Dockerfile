FROM python:3.13-slim

RUN apt update && apt -y upgrade

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /point

COPY ./ ./

ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN uv sync --frozen
