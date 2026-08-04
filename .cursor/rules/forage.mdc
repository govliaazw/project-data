# PostgreSQL MCP Server — Usage Rules

## Tool: `query`

**Server:** `@modelcontextprotocol/server-postgres` (v0.6.2)
**Tool name:** `query`
**Purpose:** Execute read-only SQL queries against the connected PostgreSQL database.

## When to Use
- Inspect database schemas (tables, columns, data types)
- Run SELECT queries to explore or analyze data
- Debug data-related issues during development
- Generate reports from the database
- Any task requiring read-only PostgreSQL access

## Input
| Parameter | Type   | Description              |
|-----------|--------|--------------------------|
| `sql`     | string | The SQL query to execute |

## Key Constraints
- **READ-ONLY**: All queries run inside a `READ ONLY` transaction. INSERT, UPDATE, DELETE, DROP, ALTER, and other write/DDL operations are rejected.
- The server connects via a PostgreSQL connection URL passed as a CLI argument (e.g. `postgresql://localhost/mydb`).

## Usage Pattern
```
query(sql="SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users';")
query(sql="SELECT * FROM orders WHERE created_at > now() - interval '7 days' LIMIT 50;")
```

## Schema Resources
The server also exposes per-table schema resources at `postgres://<host>/<table>/schema` (JSON with column names and data types), auto-discovered from database metadata.

## Configuration
Add to your MCP client config (e.g. `claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```
Replace `postgresql://localhost/mydb` with your actual database connection string.

## Best Practices
1. Always include `LIMIT` on exploratory queries to avoid large result sets.
2. Use `information_schema` queries to discover table structures before writing complex queries.
3. Prefer parameterized-style filtering (WHERE clauses) over fetching full tables.
4. Remember: this tool is read-only — use a separate migration/admin tool for schema changes.
