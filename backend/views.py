from flask import Blueprint, jsonify, request
import logging

from rag_utils import  get_generated_prompt_with_evaulation

main_bp = Blueprint('main', __name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@main_bp.route('/api/v1/chat', methods=['POST'])
def index():
    response = {
        "data" : None,
        "error" : None
    }
    statusCode = 404
    try:
        question = request.json.get('question')
        answer = get_generated_prompt_with_evaulation(question)
        answer_dict = answer.to_json()
        
        response["data"] = answer_dict
        statusCode = 200
        
    except Exception as error:
        logging.error(error)
        response['error'] = {
        'message': f"{error}"
        }

    return jsonify(response), statusCode