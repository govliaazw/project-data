# Agent Rules

## PostgreSQL MCP Server (@modelcontextprotocol/server-postgres)

### When to use
Use the PostgreSQL query tool whenever you need to inspect or query a PostgreSQL database: exploring table schemas, running SELECT queries, checking row counts, or verifying data. The server provides **read-only** access — all queries run inside a READ ONLY transaction, so INSERT/UPDATE/DELETE/DDL statements are not permitted.

### Available tool
- **`query`** — Execute a read-only SQL query against the connected database.
  - Input: `sql` (string) — the SQL query to execute.
  - Returns: query result rows as JSON.

### Connection
The server is started with a PostgreSQL connection string passed as a CLI argument:
```
npx -y @modelcontextprotocol/server-postgres postgresql://localhost/mydb
```
Set the `POSTGRES_CONNECTION_STRING` environment variable (or pass the connection string directly) in the format `postgresql://[user[:password]@]host[:port]/dbname`.

### Key patterns
1. **Discover schema first**: Table schemas are exposed as MCP resources at `postgres://<host>/<table>/schema` (JSON with column names and data types, auto-discovered from database metadata). You can also query `information_schema.tables` and `information_schema.columns` directly.
2. **Always limit results**: Use `LIMIT` on exploratory queries to avoid huge result sets.
3. **Read-only safety**: Never attempt writes — the server enforces READ ONLY transactions.

### Example queries
```sql
-- List all tables
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';

-- Inspect a table's columns
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users';

-- Query data
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;
```

### Notes
- Package: `@modelcontextprotocol/server-postgres` v0.6.2 (official MCP reference server, MIT license).
- Only the `query` tool is exposed; schema info comes via resources or information_schema queries.
