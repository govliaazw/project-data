# Agent Rules

## PostgreSQL MCP Server (@modelcontextprotocol/server-postgres)

### When to use
Use this tool whenever you need to inspect or query a PostgreSQL database: exploring table schemas, checking column names/types, running SELECT queries, aggregations, joins, or verifying data. The server provides **read-only** access — all queries run inside a READ ONLY transaction.

### Available tool: `query`
- **Tool name:** `foraged__modelcontextprotocol__server-postgres__query`
- **Input:** `sql` (string) — the SQL query to execute.
- **Behavior:** Executes read-only SQL against the connected database. Write operations (INSERT/UPDATE/DELETE/DDL) are rejected because every statement runs in a READ ONLY transaction.

### Key patterns
- **List tables:** `SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';`
- **Inspect a table's columns:** `SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = '<table>';`
- **Read data:** `SELECT * FROM <table> LIMIT 50;`
- **Aggregations:** `SELECT <col>, COUNT(*) FROM <table> GROUP BY <col> ORDER BY 2 DESC;`
- Schema resources are also exposed per table at `postgres://<host>/<table>/schema` (JSON with column names and data types, auto-discovered from database metadata).

### Configuration / required env
- The server is launched via: `npx -y @modelcontextprotocol/server-postgres <connection-string>`
- The connection string is passed as the first positional argument, e.g. `postgresql://localhost/mydb` (replace `mydb` with the target database name). A valid PostgreSQL connection string (host, port, user, password, database) must be configured for the server to connect.

### Tips
- Always prefer `LIMIT` on unbounded SELECTs to avoid huge result sets.
- Quote identifiers with double quotes when table/column names are mixed-case or reserved words.
- Do not attempt writes — they will fail by design; use this server for inspection and analytics only.
