# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from django.utils import timezone
# from .models import TofData, TofData1, TofData2

# # Initialize message buffer and batch size
# MESSAGE_BUFFER = {}
# BATCH_SIZE = 2000

# @shared_task
# def process_data(timestamp, data, topic):
#     value1 = data.get('value1')

#     # Use topic to determine which model to use for storing data
#     if topic == 'tof':
#         model_class = TofData
#     elif topic == 'tof1':
#         model_class = TofData1
#     elif topic == 'tof2':
#         model_class = TofData2
#     else:
#         raise ValueError('Invalid topic')

#     # Add data to message buffer
#     if model_class not in MESSAGE_BUFFER:
#         MESSAGE_BUFFER[model_class] = []
#     MESSAGE_BUFFER[model_class].append(model_class(timestamp=timestamp, value1=value1))

#     # Check if buffer is full
#     if len(MESSAGE_BUFFER[model_class]) >= BATCH_SIZE:
#         # Save all the records in the buffer to the database in a single query
#         model_class.objects.bulk_create(MESSAGE_BUFFER[model_class])
#         MESSAGE_BUFFER[model_class] = []


#------------------------Just skipping every other message------------------------

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone
from .models import TofData, TofData1, TofData2, VizData, LdrData, IncidentData

# Initialize message counter and step size
MESSAGE_COUNTER = 0
STEP_SIZE = 1

@shared_task
def process_data(timestamp, data, topic):
    global MESSAGE_COUNTER

    # Increment message counter
    MESSAGE_COUNTER +=1

    # Only process and save message if it matches the step size
    if MESSAGE_COUNTER % STEP_SIZE == 0:
        value1 = data.get('value1')
        value2 = data.get('value2')
        value3 = data.get('value3')

        # Use topic to determine which model to use for storing data
        if topic == 'tof':
            model_class = TofData
        elif topic == 'tof1':
            model_class = TofData1
        elif topic == 'tof2':
            model_class = TofData2
        elif topic == 'viz':
            model_class = VizData
        elif topic == 'ldr':
            model_class = LdrData
        else:
            raise ValueError('Invalid topic')

        # Save data to database
        tof_data = model_class.objects.create(timestamp=timestamp, value1=value1, value2=value2, value3=value3, )
        tof_data.save()

        # Reset message counter if it reaches the step size
        if MESSAGE_COUNTER == STEP_SIZE:
            MESSAGE_COUNTER = 0



#---------------------------------------------combined----------------


# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from django.utils import timezone
# from .models import TofData, TofData1, TofData2

# # Initialize message counter and step size
# MESSAGE_COUNTER = 0
# STEP_SIZE = 2

# # Initialize message buffer and batch size
# MESSAGE_BUFFER = {
#     TofData: [],
#     TofData1: [],
#     TofData2: [],
# }
# BATCH_SIZE = 500

# @shared_task
# def process_data(timestamp, data, topic):
#     global MESSAGE_COUNTER

#     # Increment message counter
#     MESSAGE_COUNTER += 1

#     # Only process and save message if it matches the step size
#     if MESSAGE_COUNTER % STEP_SIZE == 0:
#         value1 = data.get('value1')

#         # Use topic to determine which model to use for storing data
#         if topic == 'tof':
#             model_class = TofData
#         elif topic == 'tof1':
#             model_class = TofData1
#         elif topic == 'tof2':
#             model_class = TofData2
#         else:
#             raise ValueError('Invalid topic')

#         # Add message to buffer for the corresponding model class
#         MESSAGE_BUFFER[model_class].append(model_class(timestamp=timestamp, value1=value1))

#         # Flush buffer if it reaches the batch size
#         if len(MESSAGE_BUFFER[model_class]) == BATCH_SIZE:
#             model_class.objects.bulk_create(MESSAGE_BUFFER[model_class])
#             MESSAGE_BUFFER[model_class] = []

#         # Reset message counter if it reaches the step size
#         if MESSAGE_COUNTER == STEP_SIZE:
#             MESSAGE_COUNTER = 0




@shared_task
def create_incident(timestamp):
    # Get latest values from all 5 topics
    tof_value1 = TofData.objects.last().value1
    tof1_value1 = TofData1.objects.last().value1
    tof2_value1 = TofData2.objects.last().value1
    viz_value1 = VizData.objects.last().value1
    ldr_value1 = LdrData.objects.last().value1

    # Check if any of the values is equal to 2, indicating an obstacle is detected
    if tof_value1 == 2 or tof1_value1 == 2 or tof2_value1 == 2 or viz_value1 == 2 or ldr_value1 == 2:

        # Get current GPS coordinates (placeholder)
        latitude = 0.0
        longitude = 0.0

        # Get current speed (placeholder)
        speed = 0.0

        # Placeholder values for breakAction, override, zone_coord1, zone_coord2, and zone
        break_action = True
        override = False
        zone_coord1 = 0
        zone_coord2 = 0
        zone = 0

        # Create a new incident record
        incident = IncidentData.objects.create(
            timestamp=timestamp,
            description='Obstacle detected',
            value1=tof_value1,
            value2=tof1_value1,
            value3=tof2_value1,
            value4=viz_value1,
            value5=ldr_value1,
            latitude=latitude,
            longitude=longitude,
            breakAction=break_action,
            override=override,
            speed=speed,
            zone_coord1=zone_coord1,
            zone_coord2=zone_coord2,
            zone=zone
        )
        incident.save()
