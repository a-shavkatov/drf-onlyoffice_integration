# ONLYOFFICE Integration Example

This project demonstrates a simple integration of ONLYOFFICE Document Server with a Django backend application. It provides basic functionality for document management and editing using ONLYOFFICE.

## Project Structure

The project consists of several main components:
- Django backend application
- ONLYOFFICE Document Server integration
- MinIO for document storage
- Docker configuration for easy deployment

## Features

- Document management (upload, view, edit)
- Template management
- User authentication
- Integration with ONLYOFFICE Document Server
- MinIO storage integration

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- ONLYOFFICE Document Server (handled via Docker)

## Quick Start

1. Clone the repository
2. Start the services using Docker Compose:
```bash
docker-compose up -d
```

3. The application will be available at `http://localhost:8000`

## Project Components

- `backend/` - Django application
  - `src/api/` - API endpoints and integration logic
  - `src/apps/` - Django applications (documentation, user management, etc.)
- `docker/` - Docker configuration files
- `docker-compose.yml` - Docker Compose configuration

## Configuration

The project uses environment variables for configuration. Check the `docker-compose.yml` file for the required environment variables.

## API Documentation

The API includes endpoints for:
- Document management
- User authentication
- ONLYOFFICE callback handling
- Template management

## License

[MIT License](LICENSE)

## Note

This is a demonstration project showing how to integrate ONLYOFFICE Document Server with a Django backend. It's intended as a learning resource and starting point for similar integrations.
