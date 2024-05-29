from flask import Flask, render_template, request

app = Flask(__name__)

html_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Ипотечный калькулятор</title>
</head>
<body>
    <h1>Ипотечный калькулятор</h1>
    <form action="/calculate" method="post">
        <label for="property_value">Стоимость недвижимости:</label>
        <input type="number" name="property_value"><br><br>

        <label for="down_payment">Первоначальный взнос:</label>
        <input type="number" name="down_payment"><br><br>

        <label for="loan_term">Срок кредита (в месяцах):</label>
        <input type="number" name="loan_term"><br><br>

        <label for="interest_rate">Процентная ставка:</label>
        <input type="number" step="0.01" name="interest_rate"><br><br>

        <label for="monthly_fee">Ежемесячная комиссия:</label>
        <input type="number" name="monthly_fee"><br><br>

        <input type="submit" value="Рассчитать">
    </form>
</body>
</html>
'''


@app.route('/')
def index():
    return html_form


@app.route('/calculate', methods=['POST'])
def calculate():
    property_value = float(request.form['property_value'])
    down_payment = float(request.form['down_payment'])
    loan_term = int(request.form['loan_term'])
    interest_rate = float(request.form['interest_rate'])
    monthly_fee = float(request.form['monthly_fee'])

    loan_amount = property_value - down_payment
    monthly_interest_rate = interest_rate / 100 / 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-loan_term)) + monthly_fee

    return f'<h1>Ежемесячный платеж: {monthly_payment}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
