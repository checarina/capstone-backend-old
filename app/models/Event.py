from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    type = db.Column(db.String)
    notes = db.Column(db.String)

    pet_id = db.Column(db.Integer, db.ForeignKey("pet.id"))
    pet = db.relationship("Pet", back_populates = "events")

    @classmethod
    def from_dict(cls, event_data):
        new_event = Event(
            type = event_data["type"],
            notes = event_data["notes"],

        )
        return new_event
    
    def to_dict(self):
        event_dict = {}
        event_dict["id"] = self.id
        event_dict["type"] = self.type
        event_dict["timestamp"] = self.timestamp

        return event_dict