#!/usr/bin/env python3

import click
import boto3

#This will allow the help section to provide info on how to run the file
@click.command(help="This tool does label detection")
@click.option('--file', prompt='I need the name of the file in the bucket',
              help='This is the name of the file in the bucket')
def detect(file):
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'aws-test-img-bucket',
                'Name': file,
            },
        },
    )
    #Provides input on what actions are currently being taken while providing labels 
    #for each image
    click.echo(click.style(f"Detecting Labels for: {file}", fg="red"))
    labels = response['Labels']
    for label in labels:
        name = label['Name']
        confidence = round(label['Confidence'],3)
        click.echo(click.style(f"{name}: {confidence}%", fg="green"))

if __name__ == '__main__':
    # pylint: disable=E1120
    detect()
