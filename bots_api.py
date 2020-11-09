from flask import Flask, url_for, jsonify, request, abort, make_response
from markupsafe import escape
from data_base_interfaces import SqlInterface

app = Flask(__name__)

interface = SqlInterface('sqlite_database.db')

# Bots

@app.route('/bots', methods=['GET'])
def get_bots():
    bots = interface.get_bots()
    return jsonify({'bots': bots})


@app.route('/bots/<id>', methods=['GET'])
def get_bot(id):
    bot = interface.get_bot_by_id(id)
    return jsonify({'bot': bot[0]})


@app.route('/bots', methods=['POST'])
def post_bots():
    if not request.json or not 'id' in request.json or not 'name' in request.json:
        abort(400)
    bot = {
        'bot_id': request.json.get('id', ""),
        'bot_name': request.json.get('name', ""),
    }
    result = interface.add_bot(**bot)
    if result:
        return jsonify({'bot': bot}), 201
    else:
        return jsonify({'bot': 'Error'})


@app.route('/bots/<id>', methods=['DELETE'])
def remove_bot(id):
    result = interface.delete_bot(id)
    return jsonify({'result': result})

@app.route('/bots/<id>', methods=['PUT'])
def update_bot(id):
    if not request.json:
        abort(400)
    bot_id = request.json.get('id', "")
    new_name = request.json.get('name', "")
    result = interface.update_bot(bot_id, new_name)
    return jsonify({'update_sucess': result})

# Messages

@app.route('/messages', methods=['GET'])
def get_messages_by_conversation_id():
    conversation_id = request.args.get('conversationId')
    message = interface.get_message_by_conversation_id(conversation_id)
    return jsonify({'messages': message})

@app.route('/messages/<id>', methods=['GET'])
def get_message(id):
    message = interface.get_message_by_id(id)
    if len(message) == 0:
        abort(404)
    return jsonify({'message': message[0]})

@app.route('/messages', methods=['POST'])
def post_message():
    if not request.json:
        abort(400)
    message_id =  request.json.get('id', "")
    conversationId =  request.json['conversationId']
    timestamp = request.json.get('timestamp', "")
    from_point = request.json.get('from', "")
    to_point = request.json.get('to', "")
    text = request.json.get('text', "")

    message = {
        'conversationId': conversationId,
        'timestamp': timestamp,
        'from': from_point,
        'to': to_point,
        'text': text,
    }
    interface.add_message(message_id, conversationId, timestamp, from_point, to_point, text)
    return jsonify(message), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
