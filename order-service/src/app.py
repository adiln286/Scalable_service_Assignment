from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection parameters
DB_HOST = 'postgres_container'  # Name of the PostgreSQL container
DB_PORT = '5432'  # Default PostgreSQL port
DB_NAME = 'order_db'
DB_USER = 'order_service_user'
DB_PASSWORD = 'password'

# Connect to PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=postgres-container,
            port=5432,
            database=postgres,
            user=postgres,
            password=postgres
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders")
        orders = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(orders)
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

# Define other endpoints for orders CRUD operations

if __name__ == '__main__':
    app.run(debug=True)
