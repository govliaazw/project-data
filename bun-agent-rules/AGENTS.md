## my_tool: True

# PostgreSQL MCP Server Usage Instructions

## When to use
Use this tool whenever you need to query a PostgreSQL database using natural language or SQL. It provides read-only access to inspect database schemas and execute read-only queries.

## Key commands/patterns
- **Tool name**: `foraged__modelcontextprotocol__server-postgres__query`
- **Input**: `sql` (string) — The SQL query to execute
- All queries are executed within a READ ONLY transaction
- Schema resources are available at `postgres://<host>/<table>/schema` with JSON schema info (column names and data types) auto-discovered from database metadata

## Configuration
- **Install command**: `npx -y @modelcontextprotocol/server-postgres`
- **Connection string**: Pass a PostgreSQL connection URL as an argument, e.g. `postgresql://localhost/mydb`
- Replace `/mydb` with your target database name

## Example
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ]
    }
  }
}
```
