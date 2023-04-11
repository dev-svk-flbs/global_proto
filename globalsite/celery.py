import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globalsite.settings')

# Initialize Celery instance
app = Celery('globalsite')

# Load tasks from all registered Django app configs
app.autodiscover_tasks()

# Set broker URL and backend for Celery
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
)

