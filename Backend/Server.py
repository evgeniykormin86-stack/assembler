from flask import Flask, jsonify, request
from Reports.CISA import CISA


app = Flask(__name__)
cisa: CISA = CISA()


@app.route("/")
def hello():
    return "Hello from assembler SDK!"

@app.route("/2")
def hello2():
    return "Hello from assembler SDK2!"

@app.route("/get-cisa-kev", methods=["GET"])
def get_cisa_kev():
    params = request.get_json(force=True)

    items_per_page = params['items_per_page']
    page_number = params['page_number']

    cisa_kev_data = cisa.get_cisa_kev(
        page_number=page_number,
        items_per_page=items_per_page
    )
    return jsonify({
        "cisa_kev_data": cisa_kev_data
    })


if __name__ == "__main__":
    app.run(debug=True)
