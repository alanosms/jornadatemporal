from flask import Flask, jsonify
import datetime

app = Flask(__name__)

def calculate_percentages(date):
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Please provide the date in 'YYYY-MM-DD' format."}), 400

    end_of_year_2024 = datetime.datetime(2024, 12, 31, 23, 59, 59)

    start_of_year = datetime.datetime(date.year, 1, 1)
    start_of_week = date - datetime.timedelta(days=date.weekday())
    start_of_month = datetime.datetime(date.year, date.month, 1)

    hours_per_year = 8760  # Assuming a non-leap year
    hours_per_week = 168
    hours_per_month = (start_of_month.replace(month=start_of_month.month % 12 + 1, day=1) - start_of_month).total_seconds() / 3600

    total_hours_passed_year = (date - start_of_year).total_seconds() / 3600
    total_hours_passed_week = (date - start_of_week).total_seconds() / 3600
    total_hours_passed_month = (date - start_of_month).total_seconds() / 3600

    total_hours_reference_year = (end_of_year_2024 - start_of_year).total_seconds() / 3600
    total_hours_reference_week = (end_of_year_2024 - start_of_week).total_seconds() / 3600
    total_hours_reference_month = (end_of_year_2024 - start_of_month).total_seconds() / 3600

    percentage_of_year_passed = min((total_hours_passed_year / total_hours_reference_year) * 100, 100)
    percentage_of_week_passed = min((total_hours_passed_week / total_hours_reference_week) * 100, 100)
    percentage_of_month_passed = min((total_hours_passed_month / total_hours_reference_month) * 100, 100)

    percentage_of_year_passed_formatted = "{:.2f}".format(percentage_of_year_passed)
    percentage_of_week_passed_formatted = "{:.2f}".format(percentage_of_week_passed)
    percentage_of_month_passed_formatted = "{:.2f}".format(percentage_of_month_passed)

    return {
        "percentage_of_year_passed": percentage_of_year_passed_formatted,
        "percentage_of_week_passed": percentage_of_week_passed_formatted,
        "percentage_of_month_passed": percentage_of_month_passed_formatted
    }

@app.route('/percentages/<date>', methods=['GET'])
def get_percentages(date):
    percentages = calculate_percentages(date)
    return jsonify(percentages)

if __name__ == '__main__':
    app.run(debug=True)
