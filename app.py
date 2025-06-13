from flask import Flask, jsonify
import os
from azure.cosmos import CosmosClient, exceptions

app = Flask(__name__)

# Set up Cosmos DB connection using environment variables
cosmos_url = os.getenv('COSMOS_URL')  # Cosmos DB endpoint URL from Azure environment variable
cosmos_key = os.getenv('COSMOS_KEY')  # Cosmos DB primary key from Azure environment variable

# Initialize Cosmos client
client = CosmosClient(cosmos_url, cosmos_key)

# Define the database and container to use
database_name = 'DemoDB'
container_name = 'DemoContainer'

# Get the database and container client
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

@app.route('/')
def home():
    try:
        # Example of fetching data from CosmosDB
        item = container.read_item(item="1", partition_key="1")
        
        return jsonify({
            'message': 'Hello from Azure Web App',
            'item_from_cosmosdb': item
        })
    except exceptions.CosmosResourceNotFoundError:
        return jsonify({'error': 'Item not found in Cosmos DB'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
