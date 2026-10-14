
import json

def lambda_handler(event, context):
    length = event.get("length", 6)
    width = event.get("width", 7)

    area = length * width

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "AWS Lambda сәтті жұмыс істеді!",
            "length": length,
            "width": width,
            "area": area
        }, ensure_ascii=False)
    }