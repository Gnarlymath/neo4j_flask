from neo4j import GraphDatabase
# from app import app

# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "dbpassword"

class Neo4jSession():
    # def __init__(self, uri, user, password):
    def __init__(self):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()