import sqlite3

DB_NAME = "resume_history.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        resume_name TEXT,

        predicted_career TEXT,

        match_score INTEGER,

        ats_score INTEGER,

        quality_score INTEGER,

        resume_grade TEXT,

        hiring_recommendation TEXT,

        skills_count INTEGER,

        domain_count INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(
    resume_name,
    predicted_career,
    match_score,
    ats_score,
    quality_score,
    resume_grade,
    hiring_recommendation,
    skills_count,
    domain_count
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analyses (

        resume_name,

        predicted_career,

        match_score,

        ats_score,

        quality_score,

        resume_grade,

        hiring_recommendation,

        skills_count,

        domain_count

    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        resume_name,

        predicted_career,

        match_score,

        ats_score,

        quality_score,

        resume_grade,

        hiring_recommendation,

        skills_count,

        domain_count
    ))

    conn.commit()
    conn.close()


def get_all_analyses():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM analyses
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_analysis(record_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM analyses WHERE id = ?",
        (record_id,)
    )

    conn.commit()
    conn.close()


def get_statistics():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        COUNT(*),
        AVG(match_score),
        AVG(ats_score),
        AVG(quality_score),
        MAX(match_score)
    FROM analyses
    """)

    stats = cursor.fetchone()

    conn.close()

    return stats