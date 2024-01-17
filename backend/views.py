from flask import Blueprint, jsonify, request
import json
import logging
from exectuors import get_agent_executor

main_bp = Blueprint('main', __name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


analyst_agent_openai = get_agent_executor()


@main_bp.route('/', methods=['POST'])
def index():
    data = request.json
    response = {
        "data" : None,
        "error" : None
    }
    statusCode = 404
    try:
        response["data"] = "answer"
        statusCode = 200
    except Exception as error:
        logging.error(error)
        response['error'] = {
        'message': f"{error}"
        }
        statusCode = 404
    return jsonify(response), statusCode