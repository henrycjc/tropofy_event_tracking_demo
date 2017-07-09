import pkg_resources
import json

try:
    with open('settings.json') as f:
        data = json.load(f)

        apps_config = {
            'tropofy': {
                'api_url': 'https://api.tropofy.com',
                'auth_url': 'https://auth.tropofy.com',
            },
            'database': {
                'url': 'sqlite:///events.db',
            },
            'apps': [
                {
                    'module': 'event_tracking_demo',
                    'classname': 'EventTrackingDemoApp',
                    'config': {
                        'key.public': data['API_PUBLIC'],
                        'key.private': data['API_PRIVATE']
                    }
                }
            ]
        }
except Exception as e:
    print("settings.json is missing or corrupt. There is an example for you to modify.")
    exit(0)

from tropofy import main as tropofy_main, serve_app_cascade

tropofy_app = tropofy_main(apps_config)

if __name__ == "__main__":
    serve_app_cascade(tropofy_app, '0.0.0.0', 8080)
