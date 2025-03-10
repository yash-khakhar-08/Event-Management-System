from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255,unique=True)

    password = models.CharField(max_length=255)

    profile_picture = models.ImageField(upload_to='profile_pics/')  # Stores the image in 'media/profile_pics/'

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

class Organizer(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    company_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255,unique=True)

    phone_number = models.CharField(max_length=10)

    password = models.CharField(max_length=255)

    profile_picture = models.ImageField(upload_to='organizer/profile_pics/')  # Stores the image in 'media/profile_pics/'

    company_logo = models.ImageField(upload_to='organizer/company_logo/') 

    about_us = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizer'

    def __str__(self):
        return self.name  
    
class EventCategory(models.Model):

    cat_name = models.CharField(max_length=255)

    cat_image = models.ImageField(upload_to='category_pics/',default="")

    cat_desc = models.CharField(max_length=255,default="")

    class Meta:
        db_table = 'event_category'

class Event(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    price = models.CharField(max_length=6, default="0")

    total_tickets = models.CharField(max_length=6,default="0")

    date = models.DateField()

    time = models.TimeField()

    location = models.CharField(max_length=255)

    state = models.CharField(max_length=40,default="Andhra Pradesh")

    description = models.CharField(max_length=255)

    cover_image = models.ImageField(upload_to='organizer/event_cover_images/',default="")

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="events")

    event_category = models.ForeignKey("EventCategory", on_delete=models.CASCADE, related_name="category",default="")

    class Meta:
        db_table = 'event'

    def __str__(self):
        return f"{self.name} - {self.organizer.name}"  # Show event + organizer name
    
class EventPics(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_pics")  # ForeignKey to Event

    image = models.ImageField(upload_to='organizer/event_images/')  # Image field for storing pictures

    def __str__(self):
        return f"Image for {self.event.name}"

class EventTickets(models.Model):

    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event")

    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")

    date = models.DateField()

    time = models.TimeField()

    no_of_tickets = models.CharField(max_length=1)

    total_amount = models.CharField(max_length=6)

    class Meta:
        db_table = 'event_tickets'

    def __str__(self):
        return f"Ticket for {self.event_id.name} - {self.user_id.name}"
    

class CustomizeEvent(models.Model):

    name = models.CharField(max_length=255)

    description = models.CharField(max_length=255)

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="customize_events")

    cover_image = models.ImageField(upload_to='organizer/customize_event_cover_images/')

    class Meta:
        db_table = 'customize_events'

    def __str__(self):
        return f"{self.name} - {self.organizer.name}"
    
class CustomizeEventTheme(models.Model):

    customize_event = models.ForeignKey("CustomizeEvent", on_delete=models.CASCADE, related_name="customize_event_pics")  # ForeignKey to Event

    image = models.ImageField(upload_to='organizer/event_theme/')  # Image field for storing pictures

    price = models.CharField(max_length=10)

    def __str__(self):
        return f"Image for {self.customize_event.name}"
    

class EventRequest(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_id")

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="organizer_id",default=1)

    theme = models.ForeignKey("CustomizeEventTheme", on_delete=models.CASCADE, related_name="theme_id")

    date = models.DateField()

    time = models.TimeField()

    suggestions = models.CharField(max_length=255)

    location = models.CharField(max_length=255,default="")

    state = models.CharField(max_length=50,default="")

    status = models.CharField(max_length=255,default="Pending")

    class Meta:
        db_table = 'event_request'

    def __str__(self):
        return f"{self.theme.price} - {self.user.name} - {self.status} "






    


