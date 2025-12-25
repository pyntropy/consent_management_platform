from sqlalchemy import create_engine


engine = create_engine('postgresql://user:pass@localhost:5432/cpm_db')

with engine.connect() as conn:
    result = conn.execute("select 1").fetchone()
    print(result)

