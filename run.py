import pkg_resources
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
                'key.public': 'PUBLIC_KEY_HERE',
                'key.private': 'PRIVATE_KEY_HERE'
            }
        }
    ]
}


from tropofy import main as tropofy_main, serve_app_cascade

tropofy_app = tropofy_main(apps_config)

if __name__ == "__main__":
    serve_app_cascade(tropofy_app, '0.0.0.0', 8080)
