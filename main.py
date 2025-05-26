import sys
import os
from app import create_app
import traceback
from flask import jsonify

# Print environment for debugging
print(f"Environment: {os.environ.get('FLASK_ENV', 'not set')}", file=sys.stderr)
print(f"Debug mode: {os.environ.get('FLASK_DEBUG', 'not set')}", file=sys.stderr)

try:
    # Create Flask application using the factory pattern
    app = create_app()
    print("App successfully created", file=sys.stderr)
    
    @app.errorhandler(500)
    def internal_error(error):
        print(f"500 error: {str(error)}", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        return jsonify(error=str(error), traceback=traceback.format_exc()), 500
        
except Exception as e:
    print(f"Error creating app: {str(e)}", file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    raise

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 