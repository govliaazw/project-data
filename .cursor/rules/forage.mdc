# PostgreSQL MCP Server — Usage Rules

## When to use
Use the `modelcontextprotocol__server-postgres` tools whenever you need to inspect or query a PostgreSQL database directly — e.g., checking table schemas, verifying data, debugging query results, or validating migrations during development.

## Available tools

### `modelcontextprotocol__server-postgres__query`
- **Purpose**: Run a read-only SQL query against the connected PostgreSQL database.
- **Input**: `sql` (string) — the SQL statement to execute.
- **Safety**: ALL queries execute inside a `READ ONLY` transaction. `INSERT`, `UPDATE`, `DELETE`, `DROP`, and any other write/DDL statements will be rejected. Do not attempt writes through this tool.
- **Returns**: Query result rows as JSON.

## Key patterns
- Inspect schemas first: `SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '<table>';`
- List tables: `SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';`
- Always add `LIMIT` to exploratory `SELECT *` queries to avoid huge result sets (e.g., `LIMIT 50`).
- Prefer explicit column lists over `SELECT *` in production-oriented queries.
- The server also exposes per-table schema resources at `postgres://<host>/<table>/schema` (auto-discovered from database metadata) — use these to understand structure before writing queries.

## Configuration / connection
- The server is launched with a PostgreSQL connection string as its argument: `npx -y @modelcontextprotocol/server-postgres postgresql://<user>:<password>@<host>:<port>/<database>`.
- The connection string must be provided when the server starts; if queries fail with connection errors, verify the database URL and network reachability.
