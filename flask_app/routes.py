from flask import jsonify, request
from flask_app.analysis import analyze_receipt_en
from flask_app import app

@app.route("/api/analyze_receipt", methods=['POST'])
def analyze_receipt_api():
    if request.method == 'POST':
        file = request.files['file']
        results = analyze_receipt_en(file)
        
        # Filter DataFrame to include only required fields
        filtered_results = results[['description', 'footprint', 'quantity', 'typical_footprint']]
        
        # Calculate total footprint
        total_footprint = (filtered_results['footprint'] * filtered_results['quantity']).sum()
        
        # Convert filtered DataFrame to dictionary
        results_dict = filtered_results.to_dict(orient='records')
        
        # Add total_footprint to the results dictionary
        results_dict.append({'total_footprint': total_footprint})
        
        # Return JSON response
        return jsonify(results_dict)

# This route is optional if you want to keep the HTML form for manual testing
@app.route("/", methods=['GET'])
def home():
    return "Welcome to the API"

# This route is optional if you want to keep the HTML form for manual testing
@app.route("/submit_receipt", methods=['POST'])
def submit_receipt():
    file = request.files['file']
    results = analyze_receipt_en(file)
    
    # Filter DataFrame to include only required fields
    filtered_results = results[['description', 'footprint', 'quantity', 'typical_footprint']]
    
    # Calculate total footprint
    total_footprint = (filtered_results['footprint'] * filtered_results['quantity']).sum()
    
    # Convert filtered DataFrame to dictionary
    results_dict = filtered_results.to_dict(orient='records')
    
    # Add total_footprint to the results dictionary
    results_dict.append({'total_footprint': total_footprint})
    
    # Return JSON response
    return jsonify(results_dict)

# You can define other routes for your web application as needed
