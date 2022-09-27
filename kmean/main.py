from flask import Flask, request
from . import kmean_modul

app = Flask(__name__)


@app.route('/data', methods =['POST'])
def k_mean():
    # TODO(?): log the request?
    app.logger.info("received the request")
    try:
        if not request.values['k_param']:
            return "missing param: k_param", 400
        k_param = request.values['k_param']
        k_clustered_images = kmean_modul.train(int(k_param))
        app.logger.info("finished the request")
    except Exception:
        return "Record not found", 400
    return k_clustered_images


if __name__ == "__main__":
    app.run(debug=True)

    # TODO(?): remove todo's
    #todo: comments
    #todo:git


