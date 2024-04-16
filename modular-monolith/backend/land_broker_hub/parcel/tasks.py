import requests
from celery import shared_task

from .models import Parcel


@shared_task(bind=True)
def monitor_parcel_offers(self):
    """Periodic task to monitor parcels with active offers"""

    # Get unique combinations of block number and subdivision number
    combinations = Parcel.objects.values('block_number', 'subdivision_number').distinct()

    for combination in combinations:
        block_number = combination['block_number']
        subdivision_number = combination['subdivision_number']

        # Get parcels in the combination
        parcels_in_combination = Parcel.objects.filter(
            block_number=block_number,
            subdivision_number=subdivision_number
        )

        # Check if all parcels in the combination have active offers
        if all(p.has_active_offer() for p in parcels_in_combination):
            # Trigger notification (post to dummy API)
            response = post_to_dummy_api(block_number, subdivision_number)
            # Log response or handle as needed


def post_to_dummy_api(block_number, subdivision_number):
    """Dummy post handler"""

    # Dummy API endpoint URL
    dummy_api_url = 'http://example.com/dummy-api'

    # Dummy payload
    payload = {
        'block_number': block_number,
        'subdivision_number': subdivision_number,
        'message': 'All parcels in this combination have active offers'
    }

    # Send POST request to dummy API
    # You can use any HTTP client library like requests or Django's built-in capabilities
    # For simplicity, I'm using JsonResponse to simulate a response
    response = JsonResponse(payload)

    # Return response (for logging purposes)
    return response  