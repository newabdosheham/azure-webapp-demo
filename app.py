from flask import Flask, jsonify
import os
import logging
from azure.cosmos import CosmosClient

app = Flask(__name__)

# Application Insights Logging (for monitoring)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# CosmosDB setup
cosmos_url = os.getenv('COSMOS_URL')
cosmos_key = os.getenv('COSMOS_KEY')
client = CosmosClient(cosmos_url, cosmos_key)
database_name = 'DemoDB'
container_name = 'DemoContainer'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

@app.route('/')
def home():
    # Example of fetching data from CosmosDB
    item = container.read_item(item="1", partition_key="1")
    return jsonify({
        'message': 'Hello from Azure Web App',
        'item_from_cosmosdb': item
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
