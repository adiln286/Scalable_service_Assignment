from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection parameters
DB_HOST = 'postgres_container'  # Name of the PostgreSQL container
DB_PORT = '5432'  # Default PostgreSQL port
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Connect to PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Route to get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(products)
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

# Define other endpoints for products CRUD operations

if __name__ == '__main__':
    app.run(debug=True)
