from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer.writerow([email, subject, message])
# def write_to_file(data):
#     with open('database', 'a') as database:
#         for key, value in data.items():
#             database.write('%s:%s\n' % (key, value))

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not safe to database'
    else:
        return 'something went wrong'

# flask --app server.py run
# flask --app server.py --debug run