import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "resumescence.db")

'''
outline
 - get_projects_list()
 - get_project(project_id)
 - get_components(project_id)
 - get_component(component_id)
'''

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS components (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        );
    """)
    conn.commit()
    conn.close()


def get_projects_list():
    conn = get_connection()
    projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return [dict(p) for p in projects]


def get_project(project_id: str):
    conn = get_connection()
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    conn.close()
    return dict(project) if project else None


def get_components(project_id: str):
    conn = get_connection()
    components = conn.execute("SELECT * FROM components WHERE project_id = ?", (project_id,)).fetchall()
    conn.close()
    return [dict(c) for c in components]


def get_component(component_id: str):
    conn = get_connection()
    component = conn.execute("SELECT * FROM components WHERE id = ?", (component_id,)).fetchone()
    conn.close()
    return dict(component) if component else None


# Initialize the database on import
init_db()