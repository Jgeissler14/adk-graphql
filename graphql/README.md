# ADK GraphQL Learning Project

This repository contains a minimal JavaScript project designed for learning how to integrate Google ADK with a GraphQL API using Apollo Server. The implementation is intentionally incomplete so you can fill in the missing pieces. It now includes a simple PostgreSQL connection so queries can return data from a database instead of hard coded strings.

## Project Structure

- `src/index.js` – entry point that starts an Apollo GraphQL server.
- `src/db.js` – PostgreSQL connection helper used by the resolvers.
- `src/googleAdk.js` – placeholder module for Google ADK calls. Replace the placeholder logic with real API code.
- `schema.sql` – sample PostgreSQL schema for the demo tables.
- `package.json` – basic package configuration with start and test scripts.

## Getting Started

1. Install dependencies (requires Node.js):
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm start
   ```
3. Create a PostgreSQL database, run `schema.sql` to create the tables, and provide connection details through the following environment variables when running the server:
   - `PGHOST`
   - `PGPORT`
   - `PGUSER`
   - `PGPASSWORD`
   - `PGDATABASE`
4. Implement Google ADK integration in `src/googleAdk.js` and extend the GraphQL schema as needed.

## Testing

A placeholder test script is provided. You can add your own tests in the future:

```bash
npm test
```

Feel free to extend this project as you explore Google ADK and GraphQL.
