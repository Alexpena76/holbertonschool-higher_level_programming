def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): Template string with placeholders for personalization
        attendees (list): List of dictionaries containing attendee information
    """
    
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        personalized_invitation = template
        
        # Replace placeholders with actual values or "N/A" if missing
        # Get the value or None if key doesn't exist, then convert None to "N/A"
        name = attendee.get('name') if attendee.get('name') is not None else "N/A"
        event_title = attendee.get('event_title') if attendee.get('event_title') is not None else "N/A"
        event_date = attendee.get('event_date') if attendee.get('event_date') is not None else "N/A"
        event_location = attendee.get('event_location') if attendee.get('event_location') is not None else "N/A"
        
        # Replace placeholders in the template
        personalized_invitation = personalized_invitation.replace('{name}', str(name))
        personalized_invitation = personalized_invitation.replace('{event_title}', str(event_title))
        personalized_invitation = personalized_invitation.replace('{event_date}', str(event_date))
        personalized_invitation = personalized_invitation.replace('{event_location}', str(event_location))
        
        # Generate output filename
        output_filename = f"output_{index}.txt"
        
        # Write to file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_invitation)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")