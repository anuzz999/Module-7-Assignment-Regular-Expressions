import re

class ConcertAnalysis:
    def __init__(self, text):
        self.text = text
    
    def task_one(self):
        """
        Extracts the Capacity and Attendance counts from the text.
        
        Parameters:
        None
        
        Returns:
        tuple: Two lists containing the Capacity and Attendance values as integers.
        """
        
        # Extracting Capacity values
        capacity_matches = re.findall(r'CAPACITY---:(\d+)', self.text)
        capacities = [int(cap) for cap in capacity_matches]
        
        # Extracting Attendance values
        attendance_matches = re.findall(r'ATTENDANCE: (\d+,?\d+)', self.text)
        attendances = [int(att.replace(',', '')) for att in attendance_matches]
        
        return capacities, attendances

    def task_two(text):
        """
        Extracts the names of each musical artist from the text.
    
        Parameters:
        text (str): The text containing concert information.
    
        Returns:
        list: A list containing the names of the musical artists.
        """
    
        # Extracting artist names
        artist_matches = re.findall(r'\*{5}([^*]+)', text)
        artists = [artist.strip() for artist in artist_matches]
    
        return artists

    def task_three(text):
        """
        Extracts the Gross ticket revenue for each concert from the text.
    
        Parameters:
        text (str): The text containing concert information.
    
        Returns:
        list: A list containing the gross ticket revenue as floats.
        """
    
        # Extracting gross ticket revenue
        revenue_matches = re.findall(r'GATE:[^$]*\$([\d,]+)', text)
        revenues = [float(revenue.replace(',', '')) for revenue in revenue_matches]
        return revenues

    def task_four(self, artists, capacities, attendances, revenues):
        """
        Creates a nested dictionary with various calculated values for each artist.
    
        Parameters:
        artists (list): List of artist names.
        capacities (list): List of venue capacities.
        attendances (list): List of concert attendances.
        revenues (list): List of gross ticket revenues.
    
        Returns:
        dict: A nested dictionary with calculated values for each artist.
        """
    
        concert_info = {}
        for artist, capacity, attendance, revenue in zip(artists, capacities, attendances, revenues):
            concert_info[artist] = {
            'average_ticket_price': f"${revenue / attendance:.2f}",
            'multi_word_name': len(artist.split()) > 1,
            'venue_fill_percentage': f"{(attendance / capacity) * 100:.2f}%"
            }
    
        return concert_info

    def task_five(text="FIdD1E7h="):
        """Matches a string with a corrected regular expression."""
        regex = r"\D\w*[^,]="
        match = re.search(regex, text)
        return match.group() if match else "No match"

    def task_six(text="The spy was carefully disguised"):
        """Extracts an adverb from a sentence."""
        regex = r"\b\w+ly\b"
        match = re.search(regex, text)
        return match.group() if match else "No match"




