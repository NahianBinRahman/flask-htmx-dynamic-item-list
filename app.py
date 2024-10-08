from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List to store items
items = []


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return render_template('item.html', item=item)


if __name__ == '__main__':
    app.run(debug=True)
