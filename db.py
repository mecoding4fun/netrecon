import sqlite3

DB_NAME = "netrecon.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            port INTEGER NOT NULL,
            service TEXT,
            state TEXT,
            risk TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def store_results(ip, results):
    conn = get_connection()
    cur = conn.cursor()

    for r in results:
        cur.execute("""
            INSERT INTO scans (ip, port, service, state, risk)
            VALUES (?, ?, ?, ?, ?)
        """, (
            ip,
            r["port"],
            r["service"],
            r["state"],
            r.get("risk")
        ))

    conn.commit()
    conn.close()


def get_previous_state(ip):
    """
    Returns the previous scan state for an IP as:
    { port: state }
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT port, state
        FROM scans
        WHERE ip = ?
        AND timestamp < (
            SELECT MAX(timestamp)
            FROM scans
            WHERE ip = ?
        )
    """, (ip, ip))

    rows = cur.fetchall()
    conn.close()

    return {port: state for port, state in rows}


def get_latest_scan(ip):
    """
    Returns the latest scan results for an IP
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT port, service, state, risk, timestamp
        FROM scans
        WHERE ip = ?
        AND timestamp = (
            SELECT MAX(timestamp)
            FROM scans
            WHERE ip = ?
        )
        ORDER BY port
    """, (ip, ip))

    rows = cur.fetchall()
    conn.close()

    return rows
